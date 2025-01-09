# Use the latest Ubuntu image
FROM ubuntu:latest

RUN useradd -m appuser

USER appuser

USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential && \
    rm -rf /var/lib/apt/lists/*  # Clean up after installation

COPY --chown=appuser:appuser src/requirements.txt /usr/src/app/

USER appuser

RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

COPY --chown=appuser:appuser src/app.py /usr/src/app/

EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]
