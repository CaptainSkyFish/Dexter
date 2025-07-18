# Dexter - image to pdf solution

User's browser
   |
   | uploads image → Blob Storage (Container: input-images)
   |
   | gets back an `image_id`
   |
   | calls your FastAPI backend with `image_id`
   |
   | backend fetches blob → runs OCR → creates PDF → uploads PDF to Blob Storage (Container: output-pdfs)
   |
   | backend returns `pdf_id` → frontend gets download link.
