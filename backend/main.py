from fastapi import FastAPI
import datetime as date
import time

# Initialize FastAPI
app = FastAPI()

# Define a simple route
@app.get("/")
async def root():
    
    time.sleep(1)
    return date.datetime.now().isoformat()