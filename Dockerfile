FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN pip install poetry==1.0.0
RUN mkdir /code
COPY poetry.lock /code/
COPY pyproject.toml /code/
COPY song_translator /code/song_translator

WORKDIR /code
RUN poetry install
