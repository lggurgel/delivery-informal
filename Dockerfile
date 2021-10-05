FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app/
RUN mkdir /app
RUN apt update -y

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app.py"]