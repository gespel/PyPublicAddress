FROM python:3.9

WORKDIR /code

EXPOSE 80

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app

CMD ["fastapi", "run", "app/render_server.py", "--port", "80"]