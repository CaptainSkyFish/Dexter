FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y libgl1 libglib2.0-0 \
    tesseract-ocr \
    libtesseract-dev \
    libleptonica-dev \
    poppler-utils \
    libxml2 \
    libpango-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    build-essential \
    libglib2.0-0 \
    libjpeg-dev \
    zlib1g-dev \
    libpng-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r dependencies.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
