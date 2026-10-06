from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EvidenceBase(BaseModel):
    original_filename: str
    mime_type: Optional[str] = None
    file_size: Optional[int] = None

class EvidenceCreate(EvidenceBase):
    pass

class EvidenceUpdate(BaseModel):
    original_filename: Optional[str] = None

class EvidenceInDBBase(EvidenceBase):
    id: int
    case_id: int
    evidence_number: str
    stored_filename: str
    mime_type: str
    file_size: int
    sha256: str
    md5: str
    width: Optional[int] = None
    height: Optional[int] = None
    format: Optional[str] = None
    acquisition_timestamp: Optional[datetime] = None
    created_at: datetime

    class Config:
        orm_mode = True

class Evidence(EvidenceInDBBase):
    pass
