FROM python:3.7.2-stretch

RUN pip install --upgrade pip

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 3050

CMD ["python", "run.py"]
