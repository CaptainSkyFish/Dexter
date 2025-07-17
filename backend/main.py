from fastapi import FastAPI, UploadFile, File, Query
from fastapi.responses import JSONResponse, Response
from blob_utils import upload_file, download_file
from pdf_utils import create_pdf_from_blocks
from ocr import run_ocr
import uuid
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Dexter is live!"}


@app.post("/upload")
async def upload_image(
    file: UploadFile = File(...),
    styled: bool = Query(True, description="Include pdf styling."),
):
    img_id = str(uuid.uuid4()) + ".jpg"

    contents = await file.read()
    upload_file("input-images", img_id, contents)

    img_bytes = download_file("input-images", img_id)
    extracted_blocks = run_ocr(img_bytes)

    pdf_id = str(uuid.uuid4()) + ".pdf"
    output_path = f"/tmp/{pdf_id}"

    create_pdf_from_blocks(extracted_blocks, output_path, styled=styled)

    with open(output_path, "rb") as f:
        upload_file("output-pdfs", pdf_id, f.read())

    os.remove(output_path)

    return JSONResponse({"pdf_id": pdf_id})


@app.get("/download/{pdf_id}")
def download_pdf(pdf_id: str):
    pdf_bytes = download_file("output-pdfs", pdf_id)
    return Response(pdf_bytes, media_type="application/pdf")
