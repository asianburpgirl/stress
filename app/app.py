from flask import Flask,request, jsonify
from flask_cors import CORS,cross_origin
import json
import test as t
import neurokit2 as nk
import matplotlib.pyplot as plt
import joblib
import pandas as pd
import datetime

app = Flask(__name__)

from response import *


@app.route('/',methods = ['GET'])
@cross_origin(origin='*',headers=['content-type'])
def Hellowolrd():
    return "Hello World"

@app.route('/',methods = ['POST'])
@cross_origin(origin='*',headers=['content-type'])
def ByeWorld():
    data = request.data
    print(data)
    return "Data Received!"

@app.route('/saveresponse',methods = ['POST'])
@cross_origin(origin='*',headers=['content-type'])
def saveToFile():
    data = request.get_json()
# Convert JSON data to a string
    #json_str = json.dumps(data)

    # Write JSON string to a file
    #print(data)
    with open('data.json', 'w') as f:
        f.write(json.dumps(data))
    return "Response Saved"

@app.route('/response',methods = ['GET'])
@cross_origin(origin='*')
def getResponse():
    data = "No Response"
    with open('data.json', 'r') as f:
    # Load the contents of the file into a dictionary
        data = json.load(f)
    return data

@app.route('/alldata',methods = ['GET'])
@cross_origin(origin='*')
def getAllData():
    data = "No Response"
    with open('userdata.json', 'r') as f:
    # Load the contents of the file into a dictionary
        data = json.load(f)
    return jsonify(data)

@app.route('/newData', methods = ['GET'])
@cross_origin(origins="*")
def getECG():

    HRdata = t.ecg2()
    SDNN = HRdata[0]
    HR = HRdata[1]
    print(SDNN)
    filename = 'decision_tree_model.sav'
    loaded_model = joblib.load(filename)
    new_data = pd.DataFrame({'Gener': [1], 'SNDD': [SDNN], 'Age': [25]})
    prediction = loaded_model.predict(new_data)
    prediction = int(prediction[0])
    data = {
        "Date" : datetime.datetime.today().strftime('%d/%m/%Y'),
        "SDNN" : SDNN,
        "HR" : HR,
        "Stress" : prediction
    }
    with open('userdata.json', 'r') as f:
    # Load the contents of the file into a dictionary
        userdata = json.load(f)
    #userdata = userdata["Data"]
    userdata.append(data)
    with open('userdata.json', 'w') as f:
        json.dump(userdata, f)
    return data

# Start the app
if __name__ == '__main__':
    app.run(debug=True)


