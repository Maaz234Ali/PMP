import pytesseract
from PIL import Image
import io
import fitz  # PyMuPDF

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def convert_pdf_to_images(pdf_bytes: bytes):
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    images = [Image.open(io.BytesIO(page.get_pixmap().tobytes("png"))) for page in pdf_document]
    return images

def extract_text_from_images(images):
    return "\n".join([pytesseract.image_to_string(img) for img in images])

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    images = convert_pdf_to_images(pdf_bytes)
    return extract_text_from_images(images)

def extract_text_from_image(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes))
    return pytesseract.image_to_string(image)

