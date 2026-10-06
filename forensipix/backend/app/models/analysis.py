from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float, JSON
from sqlalchemy.sql import func
from app.db.base import Base

class Analysis(Base):
    __tablename__ = "analyses"
    
    id = Column(Integer, primary_key=True, index=True)
    evidence_id = Column(Integer, ForeignKey("evidence.id"))
    analysis_status = Column(String(50))  # pending, processing, completed, failed
    metadata_result = Column(JSON)
    integrity_result = Column(JSON)
    ela_result = Column(JSON)
    noise_result = Column(JSON)
    jpeg_result = Column(JSON)
    frequency_result = Column(JSON)
    copy_move_result = Column(JSON)
    steganography_result = Column(JSON)
    provenance_result = Column(JSON)
    ai_result = Column(JSON)
    overall_score = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
