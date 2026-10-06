from typing import Dict, Any

def calculate_forensic_score(analysis_results: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate a forensic risk score based on various analysis results
    
    Args:
        analysis_results: Dictionary containing results from various forensic analyses
        
    Returns:
        Dictionary containing the score and risk level
    """
    score = 0
    max_score = 100
    factors = []
    
    # Metadata anomalies (0-15 points)
    metadata_score = 0
    if analysis_results.get("metadata", {}).get("editing_software_detected"):
        metadata_score += len(analysis_results["metadata"]["editing_software_detected"]) * 5
    if not analysis_results.get("metadata", {}).get("metadata_complete", True):
        metadata_score += 5
    metadata_score = min(metadata_score, 15)
    score += metadata_score
    if metadata_score > 0:
        factors.append(("Metadata anomalies", metadata_score, 15))
    
    # File integrity (0-10 points) - usually 0 if we're analyzing the stored file
    integrity_score = 0
    # In a real system, we might check for signs of file tampering
    score += integrity_score
    if integrity_score > 0:
        factors.append(("File integrity anomalies", integrity_score, 10))
    
    # ELA indicators (0-20 points)
    ela_score = 0
    ela_result = analysis_results.get("ela", {})
    if ela_result.get("has_significant_anomalies"):
        # Scale based on intensity
        intensity = ela_result.get("max_intensity", 0)
        ela_score = min(int(intensity / 10), 20)  # Scale 0-200 intensity to 0-20 points
    score += ela_score
    if ela_score > 0:
        factors.append(("ELA indicators", ela_score, 20))
    
    # Noise anomalies (0-15 points)
    noise_score = 0
    noise_result = analysis_results.get("noise", {})
    if noise_result.get("has_significant_anomalies"):
        noise_score = 15
    score += noise_score
    if noise_score > 0:
        factors.append(("Noise anomalies", noise_score, 15))
    
    # JPEG analysis (0-10 points) - placeholder
    jpeg_score = 0
    score += jpeg_score
    if jpeg_score > 0:
        factors.append(("JPEG analysis anomalies", jpeg_score, 10))
    
    # Frequency analysis (0-10 points) - placeholder
    freq_score = 0
    score += freq_score
    if freq_score > 0:
        factors.append(("Frequency analysis anomalies", freq_score, 10))
    
    # Copy-move indicators (0-20 points)
    copymove_score = 0
    copymove_result = analysis_results.get("copy_move", {})
    if copymove_result.get("has_significant_matches"):
        match_count = copymove_result.get("matches_found", 0)
        copymove_score = min(match_count, 20)  # Cap at 20 points
    score += copymove_score
    if copymove_score > 0:
        factors.append(("Copy-move indicators", copymove_score, 20))
    
    # Provenance signals (-10 to +10 points) - negative if provenance found (good), positive if not found (concerning)
    prov_score = 0
    prov_result = analysis_results.get("provenance", {})
    if not prov_result.get("provenance_found", False):
        prov_score = 10  # Slightly concerning if no provenance
    else:
        prov_score = -5  # Good sign if provenance found
    score = max(0, min(score + prov_score, max_score))  # Keep score in bounds
    if prov_score != 0:
        factors.append(("Provenance signals", prov_score, 10, prov_score < 0))  # Negative is good
    
    # AI-assisted result (0-20 points)
    ai_score = 0
    ai_result = analysis_results.get("ai", {})
    if ai_result.get("available", False):
        confidence = ai_result.get("confidence", 0)
        ai_score = int(confidence * 20)  # Scale 0-1 confidence to 0-20 points
    score += ai_score
    if ai_score > 0:
        factors.append(("AI-assisted result", ai_score, 20))
    
    # Ensure score is within bounds
    score = max(0, min(score, max_score))
    
    # Determine risk level
    if score <= 24:
        risk_level = "LOW"
    elif score <= 49:
        risk_level = "MODERATE"
    elif score <= 74:
        risk_level = "HIGH"
    else:
        risk_level = "CRITICAL"
    
    return {
        "score": score,
        "max_score": max_score,
        "risk_level": risk_level,
        "factors": factors,
        "interpretation": get_score_interpretation(score, risk_level)
    }

def get_score_interpretation(score: int, risk_level: str) -> str:
    """
    Get interpretation of the forensic score
    
    Args:
        score: The calculated score (0-100)
        risk_level: The risk level string
        
    Returns:
        Interpretation string
    """
    interpretations = {
        "LOW": (
            "This score indicates low investigative interest. "
            "Few or no significant anomalies were detected across the analyses performed. "
            "This does not guarantee authenticity but suggests the image appears consistent."
        ),
        "MODERATE": (
            "This score indicates moderate investigative interest. "
            "Some anomalies were detected that warrant closer examination. "
            "These findings should be considered alongside other evidence and investigative context."
        ),
        "HIGH": (
            "This score indicates high investigative interest. "
            "Multiple or significant anomalies were detected across several analysis types. "
            "Further investigation is recommended before drawing conclusions."
        ),
        "CRITICAL": (
            "This score indicates critical investigative interest. "
            "Substantial anomalies were detected across multiple analysis types. "
            "The image shows multiple indicators that may suggest manipulation, "
            "but forensic analysis alone cannot definitively prove authenticity."
        )
    }
    
    return interpretations.get(risk_level, "Unable to interpret score.")
