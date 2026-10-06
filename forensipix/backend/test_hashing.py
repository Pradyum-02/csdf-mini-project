#!/usr/bin/env python
"""
Test script to verify our hashing service works
"""
import sys
import os
import tempfile

# Add the app directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from forensic.hashing import calculate_file_hashes, verify_file_integrity

def test_hashing_service():
    """Test the hashing service"""
    try:
        # Create a test file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(b"This is a test file for hashing")
        temp_file.close()
        
        # Calculate hashes
        hashes = calculate_file_hashes(temp_file.name)
        
        # Verify we got both hashes
        assert 'sha256' in hashes
        assert 'md5' in hashes
        assert len(hashes['sha256']) == 64  # SHA-256 is 64 hex chars
        assert len(hashes['md5']) == 32   # MD5 is 32 hex chars
        
        # Verify integrity verification works
        integrity = verify_file_integrity(
            temp_file.name, 
            hashes['sha256'], 
            hashes['md5']
        )
        assert integrity['sha256_verified'] == True
        assert integrity['md5_verified'] == True
        
        # Clean up
        os.unlink(temp_file.name)
        
        print("[OK] Hashing service working correctly")
        return True
    except Exception as e:
        print(f"[ERROR] Hashing service failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing ForensiPix hashing service...")
    print("=" * 40)
    
    if test_hashing_service():
        print("=" * 40)
        print("[OK] Hashing service test passed!")
        sys.exit(0)
    else:
        print("=" * 40)
        print("[ERROR] Hashing service test failed!")
        sys.exit(1)
