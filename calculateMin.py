import pandas as pd
import datetime

def calculateMin(df: pd.DataFrame, hoursToCharge: int) -> datetime:

    minHour: datetime = df.iloc[0]["datetime"]
    minIntensity: int = df.iloc[0:(hoursToCharge-1)]["carbonIntensity"].sum()

    for i in range(24):
        intensity: int = df.iloc[i:(hoursToCharge-1+i)]["carbonIntensity"].sum()

        if minIntensity > intensity:
            minHour = df.iloc[i]["datetime"]
            minIntensity = intensity
    
    return minHour
