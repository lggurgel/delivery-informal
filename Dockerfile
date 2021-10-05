FROM python:3.9-alpine

RUN addgroup app && adduser -S -G app app
USER app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app.py"]