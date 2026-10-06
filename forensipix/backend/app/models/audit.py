from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(Integer, ForeignKey("cases.id"))
    evidence_id = Column(Integer, ForeignKey("evidence.id"))
    action = Column(String(255), nullable=False)
    actor = Column(String(255))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    details = Column(Text)
    previous_hash = Column(String(64))
    current_hash = Column(String(64))
