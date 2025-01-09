
FROM ubuntu:latest

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    && python3 -m venv /usr/src/app/venv \
    && /usr/src/app/venv/bin/pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/src/app/venv/bin:$PATH"

RUN useradd -m appuser && chown -R appuser /usr/src/app
USER appuser

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/app.py .

EXPOSE 5000

CMD ["python3", "app.py"]
