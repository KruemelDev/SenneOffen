FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src/main/fetchOpenTimes.py fetchOpenTimes.py

CMD [ "python", "fetchOpenTimes.py"]
