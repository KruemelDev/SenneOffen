FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src/main/ ./

CMD [ "gunicorn", "--bind", "0.0.0.0:80", "wsgi:app"]
