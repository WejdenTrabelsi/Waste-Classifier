"""
FastAPI backend for the waste classifier.

Endpoint:
    POST /predict  -> upload an image, get back predicted class,
                       confidence, and recommended Nielsen equipment.

Run:
    uvicorn app:app --reload
"""

from pathlib import Path
from fastai.vision.all import load_learner, PILImage
from fastapi import FastAPI, UploadFile, File
import io

from recommendations import get_recommendation

app = FastAPI(title="Nielsen Waste Classifier API")

MODEL_PATH = Path("model/waste_classifier.pkl")
learn = load_learner(MODEL_PATH)


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img = PILImage.create(io.BytesIO(image_bytes))

    pred_class, pred_idx, probs = learn.predict(img)
    confidence = float(probs[pred_idx])

    return {
        "predicted_class": str(pred_class),
        "confidence": round(confidence, 4),
        "recommendation": get_recommendation(str(pred_class)),
    }
