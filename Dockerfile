FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN pip install poetry==1.0.0
RUN mkdir /code
ADD poetry.lock /code/
ADD pyproject.toml /code/
ADD song_translator /code/song_translator

WORKDIR /code
RUN poetry install
ADD song_translator /code/
