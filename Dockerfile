
FROM python:3.10-slim

COPY . .

ENTRYPOINT ['uvicorn', 'domino.app:app', '--host', '0.0.0.0', '--port', '80']
