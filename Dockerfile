FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install virtualenv
RUN virtualenv venv
CMD ["source", "./venv/bin/activate"]
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./.env /code/.env
COPY ./app /code/app

CMD ["python", "-m","app"]
