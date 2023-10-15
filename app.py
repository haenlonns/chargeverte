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

<center>
<|navbar|lov={[("page", "ChargeVerte")]}|>
</center>

What interval do you want to charge during? (Enter times as 24-hour: ex. 6:30 is 1830)\n
Start: <|{start}|input|> \n
End: <|{end}|input|> \n
How many hours do you need to charge for? \n
Hours: <|{numHours}|input|> \n

<|Calculate Optimal Time|button|on_action=button_pressed|>


<|{minTime}|>


<|{minTime}|text|>
<|{graphData}|chart|properties={propertyData}|options={options}|>

"""

Gui(page).run(use_reloader=True, dark_mode=False)
