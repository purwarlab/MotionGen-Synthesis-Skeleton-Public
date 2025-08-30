import numpy as np
from sklearn.neighbors import KDTree
from datasetProcess import getMech, four_bar, six_bar, eight_bar
import json 
import torch
from flask import Flask, request, jsonify
from flask_cors import CORS
import os


# You should modify this function for your own synthesis method. 
def decode(path, mechTypes = []):
    solutions = [] # Saves a bunch of BSIpcs and send it back to MotionGen/frontend 

    # Example of use
    # You can put the synthesis pipeline in another script. 
    BSIpc = getMech(path, "RRRR")

    # Example point configuration: 
    # This is an RRRR mechanism 
    BSIpc['p'] = [
        [0, 0],
        [0.5, 1],
        [3, 0],
        [3.1, 1.8],
        [1.35, 3]
    ]

    solutions.append(BSIpc)

    result = {"version": "1.1.0", "solutions": solutions} 
    return result


app = Flask(__name__) 
CORS(app)

@app.route("/")
def index():
    return "Flask App now!"


@app.route("/image-based-path-synthesis", methods=["POST"])
def query():
    #print('query started')
    data = json.loads(request.data.decode("utf8").replace("'", '"'))

    knn = data["knn"] # Required number of solutions fed back to MotionGen. You don't need to feed these many back to MotionGen. 
    path = np.array(data["path"]) # input path points for path synthesis. 
    mechTypes = data.get('types') # types of mechanisms desired not implemented as Wei did not make UIs for this function 

    if len(path) == 0:
        return jsonify({"version": "1.1.0", "solutions": []})

    if any('four_bar' in tup for tup in mechTypes):
        mechTypes = set(list(mechTypes) + four_bar)
        mechTypes.remove('four_bar')
    if any('six_bar' in tup for tup in mechTypes):
        mechTypes = set(list(mechTypes) + ['Watt1', 'Watt2', 'Stephensen1', 'Stephensen2', 'Stephensen3'])
        mechTypes.remove('six_bar')
    
    result = decode(path, mechTypes)
    return jsonify(result)


if __name__ == "__main__":
    # debug: Refresh the server whenever code changes are made. 
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080))) 