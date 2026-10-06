from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import json
from typing import Dict, Any, Optional
import os

def get_exif_data(image_path: str) -> Dict[str, Any]:
    """
    Extract EXIF data from an image
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary containing EXIF data
    """
    try:
        image = Image.open(image_path)
        exif_data = {}
        
        if hasattr(image, '_getexif') and image._getexif() is not None:
            exif = image._getexif()
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                exif_data[tag] = value
        
        return exif_data
    except Exception as e:
        return {"error": f"Could not extract EXIF data: {str(e)}"}

def get_gps_info(exif_data: Dict[str, Any]) -> Optional[Dict[str, float]]:
    """
    Extract GPS information from EXIF data
    
    Args:
        exif_data: EXIF data dictionary
        
    Returns:
        Dictionary with latitude, longitude, and altitude or None
    """
    try:
        gps_info = {}
        if "GPSInfo" in exif_data:
            gps_data = exif_data["GPSInfo"]
            
            # Extract latitude
            if 1 in gps_data and 2 in gps_data:
                lat_ref = gps_data[1]
                lat_degrees = gps_data[2]
                latitude = convert_to_degrees(lat_degrees)
                if lat_ref != "N":
                    latitude = -latitude
                gps_info["latitude"] = latitude
            
            # Extract longitude
            if 3 in gps_data and 4 in gps_data:
                lon_ref = gps_data[3]
                lon_degrees = gps_data[4]
                longitude = convert_to_degrees(lon_degrees)
                if lon_ref != "E":
                    longitude = -longitude
                gps_info["longitude"] = longitude
            
            # Extract altitude
            if 5 in gps_data and 6 in gps_data:
                alt_ref = gps_data[5]
                alt_data = gps_data[6]
                altitude = float(alt_data[0]) / float(alt_data[1])
                if alt_ref != b"\x00":  # Above sea level = 0, Below sea level = 1
                    altitude = -altitude
                gps_info["altitude"] = altitude
        
        return gps_info if gps_info else None
    except Exception:
        return None

def convert_to_degrees(value):
    """
    Convert GPS coordinates to degrees
    
    Args:
        value: GPS coordinates in EXIF format
        
    Returns:
        Coordinates in decimal degrees
    """
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    
    return d + (m / 60.0) + (s / 3600.0)

def analyze_image_metadata(image_path: str) -> Dict[str, Any]:
    """
    Perform comprehensive metadata analysis on an image
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary containing metadata analysis results
    """
    try:
        # Basic image info
        with Image.open(image_path) as img:
            width, height = img.size
            format = img.format
            mode = img.mode
        
        # EXIF data
        exif_data = get_exif_data(image_path)
        
        # GPS info
        gps_info = get_gps_info(exif_data)
        
        # Detect editing software
        editing_software = []
        software_indicators = ["photoshop", "gimp", "canva", "paint shop", "corel"]
        if exif_data:
            software = str(exif_data.get("Software", "")) + str(exif_data.get("ProcessingSoftware", ""))
            software_lower = software.lower()
            for indicator in software_indicators:
                if indicator in software_lower:
                    editing_software.append(indicator.title())
        
        return {
            "basic_info": {
                "width": width,
                "height": height,
                "format": format,
                "mode": mode
            },
            "exif_data": exif_data,
            "gps_info": gps_info,
            "editing_software_detected": editing_software,
            "metadata_complete": len(exif_data) > 0 if isinstance(exif_data, dict) else False
        }
    except Exception as e:
        return {
            "error": f"Failed to analyze metadata: {str(e)}",
            "basic_info": {},
            "exif_data": {},
            "gps_info": None,
            "editing_software_detected": [],
            "metadata_complete": False
        }
