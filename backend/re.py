def calculateRecyclabilityScore(material):
    """
    Calculates the recyclability score for a material based on its category and physical properties.
    Returns a score (0-1) and an explanation dictionary.
    """
    category = material.get("category", "").lower()
    score = 1.0
    explanations = {}
    if category == "metal":
        # Magnetism helps separate ferrous from non-ferrous materials (ideal if True)
        magnetism = material.get("magnetism", "").lower()
        if magnetism == "yes":
            explanations["magnetism"] = "Easily separated magnetically (ferrous)."
        else:
            score -= 0.05  # Minor penalty for harder sorting
            explanations["magnetism"] = "Not magnetically sortable (non-ferrous)."

        # Melting point >1000°C increases energy cost
        mp = material.get("melting_point", 0)
        if mp > 1000:
            score -= 0.1
            explanations["melting_point"] = "High melting point increases energy required for recycling."
        else:
            explanations["melting_point"] = "Melting point suitable for efficient recycling."

        # Dense metals (>7 g/cm³) are heavier and costlier to transport
        density = material.get("density", 0)
        if density > 7:
            score -= 0.05
            explanations["density"] = "High density increases transportation energy."
        else:
            explanations["density"] = "Low to moderate density aids recycling logistics."

    elif category == "polymer":
        # Some polymers (PET, HDPE) are widely accepted and recyclable
        polymer_type = material.get("polymer_type", "").upper()
        if polymer_type in ["PET", "HDPE"]:
            explanations["polymer_type"] = f"{polymer_type} is widely recyclable and accepted."
        elif polymer_type in ["PVC", "PS", "OTHER"]:
            score -= 0.2
            explanations["polymer_type"] = f"{polymer_type} is not widely accepted or releases toxins."
        else:
            score -= 0.05
            explanations["polymer_type"] = f"{polymer_type} is moderately recyclable."

        # Flame retardants, dyes, etc. complicate reprocessing
        additives = material.get("additives", "").lower()
        if additives == "yes":
            score -= 0.1
            explanations["additives"] = "Contains additives that may release toxins or disrupt recycling."
        else:
            explanations["additives"] = "No significant additives, improving recycling safety."

        # Thermal stability required for remelting and reuse
        thermal_stability = material.get("thermal_stability", "").lower()
        if thermal_stability == "low":
            score -= 0.1
            explanations["thermal_stability"] = "Low thermal stability reduces reuse potential."
        else:
            explanations["thermal_stability"] = "Thermally stable and can be reused effectively."

        # High melting point polymers require more energy to recycle
        mp = material.get("melting_point", 0)
        if mp > 300:
            score -= 0.1
            explanations["melting_point"] = "High melting point slightly reduces recycling efficiency."
        else:
            explanations["melting_point"] = "Melting point is within energy-efficient recycling range."

    elif category in ["glass", "ceramic"]:
        # Glass and ceramics with very high melting points are harder to process
        mp = material.get("melting_point", 0)
        if mp > 1400:
            score -= 0.1
            explanations["melting_point"] = "Very high melting point limits reprocessing efficiency."
        else:
            explanations["melting_point"] = "Reasonable melting point for glass recycling."

        # High thermal stability is a major benefit in these materials
        thermal_stability = material.get("thermal_stability", "").lower()
        if thermal_stability == "low":
            score -= 0.1
            explanations["thermal_stability"] = "Thermal shock risk reduces recycling success."
        else:
            explanations["thermal_stability"] = "High thermal stability supports effective recycling."

    elif category == "composite":
        # Composites with additives (glues, dyes, etc.) are difficult to recycle
        additives = material.get("additives", "").lower()
        if additives == "yes":
            score -= 0.1
            explanations["additives"] = "Contains additives that complicate separation or cause emissions."
        else:
            explanations["additives"] = "Additive-free composite, slightly easier to recycle."

        # Complexity indicates how hard it is to separate layers or bonded components
        complexity = material.get("complexity", "").lower()
        if complexity == "high":
            score -= 0.2
            explanations["complexity"] = "High material complexity reduces recyclability."
        elif complexity == "medium":
            score -= 0.1
            explanations["complexity"] = "Moderate complexity may require specialized processing."
        else:
            explanations["complexity"] = "Low complexity; easier to disassemble or recycle."

    # Return both the score and the explanations for user feedback
    return {
        "score": score,
        "explanations": explanations
    }

