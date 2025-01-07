from firebase_admin import credentials, storage, initialize_app
from datetime import timedelta
import requests
from fastapi import HTTPException

# Initialize Firebase Admin SDK
cred = credentials.Certificate("FIREBASE_KEY_JSON")
initialize_app(cred, {'storageBucket': 'login-cb7d4.appspot.com'})

def generate_signed_url(file_path: str) -> str:
    bucket = storage.bucket()
    blob = bucket.blob(file_path)
    return blob.generate_signed_url(timedelta(minutes=15))

def download_file_from_firebase(file_path: str) -> bytes:
    url = generate_signed_url(file_path)
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to download file from Firebase.")
    return response.content

