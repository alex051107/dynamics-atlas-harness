# Digest pins a public multi-platform Python image; no local image dependency.
FROM python:3.11-slim@sha256:9534e5a8e315485d4061ed659af0fd78a284c015f9b73661b41d6bab25604534
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY reproduce /app/reproduce
COPY data /app/data
ENTRYPOINT ["python", "/app/reproduce/reproduce.py"]
CMD ["--data", "/app/data", "--output", "/output"]
