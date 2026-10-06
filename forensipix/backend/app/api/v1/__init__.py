from fastapi import APIRouter
from . import cases, evidence, forensic

api_router = APIRouter()
api_router.include_router(cases.router, prefix="/cases", tags=["cases"])
api_router.include_router(evidence.router, prefix="/evidence", tags=["evidence"])
api_router.include_router(forensic.router, prefix="/evidence/{evidence_id}", tags=["forensic"])
