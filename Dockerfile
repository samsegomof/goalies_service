FROM python:3.11-alpine

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR app/
COPY /requrements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD python ./manage.py runserver 0.0.0.0:8000

