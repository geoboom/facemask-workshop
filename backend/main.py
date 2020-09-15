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


# TODO: initialize our Detector object


@app.post("/detect", response_model=DetectionsData)
async def detect_face_mask(file: UploadFile = File(...)):
    try:
        # read and predict facemask on uploaded frame
        contents = await file.read()
        pil_image = Image.open(io.BytesIO(contents))

        # TODO: predict using the detector and get the latest logs

        return {
            "results": [{ "wearing_mask": False, "confidence": 1.0, "coords": [] }],
            "detection_log_updated": True,
            "logs": [],
        }

    except Exception as e:
        print(f"POST /detect error: {e}")
        raise HTTPException(status_code=500, detail="Detection failed.")


@app.get("/detection_log", response_model=typing.List[typing.Any])
async def get_detection_log():
    os.chdir("detection_log")
    files = sorted(
        filter(os.path.isfile, os.listdir(".")), key=os.path.getmtime, reverse=True
    )
    os.chdir("..")

    return files

