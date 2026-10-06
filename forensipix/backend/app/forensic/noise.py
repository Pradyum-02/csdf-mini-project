from PIL import Image
import numpy as np
import os
from typing import Dict, Any
import uuid
import cv2

def analyze_noise(image_path: str) -> Dict[str, Any]:
    """
    Perform noise analysis on an image
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary containing noise analysis results
    """
    try:
        # Read image
        image = Image.open(image_path)
        
        # Convert to grayscale
        if image.mode != 'L':
            gray_image = image.convert('L')
        else:
            gray_image = image
        
        # Convert to numpy array
        img_array = np.array(gray_image, dtype=np.float64)
        
        # Apply Gaussian blur to get the low-frequency component
        blurred = cv2.GaussianBlur(img_array, (5, 5), 1.0)
        
        # Calculate residual (noise)
        residual = img_array - blurred
        
        # Calculate statistics
        noise_mean = np.mean(residual)
        noise_variance = np.var(residual)
        noise_std = np.std(residual)
        
        # Calculate regional variance (divide into 4 quadrants)
        h, w = img_array.shape
        quad_size_h, quad_size_w = h // 2, w // 2
        
        quadrants = [
            residual[0:quad_size_h, 0:quad_size_w],           # Top-left
            residual[0:quad_size_h, quad_size_w:w],           # Top-right
            residual[quad_size_h:h, 0:quad_size_w],           # Bottom-left
            residual[quad_size_h:h, quad_size_w:w]            # Bottom-right
        ]
        
        quadrant_variances = [float(np.var(q)) for q in quadrants]
        
        # Save noise visualization
        # Normalize residual for visualization
        residual_normalized = ((residual - noise_mean) / (noise_std + 1e-8)) * 50 + 128
        residual_normalized = np.clip(residual_normalized, 0, 255).astype(np.uint8)
        noise_image = Image.fromarray(residual_normalized)
        
        noise_filename = f"noise_{uuid.uuid4().hex}.png"
        noise_path = os.path.join(os.path.dirname(image_path), "derived", noise_filename)
        os.makedirs(os.path.dirname(noise_path), exist_ok=True)
        noise_image.save(noise_path)
        
        # Determine if there are significant anomalies
        # High variance in certain regions might indicate tampering
        variance_threshold = 100
        high_variance_regions = sum(1 for v in quadrant_variances if v > variance_threshold)
        has_significant_anomalies = high_variance_regions > 1
        
        return {
            "noise_image_path": noise_path.replace(os.path.dirname(image_path), ""),
            "noise_mean": float(noise_mean),
            "noise_variance": float(noise_variance),
            "noise_std": float(noise_std),
            "quadrant_variances": quadrant_variances,
            "has_significant_anomalies": bool(has_significant_anomalies),
            "interpretation": "Noise analysis examines sensor noise patterns. "
                            "Inconsistent noise patterns may indicate digital manipulation." if has_significant_anomalies
                            else "Noise patterns appear consistent across the image."
        }
    except Exception as e:
        return {
            "error": f"Noise analysis failed: {str(e)}",
            "noise_image_path": "",
            "noise_mean": 0.0,
            "noise_variance": 0.0,
            "noise_std": 0.0,
            "quadrant_variances": [0.0, 0.0, 0.0, 0.0],
            "has_significant_anomalies": False,
            "interpretation": "Analysis could not be completed."
        }
