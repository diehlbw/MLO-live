from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

from log_config import get_logger

logger = get_logger("my-project-logger")
app = FastAPI()

class PredictionRequest(BaseModel):
  query_string: str

@app.get('/health')
async def root():
    logger.info("Health was queried")
    return {'message': "App is running"}

@app.post('/analyze')
def analyze(request: PredictionRequest):
    sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    response = {'query':request.query_string}
    try:
        model_out = sentiment_model(response['query'])[0]
        #Force error
        #raise ValueError("Could not understand comment")
    except BaseException as e: # Catch everything
        err_str = f"Model analysis failed ({type(e).__name__}): {str(e)}"
        logger.error(err_str)
        raise HTTPException(status_code=500, detail=err_str)

    response.update(**model_out)

    logger.info(f"Analyzed => {response['label'].lower()}")
    return response


##############
# Error overrides

from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.error(f"{request['path']} Invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)