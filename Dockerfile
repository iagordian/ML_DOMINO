
FROM python:3.10-slim

COPY . .

CMD python3 -m uvicorn app.main:app --host 0.0.0.0 --port 80
