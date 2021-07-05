FROM python:3.8-slim

RUN pip install jinja2

WORKDIR /app

RUN mkdir -p /tmp/out

COPY . .

CMD ["python", "templates.py"]
