from fastapi import FastAPI
from apkMirrorScrapper import get_WhatsApp_metadata

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/whatsapp_variants")
async def WhatsApp_variants():
    return get_WhatsApp_metadata()