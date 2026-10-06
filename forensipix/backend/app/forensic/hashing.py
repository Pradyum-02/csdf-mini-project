import hashlib
import os
from typing import Dict

def calculate_file_hashes(file_path: str) -> Dict[str, str]:
    """
    Calculate SHA-256 and MD5 hashes of a file
    
    Args:
        file_path: Path to the file
        
    Returns:
        Dictionary containing sha256 and md5 hashes
    """
    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()
    
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
                md5_hash.update(chunk)
        
        return {
            "sha256": sha256_hash.hexdigest(),
            "md5": md5_hash.hexdigest()
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error calculating hashes: {str(e)}")

def verify_file_integrity(file_path: str, original_sha256: str, original_md5: str) -> Dict[str, bool]:
    """
    Verify file integrity by comparing hashes
    
    Args:
        file_path: Path to the file
        original_sha256: Original SHA-256 hash
        original_md5: Original MD5 hash
        
    Returns:
        Dictionary with verification results
    """
    hashes = calculate_file_hashes(file_path)
    
    return {
        "sha256_verified": hashes["sha256"] == original_sha256,
        "md5_verified": hashes["md5"] == original_md5,
        "current_sha256": hashes["sha256"],
        "current_md5": hashes["md5"]
    }
