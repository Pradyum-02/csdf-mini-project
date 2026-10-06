#!/usr/bin/env python
"""
Simple test script to verify the backend works
"""
import asyncio
import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from core.config import settings
from db.session import engine, SessionLocal
from models.case import Case
from models.evidence import Evidence

def test_database_connection():
    """Test that we can connect to the database"""
    try:
        # Create a session
        db = SessionLocal()
        
        # Try to query something simple
        case_count = db.query(Case).count()
        print(f"[OK] Database connection successful. Found {case_count} cases.")
        
        # Close the session
        db.close()
        return True
    except Exception as e:
        print(f"[ERROR] Database connection failed: {e}")
        return False

def test_settings():
    """Test that settings load correctly"""
    try:
        print(f"[OK] Settings loaded:")
        print(f"  - Project: {settings.PROJECT_NAME}")
        print(f"  - Version: {settings.VERSION}")
        print(f"  - Database URL: {settings.DATABASE_URL}")
        return True
    except Exception as e:
        print(f"[ERROR] Settings loading failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing ForensiPix backend...")
    print("=" * 40)
    
    success = True
    success &= test_settings()
    print()
    success &= test_database_connection()
    
    print("=" * 40)
    if success:
        print("[OK] All tests passed!")
        sys.exit(0)
    else:
        print("[ERROR] Some tests failed!")
        sys.exit(1)
