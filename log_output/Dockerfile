FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY app.py .

RUN useradd --create-home appuser
USER appuser

CMD ["python", "app.py"]
