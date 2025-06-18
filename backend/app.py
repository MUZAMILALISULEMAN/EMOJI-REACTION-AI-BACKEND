from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from textblob import TextBlob
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class data(BaseModel):
    txt:str

@app.post("/reaction/")
def reaction(input:data):
    analysis = TextBlob(input.txt)
    response = [analysis.polarity,analysis.subjectivity]
    return {"response":response}
