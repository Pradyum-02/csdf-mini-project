from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Dict, Any
from app.db.session import get_db
from app.models.evidence import Evidence
from app.forensic.hashing import calculate_file_hashes, verify_file_integrity
from app.forensic.metadata import analyze_image_metadata
from app.forensic.ela import perform_ela
from app.forensic.noise import analyze_noise
from app.forensic.copy_move import detect_copy_move
from app.forensic.provenance import check_provenance
from app.forensic.ai_analyzer import analyze_image_ai
from app.forensic.scoring import calculate_forensic_score
from app.core.config import settings
import os

router = APIRouter()

def get_evidence_file_path(evidence_id: int, db: Session) -> str:
    """Get the file path for an evidence item"""
    evidence = db.query(Evidence).filter(Evidence.id == evidence_id).first()
    if evidence is None:
        raise HTTPException(status_code=404, detail="Evidence not found")
    
    file_path = os.path.join(settings.STORAGE_PATH, "evidence", evidence.stored_filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Evidence file not found")
    
    return file_path

@router.get("/{evidence_id}/hashing")
def get_hashing_info(evidence_id: int, db: Session = Depends(get_db)):
    """Get cryptographic hash information for evidence"""
    file_path = get_evidence_file_path(evidence_id, db)
    hashes = calculate_file_hashes(file_path)
    return {
        "evidence_id": evidence_id,
        "hashes": hashes,
        "algorithm": "SHA-256 and MD5"
    }

@router.post("/{evidence_id}/verify-integrity")
def verify_evidence_integrity(evidence_id: int, db: Session = Depends(get_db)):
    """Verify the integrity of evidence by comparing stored vs current hashes"""
    evidence = db.query(Evidence).filter(Evidence.id == evidence_id).first()
    if evidence is None:
        raise HTTPException(status_code=404, detail="Evidence not found")
    
    file_path = get_evidence_file_path(evidence_id, db)
    integrity_result = verify_file_integrity(
        file_path, 
        evidence.sha256, 
        evidence.md5
    )
    
    return {
        "evidence_id": evidence_id,
        "integrity_verification": integrity_result
    }

@router.get("/{evidence_id}/metadata")
def get_metadata_info(evidence_id: int, db: Session = Depends(get_db)):
    """Get metadata information for evidence"""
    file_path = get_evidence_file_path(evidence_id, db)
    metadata_result = analyze_image_metadata(file_path)
    return {
        "evidence_id": evidence_id,
        "metadata_analysis": metadata_result
    }

@router.get("/{evidence_id}/ela")
def get_ela_info(evidence_id: int, db: Session = Depends(get_db)):
    """Get ELA (Error Level Analysis) information for evidence"""
    file_path = get_evidence_file_path(evidence_id, db)
    ela_result = perform_ela(file_path)
    return {
        "evidence_id": evidence_id,
        "ela_analysis": ela_result
    }

@router.get("/{evidence_id}/noise")
def get_noise_info(evidence_id: int, db: Session = Depends(get_db)):
    """Get noise analysis information for evidence"""
    file_path = get_evidence_file_path(evidence_id, db)
    noise_result = analyze_noise(file_path)
    return {
        "evidence_id": evidence_id,
        "noise_analysis": noise_result
    }

@router.get("/{evidence_id}/copy-move")
def get_copy_move_info(evidence_id: int, db: Session = Depends(get_db)):
    """Get copy-move analysis information for evidence"""
    file_path = get_evidence_file_path(evidence_id, db)
    copymove_result = detect_copy_move(file_path)
    return {
        "evidence_id": evidence_id,
        "copy_move_analysis": copymove_result
    }

@router.get("/{evidence_id}/provenance")
def get_provenance_info(evidence_id: int, db: Session = Depends(get_db)):
    """Get provenance information for evidence"""
    file_path = get_evidence_file_path(evidence_id, db)
    provenance_result = check_provenance(file_path)
    return {
        "evidence_id": evidence_id,
        "provenance_analysis": provenance_result
    }

@router.get("/{evidence_id}/ai")
def get_ai_info(evidence_id: int, db: Session = Depends(get_db)):
    """Get AI-assisted analysis information for evidence"""
    file_path = get_evidence_file_path(evidence_id, db)
    ai_result = analyze_image_ai(file_path)
    return {
        "evidence_id": evidence_id,
        "ai_analysis": ai_result
    }

@router.get("/{evidence_id}/analysis")
def get_full_analysis(evidence_id: int, db: Session = Depends(get_db)):
    """Get complete forensic analysis for evidence"""
    file_path = get_evidence_file_path(evidence_id, db)
    
    # Run all analyses
    hashes = calculate_file_hashes(file_path)
    metadata_result = analyze_image_metadata(file_path)
    ela_result = perform_ela(file_path)
    noise_result = analyze_noise(file_path)
    copymove_result = detect_copy_move(file_path)
    provenance_result = check_provenance(file_path)
    ai_result = analyze_image_ai(file_path)
    
    # Compile results
    analysis_results = {
        "hashing": hashes,
        "metadata": metadata_result,
        "ela": ela_result,
        "noise": noise_result,
        "copy_move": copymove_result,
        "provenance": provenance_result,
        "ai": ai_result
    }
    
    # Calculate forensic score
    scoring_result = calculate_forensic_score(analysis_results)
    
    return {
        "evidence_id": evidence_id,
        "analyses": analysis_results,
        "forensic_scoring": scoring_result
    }
