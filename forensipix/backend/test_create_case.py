#!/usr/bin/env python
"""
Test script to verify we can create a case
"""
import sys
import os

# Add the app directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from core.config import settings
from db.session import SessionLocal
from models.case import Case, CaseStatus

def test_create_case():
    """Test that we can create a case"""
    try:
        # Create a session
        db = SessionLocal()
        
        # Create a case
        test_case = Case(
            case_number="CASE-TEST-0001",
            title="Test Case",
            description="This is a test case",
            investigator_name="Test User",
            status=CaseStatus.OPEN
        )
        
        # Add to database
        db.add(test_case)
        db.commit()
        db.refresh(test_case)
        
        print(f"[OK] Created case with ID: {test_case.id}")
        print(f"     Case Number: {test_case.case_number}")
        print(f"     Title: {test_case.title}")
        
        # Clean up - delete the test case
        db.delete(test_case)
        db.commit()
        print(f"[OK] Cleaned up test case")
        
        # Close the session
        db.close()
        return True
    except Exception as e:
        print(f"[ERROR] Failed to create case: {e}")
        # Try to rollback if possible
        try:
            db.rollback()
        except:
            pass
        return False

if __name__ == "__main__":
    print("Testing case creation...")
    print("=" * 40)
    
    if test_create_case():
        print("=" * 40)
        print("[OK] Case creation test passed!")
        sys.exit(0)
    else:
        print("=" * 40)
        print("[ERROR] Case creation test failed!")
        sys.exit(1)
