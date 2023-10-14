import matplotlib.pyplot as plt

from calculateMin import calculateMin
from getData import getData
from createDataFrame import createDataFrame

if __name__ == "__main__":
    data = getData(endpoint="forecast")
    df = createDataFrame(data=data)

    # plt.plot(df["datetime"], df["carbonIntensity"])
    # plt.show()

    print(calculateMin(df, hoursToCharge=4))
