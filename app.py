from taipy import Gui

from getData import getData
from createDataFrame import createDataFrame
from calculateMin import calculateMinCarbon
from buildGraph import buildGraph

data = getData("forecast")
df = createDataFrame(data)

chargeData = calculateMinCarbon(df, 2)
graphData, propertyData, options = buildGraph(df, chargeData)

minTime = chargeData["time"].strftime(f"%Y-%m-%d %I:%M %p")

page = """

<|{minTime}|text|>
<|{graphData}|chart|properties={propertyData}|options={options}|>

"""
Gui(page).run()
