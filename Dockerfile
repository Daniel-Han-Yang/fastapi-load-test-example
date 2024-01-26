FROM python:3.11-slim-bookworm

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY async_max_1_process.py /app/async_fast_1.py
COPY async.py /app/async_fast.py
COPY sync.py /app/sync_fast.py



