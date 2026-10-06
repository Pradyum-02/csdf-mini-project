from PIL import Image
import numpy as np
import cv2
import os
from typing import Dict, Any
import uuid

def detect_copy_move(image_path: str) -> Dict[str, Any]:
    """
    Perform basic copy-move detection using SIFT features
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary containing copy-move detection results
    """
    try:
        # Read image
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Could not read image")
        
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Initialize SIFT detector
        sift = cv2.SIFT_create()
        
        # Find keypoints and descriptors
        keypoints, descriptors = sift.detectAndCompute(gray, None)
        
        if descriptors is None or len(keypoints) < 2:
            return {
                "keypoints_found": len(keypoints) if keypoints else 0,
                "matches_found": 0,
                "potential_matches": [],
                "has_significant_matches": False,
                "interpretation": "Not enough features detected for copy-move analysis."
            }
        
        # Match descriptors using BFMatcher
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(descriptors, descriptors, k=2)
        
        # Apply ratio test
        good_matches = []
        for match_pair in matches:
            if len(match_pair) == 2:
                m, n = match_pair
                if m.distance < 0.75 * n.distance:
                    good_matches.append(m)
        
        # Filter out matches where keypoints are too close (likely same feature)
        filtered_matches = []
        min_distance_threshold = 10  # Minimum distance between keypoints
        
        for match in good_matches:
            pt1 = keypoints[match.queryIdx].pt
            pt2 = keypoints[match.trainIdx].pt
            distance = np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)
            
            # Skip if it's the same keypoint or too close
            if match.queryIdx != match.trainIdx and distance > min_distance_threshold:
                filtered_matches.append(match)
        
        # Limit matches for visualization
        top_matches = filtered_matches[:20] if len(filtered_matches) > 20 else filtered_matches
        
        # Create visualization
        result_img = img.copy()
        match_image = cv2.drawMatches(img, keypoints, img, keypoints, top_matches, None, 
                                    matchColor=(0, 255, 0), singlePointColor=(255, 0, 0))
        
        # Save visualization
        match_filename = f"copymove_{uuid.uuid4().hex}.png"
        match_path = os.path.join(os.path.dirname(image_path), "derived", match_filename)
        os.makedirs(os.path.dirname(match_path), exist_ok=True)
        cv2.imwrite(match_path, match_image)
        
        # Determine if there are significant matches
        match_threshold = 8
        has_significant_matches = len(filtered_matches) > match_threshold
        
        return {
            "keypoints_found": len(keypoints),
            "matches_found": len(filtered_matches),
            "matches_visualization_path": match_path.replace(os.path.dirname(image_path), ""),
            "has_significant_matches": bool(has_significant_matches),
            "interpretation": f"Found {len(filtered_matches)} potential copy-move matches. "
                            "This may indicate duplicated or moved regions in the image." if has_significant_matches
                            else "No significant copy-move patterns detected."
        }
    except Exception as e:
        return {
            "error": f"Copy-move analysis failed: {str(e)}",
            "keypoints_found": 0,
            "matches_found": 0,
            "matches_visualization_path": "",
            "has_significant_matches": False,
            "interpretation": "Analysis could not be completed."
        }
