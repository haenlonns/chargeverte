from datetime import datetime
import taipy as ty
from taipy import Gui

from getData import getData
from createDataFrame import createDataFrame
from calculateMin import calculateMinCarbon

data = getData("forecast")
df = createDataFrame(data)

inputText = 0
start=0
end=0
numHours=0
startTime=start

minTime = calculateMinCarbon(df, numHours)

def button_pressed(state):
    state.numHours = int(state.numHours)
    state.minTime = calculateMinCarbon(df, state.numHours)
    print(state.numHours) 
    print(state.minTime)
    return state.minTime


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

"""

Gui(page).run(use_reloader=True, dark_mode=False)
