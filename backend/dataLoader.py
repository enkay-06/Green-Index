import pandas as pd

def loadMaterialsData():
    #load csv file using pandas
    dataframe = pd.read_csv('/Users/NertigaK/Documents/Recyclability-Project/backend/data/materialsData.csv')

    #convert dataframe to dictionary of dictionaries and sets the Material column as the index
    materialsDict = dataframe.set_index("Material").to_dict(orient="index")
    return materialsDict

