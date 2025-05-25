from flask import Flask, request, jsonify
 #allows for cross-origin requests (from frontend to backend)
from flask_cors import CORS
from dataLoader import loadMaterialsData
from scoring import calculateRecyclabilityScore

materialExplanations = {
    "PVC": {
        "collection": "PVC is not widely accepted in curbside recycling programs due to its chlorine content and limited recycling demand.",
        "sorting": "Difficult to sort because it resembles other plastics visually.",
        "reprocessing": "Limited reprocessing facilities and can reease hydrochloric acid + toxic dioxins, especially when flame-retardant additives are present.",
        "material health": "Contains toxic stailizers such as lead-based compounds and phthalates."
    },
    "Aluminum": {
        "collection": "Widely accepted in curbside recycling programs due to its high value and widespread use.",
        "sorting": "Easy to sort using eddy current separators.",
        "reprocessing": "Recycling aluminum is energy-efficient and it can be recycled indefinitely without loss of quality.",
        "material health": "Generally considered safe, but concerns exist about aluminum exposure and its potential health effects."
    },
    "PET Plastic": {
        "collection": "Widely accepted in curbside recycling programs.",
        "sorting": "Easy to sort using infrared technology.",
        "reprocessing": "Recycling facilities are widely available, and PET can be recycled into new bottles or fibers. However, the process can degrade the material after multiple cycles.",
        "material health": "Low toxicity and well-studied for food-grade use, however there are concerns about the leaching of antimony and other additives."
    }
}

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
    explanations = materialExplanations.get(name,{})
    if materialInfo:
        return jsonify({"properties":materialInfo, "explanations":explanations})
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

    return jsonify({"score": scoreResult})

if __name__ == '__main__':
    app.run(debug=True)