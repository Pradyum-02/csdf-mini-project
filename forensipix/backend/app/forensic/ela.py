from PIL import Image, ImageChops, ImageEnhance
import numpy as np
import os
from typing import Dict, Any
import uuid

def perform_ela(image_path: str, quality: int = 90) -> Dict[str, Any]:
    """
    Perform Error Level Analysis on an image
    
    Args:
        image_path: Path to the image file
        quality: JPEG compression quality for ELA (default: 90)
        
    Returns:
        Dictionary containing ELA analysis results
    """
    try:
        # Open original image
        original = Image.open(image_path)
        
        # Save a temporary compressed version
        temp_filename = f"temp_ela_{uuid.uuid4().hex}.jpg"
        temp_path = os.path.join(os.path.dirname(image_path), temp_filename)
        
        # Convert to RGB if necessary
        if original.mode != 'RGB':
            original = original.convert('RGB')
        
        # Save compressed version
        original.save(temp_path, 'JPEG', quality=quality)
        
        # Open compressed image
        compressed = Image.open(temp_path)
        
        # Calculate difference
        ela_image = ImageChops.difference(original, compressed)
        
        # Enhance the difference to make it visible
        extrema = ela_image.getextrema()
        max_diff = max([ex[1] for ex in extrema])
        if max_diff == 0:
            max_diff = 1
        scale = 255.0 / max_diff
        
        ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
        
        # Save ELA image
        ela_filename = f"ela_{uuid.uuid4().hex}.png"
        ela_path = os.path.join(os.path.dirname(image_path), "derived", ela_filename)
        os.makedirs(os.path.dirname(ela_path), exist_ok=True)
        ela_image.save(ela_path)
        
        # Clean up temp file
        os.remove(temp_path)
        
        # Calculate statistics
        ela_array = np.array(ela_image)
        mean_intensity = np.mean(ela_array)
        std_intensity = np.std(ela_array)
        max_intensity = np.max(ela_array)
        
        # Determine if there are significant anomalies
        # This is a simplified heuristic - in practice, this would be more sophisticated
        anomaly_threshold = 10
        has_significant_anomalies = max_intensity > anomaly_threshold
        
        return {
            "ela_image_path": ela_path.replace(os.path.dirname(image_path), ""),
            "mean_intensity": float(mean_intensity),
            "std_intensity": float(std_intensity),
            "max_intensity": float(max_intensity),
            "quality_used": quality,
            "has_significant_anomalies": bool(has_significant_anomalies),
            "interpretation": "ELA highlights regions with different compression characteristics. "
                            "Higher values indicate potentially edited regions." if has_significant_anomalies
                            else "No significant compression differences detected."
        }
    except Exception as e:
        return {
            "error": f"ELA analysis failed: {str(e)}",
            "ela_image_path": "",
            "mean_intensity": 0.0,
            "std_intensity": 0.0,
            "max_intensity": 0.0,
            "quality_used": quality,
            "has_significant_anomalies": False,
            "interpretation": "Analysis could not be completed."
        }
