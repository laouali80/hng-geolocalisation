from fastapi import FastAPI
import requests

app = FastAPI()


@app.get('/api/hello')
async def test(visitor_name:str ):
    
    ipAddress = requests.get('http://api.ipify.org').text

    response = requests.get(f'http://ip-api.com/json/{ipAddress}').json()

    print(response)
    return {"client_id": ipAddress,
            "location": response["city"],
            "greeting": f"Hello, {visitor_name.title()}!"}