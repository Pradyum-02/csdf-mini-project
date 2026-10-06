from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
import os
import shutil
from pathlib import Path
from app.db.session import get_db
from app.models.evidence import Evidence
from app.models.case import Case
from app.schemas.evidence import Evidence, EvidenceCreate, EvidenceUpdate
from app.core.config import settings
import hashlib
from PIL import Image

router = APIRouter()

# Ensure storage directories exist
os.makedirs(os.path.join(settings.STORAGE_PATH, "evidence"), exist_ok=True)

def calculate_hashes(file_path: str):
    """Calculate SHA-256 and MD5 hashes of a file"""
    sha256_hash = hashlib.sha256()
    md5_hash = hashlib.md5()
    
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
            md5_hash.update(chunk)
    
    return {
        "sha256": sha256_hash.hexdigest(),
        "md5": md5_hash.hexdigest()
    }

@router.post("/upload/{case_id}", response_model=Evidence)
async def upload_evidence(
    case_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Verify case exists
    case = db.query(Case).filter(Case.id == case_id).first()
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    
    # Validate file type
    allowed_types = ["image/jpeg", "image/png", "image/tiff", "image/webp"]
    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400, 
            detail=f"File type {file.content_type} not allowed"
        )
    
    # Generate evidence number
    evidence_count = db.query(Evidence).filter(Evidence.case_id == case_id).count()
    evidence_number = f"EVD-{evidence_count + 1:04d}"
    
    # Create safe filename
    file_extension = Path(file.filename).suffix
    stored_filename = f"{evidence_number}{file_extension}"
    file_path = os.path.join(settings.STORAGE_PATH, "evidence", stored_filename)
    
    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Calculate hashes
    hashes = calculate_hashes(file_path)
    
    # Get image dimensions
    try:
        with Image.open(file_path) as img:
            width, height = img.size
            format = img.format
    except Exception:
        width = height = None
        format = None
    
    # Create evidence record
    db_evidence = Evidence(
        case_id=case_id,
        evidence_number=evidence_number,
        original_filename=file.filename,
        stored_filename=stored_filename,
        mime_type=file.content_type,
        file_size=os.path.getsize(file_path),
        sha256=hashes["sha256"],
        md5=hashes["md5"],
        width=width,
        height=height,
        format=format
    )
    
    db.add(db_evidence)
    db.commit()
    db.refresh(db_evidence)
    return db_evidence

@router.get("/", response_model=List[Evidence])
def read_evidence(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    evidence = db.query(Evidence).offset(skip).limit(limit).all()
    return evidence

@router.get("/{evidence_id}", response_model=Evidence)
def read_evidence_item(evidence_id: int, db: Session = Depends(get_db)):
    evidence = db.query(Evidence).filter(Evidence.id == evidence_id).first()
    if evidence is None:
        raise HTTPException(status_code=404, detail="Evidence not found")
    return evidence

@router.get("/{evidence_id}/download")
def download_evidence(evidence_id: int, db: Session = Depends(get_db)):
    evidence = db.query(Evidence).filter(Evidence.id == evidence_id).first()
    if evidence is None:
        raise HTTPException(status_code=404, detail="Evidence not found")
    
    file_path = os.path.join(settings.STORAGE_PATH, "evidence", evidence.stored_filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Evidence file not found")
    
    return FileResponse(
        file_path,
        media_type=evidence.mime_type,
        filename=evidence.original_filename
    )

@router.post("/{evidence_id}/verify-integrity")
def verify_integrity(evidence_id: int, db: Session = Depends(get_db)):
    evidence = db.query(Evidence).filter(Evidence.id == evidence_id).first()
    if evidence is None:
        raise HTTPException(status_code=404, detail="Evidence not found")
    
    file_path = os.path.join(settings.STORAGE_PATH, "evidence", evidence.stored_filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Evidence file not found")
    
    hashes = calculate_hashes(file_path)
    
    sha256_verified = hashes["sha256"] == evidence.sha256
    md5_verified = hashes["md5"] == evidence.md5
    
    return {
        "evidence_id": evidence_id,
        "sha256_verified": sha256_verified,
        "md5_verified": md5_verified,
        "original_sha256": evidence.sha256,
        "current_sha256": hashes["sha256"],
        "original_md5": evidence.md5,
        "current_md5": hashes["md5"]
    }
