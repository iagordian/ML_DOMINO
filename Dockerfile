
FROM python:3.10-slim

COPY . .

RUN pip install --upgrade pip==22.1.0
RUN pip3 install --upgrade setuptools
RUN pip install python-dotenv
RUN cat requarements.txt | xargs -n 1 pip install
RUN pip install uvicorn==0.20.0
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "domino.app:app"]