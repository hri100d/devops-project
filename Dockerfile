FROM ubuntu:latest

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /usr/src/app/venv

RUN /usr/src/app/venv/bin/pip install --upgrade pip

ENV PATH="/usr/src/app/venv/bin:$PATH"

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/app.py .

EXPOSE 5000

CMD ["python3", "app.py"]
