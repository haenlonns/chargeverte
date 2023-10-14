import requests
import pandas as pd
import matplotlib.pyplot as plt
import dotenv
import os

url = "https://api-access.electricitymaps.com/2w97h07rvxvuaa1g/carbon-intensity/history"

dotenv.load_dotenv()
headers = {
    "auth-token": os.environ["API_TOKEN"]
}

params = {
    "zone": "CA-ON"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()["history"]

df = pd.DataFrame(data, columns=["datetime", "carbonIntensity"])
df['datetime'] = pd.to_datetime(df['datetime'])

plt.plot(df["datetime"], df["carbonIntensity"])
plt.show()

print(df)
