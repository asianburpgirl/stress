from flask import Flask,request, jsonify
from flask_cors import CORS,cross_origin
import json
import test as t
import neurokit2 as nk
import matplotlib.pyplot as plt

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
    print(data)
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

@app.route('/MeasureEcg', methods = ['GET'])
@cross_origin(origins="*")
def getECG():


    # Generate simulated ECG signal
    data = t.getEcg()
    return jsonify({
        "ECG" : list(data[0])
    })

# Start the app
if __name__ == '__main__':
    app.run(debug=True)


