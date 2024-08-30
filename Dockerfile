
FROM python:3.10-slim

COPY . .

RUN poetry install --no-dev 

CMD ['uvicorn', 'domino.app:app', '--host', '0.0.0.0', '--port', '80']
