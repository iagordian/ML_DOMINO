
FROM python:3.10-slim

COPY . .

RUN pip install poetry
RUN poetry lock --no-update
RUN poetry install
CMD ["poetry", 'run', "uvicorn", "domino.app:app", "--host", "0.0.0.0", "--port", "80", '--reload']