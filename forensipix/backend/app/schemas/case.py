from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CaseBase(BaseModel):
    title: str
    description: Optional[str] = None
    investigator_name: Optional[str] = None

class CaseCreate(CaseBase):
    pass

class CaseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    investigator_name: Optional[str] = None

class CaseInDBBase(CaseBase):
    id: int
    case_number: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class Case(CaseInDBBase):
    pass
