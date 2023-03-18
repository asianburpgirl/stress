from flask import request, jsonify
from flask_cors import CORS,cross_origin
from __main__ import app


@app.route('/saveResponse')
@cross_origin(origin='*',headers=['content-type'])
def saveResponse():
    return "Saved"
