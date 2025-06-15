from flask import Flask, request, jsonify
 #allows for cross-origin requests (from frontend to backend)
from flask_cors import CORS
from dataLoader import loadMaterialsData
from scoreCalculator import calculateRecyclabilityScore

#initialize Flask application 
app = Flask(__name__)
#Enable CORS 
CORS(app)

#load materials dataset and store in dictionary
MaterialsData = loadMaterialsData()

#define endpoint to return list of all available materials
@app.route('/materials', methods=['GET'])
def getAllMaterials():
    #Returns a list of materials
    return jsonify(list(MaterialsData.keys()))

@app.route('/materials/<name>', methods=['GET'])
def getMaterial(name):
    materialInfo = MaterialsData.get(name)
    if materialInfo:
        return jsonify({"properties":materialInfo})
    else:
        #return error if material is not found
        return jsonify({"error": "Material not found"}), 404
    
#define endpoint to calculate recyclability score based on input properties
@app.route('/score', methods = ['POST'])
def getRecyclabilityScore():
    #extract JSON data from user
    requestData = request.get_json()
    #calculate score 
    scoreResult = calculateRecyclabilityScore(requestData)

    return jsonify({
        "score": scoreResult["score"],
        "explanations": scoreResult["explanations"]
    })
if __name__ == '__main__':
    app.run(debug=True)