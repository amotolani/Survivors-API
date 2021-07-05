FROM python:3.8-slim AS install

RUN python -m venv /opt/venv

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED 0

COPY requirements.txt .

RUN pip install -r requirements.txt

FROM python:3.8-slim AS runtime

COPY --from=install /opt/venv /opt/venv

# Make sure we use the virtualenv
ENV PATH="/opt/venv/bin:$PATH"

RUN adduser --no-create-home --uid 901 app-user

EXPOSE 8000

WORKDIR /app

COPY . .

RUN chmod -R 755 * && chmod 777 entrypoint.sh

USER app-user

ENTRYPOINT ["./entrypoint.sh"]

CMD ["init"]
