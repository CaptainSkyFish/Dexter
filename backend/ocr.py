import cv2
import numpy as np
import pytesseract

def run_ocr(image_bytes: bytes) -> str:
    """
    Runs OCR on an image file (bytes) and returns extracted text.
    """
    # Convert bytes to OpenCV image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Preprocess: grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # You can add more preprocessing here if needed:
    # e.g., thresholding, denoising

    # Run Tesseract
    text = pytesseract.image_to_string(gray)

    return text
