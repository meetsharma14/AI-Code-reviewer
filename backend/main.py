# Import FastAPI framework
from fastapi import FastAPI
# Import Pydantic model for request validation
from pydantic import BaseModel
# Import code review function from analyzer module
from analyzer import review_code
# Create FastAPI application instance

app = FastAPI()
# Request body schema

class CodeInput(BaseModel):
    code: str
# API endpoint for code review
@app.post("/review")
def review(input_data: CodeInput):
    return review_code(input_data.code)