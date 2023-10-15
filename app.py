from datetime import datetime
import taipy as ty
from taipy import Gui

from getData import getData
from createDataFrame import createDataFrame
from calculateMin import calculateMinCarbon

data = getData("forecast")
df = createDataFrame(data)
minTime = calculateMinCarbon(df, 4)

text = minTime
inputText = 0

page = """
# Getting started with Taipy GUI

Ideal Charge Time: <|{text}|>

<|{inputText}|input|>
"""

Gui(page).run()
