# Hot reloading don't work for development
# FROM python:3.9 

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9


WORKDIR /code


COPY ./requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY ./app /code/app


# CMD ["uvicorn", "app.main:app", "--reload"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
