from fastapi import FastAPI
import requests
from dotenv import load_dotenv
import os
load_dotenv()


app = FastAPI()


@app.get('/api/hello')
async def test(visitor_name: str = "Mark"):
    
    ipAddress = requests.get('http://api.ipify.org').text

    response = requests.get(f'http://ip-api.com/json/{ipAddress}').json()
    
    temp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={response['lat']}&lon={response['lon']}&units=Metric&appid={os.getenv("api_key")}").json()

    return {"client_id": ipAddress,
            "location": response["city"],
            "greeting": f"Hello, {visitor_name.title()}!",
            "Temperature": f"{temp["main"]["temp"]} °C"
            }
