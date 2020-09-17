from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow import keras
from PIL import Image
import numpy as np
import time
import cv2
import os
import uuid

KERAS_MODEL_PATH = "config/keras_model"
CASCADE_CLASSIFIER_PATH = "config/classifiers/haarcascade_frontalface_alt2.xml"
FACENET_PROTO = "config/facenet/deploy.prototxt.txt"
FACENET_CAFFEMODEL = "config/facenet/res10_300x300_ssd_iter_140000.caffemodel"
CV2_TRACKERS = {
    "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "mosse": cv2.TrackerMOSSE_create,
}
LOGGING_DEFAULT = {
    "detections": 0,
    "total_time": 0.0,
    "avg_time": 0.0,
    "min_time": 10000.0,
    "max_time": -10000.0,
}
tracker_name = "csrt"


class Detector:
    def __init__(
        self,
        tolerance=0.15,
        face_detector_id=0,
        facenet_confidence_threshold=0.50,
        detect_every_n_frames=14,
        save_every_n_frames=30,
        max_pictures_to_keep=24,
    ):
        self.face_detector_id = face_detector_id
        self.facenet_confidence_threshold = facenet_confidence_threshold

        # load our model weights
        try:
            self.model = keras.models.load_model(
                os.path.join(os.path.dirname(__file__), KERAS_MODEL_PATH)
            )  # read from relative path
            print("keras model loaded successfully")
        except Exception as e:
            print(f"error loading keras model: {e}")
        if self.face_detector_id == 0:
            try:
                self.facenet = cv2.dnn.readNetFromCaffe(
                    os.path.join(os.path.dirname(__file__), FACENET_PROTO),
                    os.path.join(os.path.dirname(__file__), FACENET_CAFFEMODEL),
                )  # read from relative path
                print("facenet caffe loaded successfully")
            except Exception as e:
                print(f"error loading facenet: {e}")
        else:
            try:
                self.face_cascade = cv2.CascadeClassifier(
                    os.path.join(os.path.dirname(__file__), CASCADE_CLASSIFIER_PATH)
                )  # read from relative path
                print("cascade classifier weights loaded successfully")
            except Exception as e:
                print(f"error loading opencv cascade classifier weights: {e}")

        # set up object variables
        self.logs = LOGGING_DEFAULT
        self.tolerance = tolerance
        self.detect_every_n_frames = (
            detect_every_n_frames  # run detection once every n frames
        )
        self.save_every_n_frames = save_every_n_frames
        self.max_pictures_to_keep = max_pictures_to_keep
        self.trackers = []
        self.frames_elasped = 0  # keep track of frames passed

    def predict(self, img, print_logs=False):
        start_time = time.process_time()  # start logging time

        img = np.array(img)  # convert to numpy array for processing
        faces = self.get_faces(img)

        # helper variable to let frontend know whether to re-fetch images
        detection_log_updated = False
        results = []
        for (x, y, w, h) in faces:
            # crop image to face
            img_crop = img[y : y + h, x : x + w]
            facemask_result = self.predict_facemask(img_crop)
            result = self.process_result(
                facemask_result, [int(v) for v in [x, y, w, h]]
            )

            # check if valid condition for us to save the cropped face image
            # i.e. no mask worn AND frames_elasped multiple of save_every_n_frames
            if (
                not result["wearing_mask"]
                and self.frames_elasped % self.save_every_n_frames == 0
            ):
                detection_log_updated = True
                # don't overload the directory with pictures
                # keep up to max_pictures_to_keep
                self.keep_n_most_recent_files(
                    "detection_log", self.max_pictures_to_keep - 1
                )

                im = Image.fromarray(img_crop)
                im.save(f"detection_log/{uuid.uuid4().hex}.png")

            results.append(result)

        ####################################################################
        ####################### LOGGING START ##############################
        ####################################################################
        if len(faces) > 0:
            time_taken = time.process_time() - start_time  # end logging time
            if self.frames_elasped % 1000 == 0:
                self.reset_logs()  # reset logs every 1000 frames
            self.update_logs(time_taken)

        if print_logs:
            print("FRAMES ELAPSED:", self.frames_elasped)
            if len(faces) > 0:
                self.print_logs()
                print("RESULT:", results)
            else:
                print("NO FACES DETECTED")
        ####################################################################
        ####################### LOGGING END ################################
        ####################################################################

        return results, detection_log_updated

    def predict_facemask(self, face_img):
        face_img = cv2.resize(face_img, (244, 244))
        face_img = img_to_array(face_img)
        face_img = preprocess_input(face_img)
        face_img = face_img.reshape((1, 244, 244, 3))  # to match our input tensor shape
        result = self.model.predict(face_img)
        return result[0]

    def get_faces(self, img):
        algo = (
            self.get_faces_facenet
            if self.face_detector_id == 0
            else self.get_faces_cascade
        )
        if (
            self.frames_elasped % self.detect_every_n_frames == 0
        ):  # run face detection algo
            faces = algo(img)
            self.trackers = []
            for face_bb in faces:
                tracker = CV2_TRACKERS[tracker_name]()
                tracker.init(img, face_bb)
                self.trackers.append(tracker)
        else:  # use tracking data
            faces = []
            for tracker in self.trackers:
                (success, box) = tracker.update(img)
                if success:
                    (x, y, w, h) = [int(v) for v in box]
                    faces.append((x, y, w, h))

        self.frames_elasped += 1
        return faces

    def get_faces_cascade(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray, 1.1, 8
        )  # scaleFactor, minNeighbors
        return [(x, y, w, h) for [x, y, w, h] in faces]

    def get_faces_facenet(self, img):
        (h, w) = img.shape[:2]
        # blob = cv2.dnn.blobFromImage(img, 1.0, (224, 224), (104.0, 177.0, 123.0),)
        blob = cv2.dnn.blobFromImage(
            cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0),
        )
        self.facenet.setInput(blob)
        detections = self.facenet.forward()

        faces = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence < self.facenet_confidence_threshold:
                continue

            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (start_x, start_y, end_x, end_y) = box.astype("int")
            faces.append((start_x, start_y, end_x - start_x, end_y - start_y))

        return faces

    def process_result(self, result, coords):
        """
        helper function that takes in facemask detection result and face
        bounding box coords and returns a dictionary 
        """
        (mask_prob, no_mask_prob) = result

        # introduce tolerance to lower false positive rate
        no_mask_prob += self.tolerance

        wearing_mask = True
        prob = mask_prob
        if no_mask_prob > mask_prob:
            wearing_mask = False
            prob = no_mask_prob

        content = {
            "wearing_mask": wearing_mask,
            "confidence": prob,
            "coords": coords,
        }

        return content

    def keep_n_most_recent_files(self, directory, n):
        """
        keeps the n most recent files in directory and deletes the rest
        """
        os.chdir(directory)
        files = sorted(
            filter(os.path.isfile, os.listdir(".")), key=os.path.getmtime, reverse=True
        )
        files = files[n:]
        for f in files:
            os.remove(f)
        os.chdir("..")

    def reset_logs(self):
        """
        reset the detector's logging
        """
        self.logs = LOGGING_DEFAULT

    def update_logs(self, time_taken):
        """
        update our detector's logs
        """
        self.logs["latest_time"] = time_taken
        self.logs["total_time"] += time_taken
        self.logs["detections"] += 1
        self.logs["avg_time"] = self.logs["total_time"] / self.logs["detections"]
        self.logs["min_time"] = min(self.logs["min_time"], time_taken)
        self.logs["max_time"] = max(self.logs["max_time"], time_taken)

    def get_logs(self):
        return self.logs

    def print_logs(self):
        print(f"latest time taken for detection: {round(self.logs['latest_time'], 2)}s")
        print(f"total detections performed: {self.logs['detections']}")
        print(f"average detection time: {round(self.logs['avg_time'],2)}s")
        print(f"min detection time: {round(self.logs['min_time'],2)}s")
        print(f"max detection time: {round(self.logs['max_time'],2)}s")
