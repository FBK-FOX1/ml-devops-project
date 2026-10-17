from fastapi import FastAPI


app = FastAPI()

@app.post("/predict")
def predict():
    return {"predicted_price": 100}