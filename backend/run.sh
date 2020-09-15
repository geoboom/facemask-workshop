. venv/bin/activate
gunicorn main:app -k uvicorn.workers.UvicornWorker --reload
