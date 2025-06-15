def calculateAdditionalPenalties (materialProperties):
    """Applies penalties based on physical properties of the material"""
    penalty = 0
    # Penalize for high melting point (> 1000C)
    meltingPoint = materialProperties.get('meltingPoint',0)
    if meltingPoint > 1000:
        penalty += 0.1

    # Penalize for high density (> 7 g/cm^3)
    density = materialProperties.get('density', 0)
    if density > 7:
        penalty += 0.1

    # Penalize if toxicity is labeled as High
    toxicity = materialProperties.get('toxicity', '').lower()
    if toxicity == 'high':
        penalty += 0.2
    
    return penalty

def calculateRecyclabilityScore(materialProperties):
    """"Takes a dictionary of properties for a material and 
    returns a recyclability score. 
    
    Collection: how likely it is that the material is collected through curbside or depot recycling programs. 1 is widely accepted, <0.5 is rarely accepted or only in industrial settings
    Sorting: how easily the material can be sorted at a material recovery facility. 1 is easy to sort, <0.5 is difficult to sort/hard to distinguish
    Reprocessing: how easily the material can be sorted at a material recovery facility. 1 is widely recycled (aluminum,PET), <0.5 is not recycled due to lack of facilities, etc
    Material Health: how safe and non-toxic the material is during its lifecycle, including when it is recycled. 1 means stable/non-toxic, <0.5 means it releases harmful substances (PVC, flame retardants) 
    """
    recyclabilityFactors = {'collection': 0.3, 'sorting': 0.25, 'reprocessing': 0.25, 'materialHealth': 0.2}
    totalScore = 0
    for criterion, weight in recyclabilityFactors.items():
        #Defaults to 0 if missing
        propertyValue = materialProperties.get(criterion, 0)
        totalScore += propertyValue * weight
    # Apply penalties based on physical properties
    totalPenalty = calculateAdditionalPenalties(materialProperties)
    finalScore = totalScore - totalPenalty

    return max(0,round(finalScore, 2))  # Ensure score is non-negative and rounded to 2 decimal places