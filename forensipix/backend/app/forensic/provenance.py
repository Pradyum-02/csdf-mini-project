from PIL import Image
import json
from typing import Dict, Any
import os

def check_provenance(image_path: str) -> Dict[str, Any]:
    """
    Check for C2PA/provenance metadata in an image
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary containing provenance analysis results
    """
    try:
        image = Image.open(image_path)
        
        # Check for common provenance/XMP markers in EXIF
        exif_data = {}
        if hasattr(image, '_getexif') and image._getexif() is not None:
            exif = image._getexif()
            for tag_id, value in exif.items():
                exif_data[tag_id] = value
        
        # Look for common provenance indicators
        provenance_found = False
        provenance_data = {}
        
        # Check for XMP-like data in common EXIF tags
        xmp_related_tags = [700, 701, 702, 703]  # Common XMP tags
        for tag in xmp_related_tags:
            if tag in exif_data:
                provenance_found = True
                provenance_data[f"xmp_tag_{tag}"] = str(exif_data[tag])[:200]  # Limit length
        
        # Check for Photoshop-specific metadata that might indicate editing
        software = exif_data.get(305, "")  # Software tag
        if isinstance(software, bytes):
            software = software.decode('utf-8', errors='ignore')
        
        editing_indicators = ["adobe photoshop", "adobe illustrator", "corel", "gimp", "sketch"]
        is_edited = any(indicator in software.lower() for indicator in editing_indicators) if software else False
        
        if is_edited:
            provenance_found = True
            provenance_data["software_indicator"] = software
        
        return {
            "provenance_found": provenance_found,
            "provenance_data": provenance_data,
            "software_info": software if software else "Not available",
            "interpretation": "Provenance metadata detected, which may indicate the image originates from a known source or has been processed by known software." if provenance_found
                            else "No C2PA/provenance metadata detected. This does NOT mean the image is manipulated.",
            "limitation": "This implementation checks for basic metadata indicators. "
                         "Full C2PA validation requires specialized libraries."
        }
    except Exception as e:
        return {
            "error": f"Provenance analysis failed: {str(e)}",
            "provenance_found": False,
            "provenance_data": {},
            "software_info": "Analysis failed",
            "interpretation": "Analysis could not be completed.",
            "limitation": "Analysis could not be completed due to an error."
        }
