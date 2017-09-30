FROM python:3.6-slim

WORKDIR /app

RUN pip install gunicorn

COPY ./app.py ./
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--workers=4", "--bind=0.0.0.0:5000", "app:app"]

