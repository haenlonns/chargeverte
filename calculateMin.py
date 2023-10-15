import pandas as pd
from datetime import datetime

def calculateMinCarbon(df: pd.DataFrame, hoursToCharge: int) -> dict:

    minHour: datetime = df.iloc[0]["datetime"]
    minIntensity: int = df.iloc[0:(hoursToCharge-1)]["carbonIntensity"].sum()
    minIndex: int = 0

    for i in range(24):
        intensity: int = df.iloc[i:(hoursToCharge-1+i)]["carbonIntensity"].sum()

        if minIntensity > intensity:
            minHour = df.iloc[i]["datetime"]
            minIntensity = intensity
            minIndex = i
    
    endTime: datetime = df.iloc[minIndex+hoursToCharge-1]["datetime"]
    
    data: dict = {
        "index": minIndex,
        "duration": hoursToCharge,
        "time": minHour,
        "endTime": endTime,
        "intensity": minIntensity
    }

    return data
