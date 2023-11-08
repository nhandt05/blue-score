FROM python:3.9.16
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install fastapi uvicorn python-multipart sacrebleu
CMD ["python3", "translate_api.py"]