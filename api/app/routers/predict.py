from fastapi import APIRouter
from pydantic import BaseModel
from ..utils.model import get_classifier_model

router = APIRouter()

class PredictOutput(BaseModel):
    genuine: bool

@router.get('/predict', response_model=PredictOutput)
def predict(variance: float, skewness: float, curtosis: float, entropy: float):
    classifier = get_classifier_model()
    features = [variance, skewness, curtosis, entropy]
    prediction = classifier.predict([features])
    genuine = prediction[0] == 1
    return PredictOutput(genuine=genuine)