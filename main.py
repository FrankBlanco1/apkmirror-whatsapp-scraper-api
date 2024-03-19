from fastapi import FastAPI
from apkMirrorScrapper import get_WhatsApp_metadata
from fastapi_utils.tasks import repeat_every
from contextlib import asynccontextmanager
import json

# Execute on startup (see lifespan) and every 24 hours
@repeat_every(seconds=60 * 60 * 24) 
async def get_apkmirror_data():
    
    try:
        data = get_WhatsApp_metadata()
        
        # Save the data in a cached json file
        json_data = json.dumps(data, indent = 3)
        
        with open("cached_data.json", "w") as file:
            file.write(json_data)
        
        
    except Exception as e:
        
        # Notif the error ocurred while scraping the cached data will not be modified
        pass
    
@asynccontextmanager
async def lifespan(app : FastAPI):
    await get_apkmirror_data()
    yield
    
app = FastAPI(lifespan=lifespan)
    
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/whatsapp_variants")
async def WhatsApp_variants():
    
    # Return the cahced data, this data will be update every day
    
    with open('cached_data.json', 'r') as file:
        json_data = json.load(file)
        
    return json_data