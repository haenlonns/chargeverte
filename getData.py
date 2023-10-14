import requests
import dotenv
import os

def getData(endpoint: str) -> list:
    dotenv.load_dotenv()

    url = "https://api-access.electricitymaps.com/2w97h07rvxvuaa1g/carbon-intensity/" + endpoint
    headers = { "auth-token": os.environ["API_TOKEN"] }
    params = { "zone": "CA-ON" }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()[endpoint]

    return data
