FROM python:3.9
COPY . /app
EXPOSE $PORT
WORKDIR /app
RUN pip install -r requirements.txt
CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app