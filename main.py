from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allows your website to talk to your API
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/api/predict")
def get_prediction():
    # Your unique ML-style logic placeholder
    score = random.uniform(85, 99)
    return {"probability": f"{score:.1f}%", "status": "Optimized"}

@app.get("/", response_class=HTMLResponse)
def serve_home():
    with open("index.html") as f:
        return f.read()
