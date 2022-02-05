FROM python:3.10-alpine

WORKDIR /opt

COPY . app
RUN pip install -r app/requirements.txt

CMD ["python", "-m", "app.http"]