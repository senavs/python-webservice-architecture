FROM python:3.10-alpine

WORKDIR /opt

COPY . api
RUN pip install -r api/requirements.txt

CMD ["python", "-m", "api"]