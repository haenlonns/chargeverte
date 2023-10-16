from taipy import Gui

from getData import getData
from createDataFrame import createDataFrame
from calculateMin import calculateMinCarbon
from buildGraph import buildGraph

data = getData("forecast")
df = createDataFrame(data)

numHours = 0
chargeData = calculateMinCarbon(df, numHours)
graphData, propertyData, options = buildGraph(df, chargeData)
renderFlag = False
minTime = ""

md = """
<center><|assets/logo.png|image|></center>

<|How many hours do you need to charge for?|text|> \n

<|Hours: |text|> <|{numHours}|input|> \n

<|Calculate Optimal Time|button|on_action=buttonPressed|>

<|Ideal Charging Time: |text|> <|{minTime}|text|> \n
<|{graphData}|chart|properties={propertyData}|options={options}|>

"""

def buttonPressed(state):
    intHours = int(state.numHours)
    chargeData = calculateMinCarbon(df, intHours)
    state.minTime = chargeData["time"].strftime(f"%Y-%m-%d %I:%M %p")
    state.graphData, state.propertyData, state.options = buildGraph(df, chargeData)
    state.renderFlag = True

Gui(md).run(use_reloader=True)
