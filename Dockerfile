FROM python:3.8.0a3

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python3", "app.py"]