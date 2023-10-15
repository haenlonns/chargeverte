import pandas as pd

def buildGraph(df: pd.DataFrame, graphDetails: dict) -> dict:

    carbonData = df.iloc[0:34]
    chargePeriod = [100 if graphDetails["index"] <= i <= (graphDetails["index"] + graphDetails["duration"] - 1) else None for i in range(34)]

    graphData: dict = {
        "Date & Time": carbonData["datetime"].dt.strftime(f"%Y-%m-%d %H:%M:%S"),
        "Carbon Intensity": carbonData["carbonIntensity"],
        "Charge Period": chargePeriod
    }

    propertyData: dict = {
        "type": "line",
        "x": "Date & Time",
        "y[1]": "Carbon Intensity",
        "y[2]": "Charge Period",
        "color[1]": "red",
        "color[2]": "green"
    }

    options: dict = {
        "fill": "tozeroy"
    }

    return [graphData, propertyData, options]
