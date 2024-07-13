from fastapi import FastAPI
import requests
from dotenv import load_dotenv
import os
load_dotenv()


app = FastAPI()

@app.get('/')
async def welcome():
    return {"response": "succes"}

