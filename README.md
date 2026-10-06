# ForensiPix — Digital Image Forensics & Evidence Analyzer

ForensiPix is a modern web-based digital image forensic investigation platform.

## Features

- Case Management
- Evidence Ingestion with Integrity Verification
- Cryptographic Hashing (SHA-256, MD5)
- Metadata Analysis (EXIF, GPS, etc.)
- File Integrity Validation
- Error Level Analysis (ELA)
- Noise Analysis
- Copy-Move Detection
- Provenance Checking
- AI-Assisted Analysis (pluggable)
- Forensic Scoring System
- Professional PDF Reporting
- Complete Audit Trail
- Interactive Dashboard

## Technology Stack

### Frontend
- React 18+ with TypeScript
- Vite
- Tailwind CSS
- React Router
- Axios
- Recharts
- Lucide React
- React Dropzone
- Leaflet / React Leaflet

### Backend
- Python 3.11+
- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- PostgreSQL (SQLite for development)
- OpenCV, Pillow, NumPy, SciPy
- scikit-image
- ReportLab
- python-multipart
- cryptography

## Installation

### Prerequisites
- Node.js 16+ and npm
- Python 3.11+ and uv
- PostgreSQL (production) or SQLite (development)

### Backend Setup
```bash
cd forensipix/backend
uv sync
```

### Frontend Setup
```bash
cd forensipix/frontend
npm install
```

## Usage

### Development
```bash
# Backend
cd forensipix/backend
uv run uvicorn main:app --reload

# Frontend (separate terminal)
cd forensipix/frontend
npm run dev
```

## API Endpoints

Key endpoints include:
- POST /api/v1/cases/ - Create case
- POST /api/v1/cases/{case_id}/evidence/upload - Upload evidence
- GET /api/v1/evidence/{id}/analysis - Complete forensic analysis
- POST /api/v1/reports/{evidence_id}/generate - Generate report

See the source code for complete API documentation.

## Forensic Methodology

Analyses are designed to be transparent and reversible:
1. Evidence integrity verification via hashing
2. Metadata extraction and analysis
3. Error Level Analysis for compression variations
4. Noise analysis for sensor pattern examination
5. Copy-move detection for duplicated regions
6. Provenance checking for content credentials
7. AI-assisted analysis (pluggable)
8. Transparent risk scoring system

## Limitations

- Academic/prototype implementation
- Some techniques simplified for educational purposes
- AI analysis requires configured model
- Should be used as investigative aid, not definitive proof

For more information, see the source code and inline documentation.
