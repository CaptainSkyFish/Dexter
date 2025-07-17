import cv2
import numpy as np
import pytesseract


def run_ocr(image_bytes: bytes) -> list[dict]:
    """
    Runs OCR on an image file (bytes) and returns extracted text.
    """
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Image decoding failed! - Invalid image.")

    ocr_data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    blocks = []
    current_block = {"type": "paragraph", "content": []}

    for i in range(len(ocr_data["text"])):
        word = ocr_data["text"][i]
        if not word.strip():
            continue
        x, y, w, h = (
            ocr_data["left"][i],
            ocr_data["top"][i],
            ocr_data["width"][i],
            ocr_data["height"][i],
        )
        roi = img[y : y + h, x : x + w]
        avg_color = cv2.mean(roi)[:3]

        highlight = avg_color[1] > 150 and avg_color[0] < 150 and avg_color[2] < 150

        line_roi = gray[y + h : y + h + 5, x : x + w]
        underline = cv2.countNonZero(line_roi < 50) > 0.2 * line_roi.size

        # todo: add logic to check for bold and strike and different types and colors of highlights/underlines
        current_block["content"].append(
            {
                "text": word,
                "bold": False,
                "underline": bool(underline),
                "highlight": bool(highlight),
                "strike": False,
            }
        )

        blocks.append(current_block)
    return blocks
