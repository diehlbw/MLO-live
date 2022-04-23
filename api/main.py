from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class PredictionRequest(BaseModel):
  query_string: str

@app.get("/health")
async def root():
    return {"message": "This is live"}

@app.post("/analyze")
def analyze(request: PredictionRequest):
    sentiment_model = pipeline("sentiment-analysis")

    sentiment_query_sentence = request.query_string
    sentiment = sentiment_model(sentiment_query_sentence)
    print(f"Sentiment test: {sentiment_query_sentence} == {sentiment}")
