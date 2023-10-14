from flask import Flask
from flask_cors import CORS
from datetime import datetime

from getData import getData
from createDataFrame import createDataFrame
from calculateMin import calculateMinCarbon

app = Flask(__name__)
CORS(app)

@app.route("/api/forecast")
def push_data():
    data = getData("forecast")
    return data

@app.route("/api/mincarboncharge/<int:hours>")
def push_co2_charge(hours):
    data = getData("forecast")
    df = createDataFrame(data)
    chargetime = calculateMinCarbon(df, hours)
    return { "data": chargetime.strftime("%I:%M%p - %m/%d/%Y") }
    
if __name__ == '__main__':
    app.run(debug=True)
