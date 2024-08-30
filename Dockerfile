
FROM python:3.10-slim

COPY . .

RUN poetry install --no-dev 

