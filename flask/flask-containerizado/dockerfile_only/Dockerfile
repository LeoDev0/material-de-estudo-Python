FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt 

COPY ./app.py /app.py

# ENTRYPOINT ["python"]
# CMD ["app.py"]

ENTRYPOINT python app.py
