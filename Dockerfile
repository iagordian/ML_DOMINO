
FROM python:3.10-slim

COPY . .

RUN pip install uvicorn==0.20.0
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "domino.app:app"]