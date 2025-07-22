
# Dexter OCR-to-PDF

**Dexter** is a modern, full-stack application that lets users upload pictures of printed documents, scans them using OCR(tesseract) and image processing, extracts the text and styling (highlighting, underline, strike-through), and generates a clean, downloadable PDF.

---

## Features

-  Upload images (JPG, PNG)
-  Extract text using OCR (Tesseract + OpenCV)
-  Detect highlights, underlines, basic styling
-  Generate clean, styled PDFs using WeasyPrint
-  Store raw images & generated PDFs on Azure Blob Storage
-  FastAPI backend, modern monorepo layout
-  Containerized with Docker, deployed on Azure

---

## Tech Stack

- **Backend:** FastAPI, OpenCV, Tesseract, WeasyPrint
- **Storage:** Azure Blob Storage (images + PDFs)
- **Containerization:** Docker + Docker Compose
- **Infra:** Designed for Azure Container Instances

---

## How it Works

1. **User uploads an image** — no authentication needed.
2. **Backend runs OCR** — OpenCV & Tesseract detect text + simple formatting.
3. **Text blocks + style metadata** — stored in JSON structure.
4. **WeasyPrint generates PDF** — includes styling like highlights, underline.
5. **Result PDF stored** — in Azure Blob Storage.
6. **User gets a link** — to download the generated PDF.

---

## Setup

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/dexter-ocr-pdf.git
    ```

2. Setup `.env`:
    ```
    AZURE_STORAGE_CONNECTION_STRING=your_connection_string_here
    ```

3. Build & run with Docker:
    ```bash
    docker-compose up --build
    ```

4. Access backend:
    ```
    http://localhost:8000
    ```

---

## API

**POST** `/upload`  
- `multipart/form-data` with file field.
- Returns: PDF blob ID or download URL.

**GET** `/download/{pdf_id}`  
- Returns: PDF downloadable.


---

## TODO

- Support for Word file output (.docx)
- Better styling detection (bold, italics, strike-through)
- Handwritten OCR
- User authentication & history

---

## License

MIT — free for personal and commercial use.

---

## Contributing

PRs welcome — please open an issue for any changes.

---
