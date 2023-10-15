from calculateMin import calculateMinCarbon
from getData import getData
from createDataFrame import createDataFrame

if __name__ == "__main__":
    data = getData(endpoint="forecast")
    df = createDataFrame(data=data)

    print({ "data": calculateMinCarbon(df, hoursToCharge=4) })
