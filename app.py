from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from firebase_utils import download_file_from_firebase
from ocr_utils import extract_text_from_pdf, extract_text_from_image
from openai_utils import summarize_text
import logging

app = FastAPI()

class ReportRequest(BaseModel):
    file_paths: List[str]

logging.basicConfig(level=logging.INFO)

@app.post("/summarize_reports")
async def summarize_reports(report_request: ReportRequest):
    summaries = []
    for file_path in report_request.file_paths:
        try:
            file_bytes = download_file_from_firebase(file_path)
            if file_path.endswith('.pdf'):
                text = extract_text_from_pdf(file_bytes)
            else:
                text = extract_text_from_image(file_bytes)
            summaries.append(summarize_text(text))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing file {file_path}: {str(e)}")

    return {"summary": "\n\n".join(summaries)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
