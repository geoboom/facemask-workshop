import os
import time
import io
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pydantic import typing
from PIL import Image
from random import randrange

from detector.detector import Detector

# fastAPI setup
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# pre-create the detection_log/ folder if doesn't already exist
if not os.path.exists("detection_log"):
    os.makedirs("detection_log")

app.mount(
    "/detection_log", StaticFiles(directory="detection_log"), name="detection_log",
)

# expected schema of our response data i.e. the form it should take
class DetectionResult(BaseModel):
    wearing_mask: bool
    confidence: float
    coords: list


class DetectionsData(BaseModel):
    detection_log_updated: bool
    logs: typing.Any
    results: typing.List[DetectionResult]


class Temp(BaseModel):
    coords: typing.List[typing.Any]


# initialize our Detector object
detector = Detector()

# Our client will send a HTTP POST request to this endpoint
# with the image (video frame) as payload, stored in formData of 
# the post request's body (read more on POST requests online)
@app.post("/detect", response_model=DetectionsData)
async def detect_face_mask(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        pil_image = Image.open(io.BytesIO(contents))

        # predict using our detector and store the results in results (list)
        # and whether detection log has been updated in detection_log_updated (bool)
        results, detection_log_updated = detector.predict(pil_image, print_logs=True)

        # get the latest logs e.g. average detection time, num_detections, etc
        # after the last prediction/inference was performed
        logs = detector.get_logs()

        return {
            "results": results,
            "detection_log_updated": detection_log_updated,
            "logs": logs,
        }

    except Exception as e:
        print(f"POST /detect error: {e}")
        raise HTTPException(status_code=500, detail="Detection failed.")


# When our client sends a HTTP GET request to this endpoint, it'll receive a
# list of URLs corresponding to where the images are saved on the server.
# This list is sorted by creation time in descending order i.e. latest to earliest.
# You can actually visit localhost:8000/detection_log to check it out.
@app.get("/detection_log", response_model=typing.List[typing.Any])
async def get_detection_log():
    os.chdir("detection_log")
    files = sorted(
        filter(os.path.isfile, os.listdir(".")), key=os.path.getmtime, reverse=True
    )
    os.chdir("..")

    return files

