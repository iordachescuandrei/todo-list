FROM python:3.8-slim-buster

WORKDIR /app

COPY prereq.txt .

RUN pip3 install --no-cache-dir -r prereq.txt

COPY . .

CMD [ "python3", "app.py" ]