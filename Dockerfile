
FROM python:3.10-slim

COPY . .

RUN pip install poetry
RUN poetry lock --no-update
RUN poetry install
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "domino.app:app"]