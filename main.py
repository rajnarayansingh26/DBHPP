from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from utils.predictor import predict_house

app = FastAPI()

# Templates folder
templates = Jinja2Templates(directory="templates")


# ==========================
# Input Model
# ==========================
class HouseInput(BaseModel):
    area: float
    bedrooms: int
    bathrooms: int
    age: int
    location: int


# ==========================
# Home Page
# ==========================
@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# ==========================
# Prediction API
# ==========================
@app.post("/predict")
async def predict(data: HouseInput):

    features = [
        data.area,
        data.bedrooms,
        data.bathrooms,
        data.age,
        data.location
    ]

    result = predict_house(features)

    return {
        "price": result["price"],
        "source": result["source"]
    }


# ==========================
# Health Check
# ==========================
@app.get("/health")
async def health():

    return {
        "status": "running"
    }


# ==========================
# Run Server
# ==========================
if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )