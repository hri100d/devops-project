FROM ubuntu:latest

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY src/requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY src/app.py .

EXPOSE 5000

CMD ["python3", "app.py"]
