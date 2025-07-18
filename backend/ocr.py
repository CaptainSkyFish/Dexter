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

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
        if roi is not None and roi.size > 0 and len(roi.shape) >= 2:
            if len(roi.shape) == 2:
                roi = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)
            mean_result = cv2.mean(roi)
            if isinstance(mean_result, tuple):
                avg_color = mean_result[:3]
            else:
                avg_color = (0, 0, 0)
        else:
            avg_color = (0, 0, 0)
        # Heuristic: detect yellowish highlight (strong green, low blue/red)
        highlight = avg_color[1] > 150 and avg_color[0] < 150 and avg_color[2] < 150

        # Underline check: look for dark line below the word box
        line_roi = gray[y + h : y + h + 5, x : x + w]
        if line_roi.size > 0:
            # Count dark pixels (thresholded)
            _, bin_line = cv2.threshold(line_roi, 50, 255, cv2.THRESH_BINARY_INV)
            underline = cv2.countNonZero(bin_line) > 0.2 * line_roi.size
        else:
            underline = False
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
