FROM python:3.10-slim-buster

WORKDIR /app
COPY . .

RUN pip install --upgrade pip \
            && pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

CMD ["python", "server.py"]
