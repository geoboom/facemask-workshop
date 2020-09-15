# Facemask Detector (backend)

The backend of le Facemask Detection project

TODO: add in `sudo apt update && sudo apt upgrade`

## Installation
1. make sure you have `python3` installed
2. clone this repo into your directory of choice by running `git clone https://github.com/geoboom/facemask-detector-backend.git`
3. `cd facemask-detector-backend`
4. run `python3 -m venv venv` create the venv
4. run `source venv/bin/activate` to load the venv
5. run `pip install -r requirements.txt` to install the `pip` packages
6. run `uvicorn main:app --reload` to load the pip venv and spin up the fastapi server. Alternatively, you could run `./run.sh` which does this for you.
