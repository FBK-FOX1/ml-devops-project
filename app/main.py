from fastapi import FastAPI
from pydantic import BaseModel


class HouseFeatures(BaseModel):
    area: float
    bedrooms: int


app = FastAPI()


@app.post("/predict")
def predict(features: HouseFeatures):
    return {"predicted_price": 100}