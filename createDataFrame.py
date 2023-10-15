import pandas as pd

def createDataFrame(data: list) -> pd.DataFrame:

    df = pd.DataFrame(data, columns=["datetime", "carbonIntensity"])
    df['datetime'] = pd.to_datetime(df["datetime"])
    df['datetime'] = df['datetime'].dt.tz_convert("Canada/Eastern")

    return df
