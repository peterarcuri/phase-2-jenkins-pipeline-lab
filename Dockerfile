FROM python:3.13-slim

WORKDIR /app

COPY app/ app/

RUN useradd -m appuser

USER appuser

CMD ["python", "app/main.py"]

