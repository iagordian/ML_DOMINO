
FROM python:3.10-slim

COPY . .

CMD uvicorn app.main:app --host 0.0.0.0 --port 80
