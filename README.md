# IEP Assistant (Phase 1)

A privacy-first IEP (Individualized Education Program) drafting tool built with FastAPI and SQLModel.
This project helps special education teachers generate and manage IEP drafts without storing sensitive
student information. Future versions will include AI-assisted SMART goals, accommodations, and
progress-monitoring suggestions.

---

## Features
- CRUD for students (using pseudonymous IDs only)
- CRUD for IEPs and section drafting
- In-memory or SQLite storage (no PHI)
- REST API with automatic documentation (`/docs`)
- Clear privacy-first design choices
- Modular architecture ready for AI integration

---

## Tech Stack
- Python 3.11+
- FastAPI
- SQLModel (SQLite for development)
- Pydantic
- Uvicorn
- Jinja2 templates for simple UI

---

## Getting Started
### 1. Clone the repo
```bash
git clone https://github.com/MangDynasty/iep-assistant.git
cd iep-assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the development server
```bash
uvicorn app.main:app --reload
```

### Privacy & Ethical Considerations

This project is a demo and should never be used with real student names or PHI.
All student entries must use pseudonyms or placeholders (e.g., “Student A”).
Data is handled in-memory or stored in a local SQLite DB for development only.
Future work includes configurable local-only operation and optional encrypted storage.

### Roadmap
Phase 1 (current)
  Basic student + IEP CRUD
  Structured data models
  Export features (docx or HTML)
  Privacy enforcement (no PII)

Phase 2
  AI-assisted drafting for:
  Present levels
  SMART goals
  Accommodations
  Service recommendations
  Input sanitization for LLM safety

Phase 3
  Authentication (teacher accounts)
  Optional district-level analytics (synthetic data only)
  Deployment with limited demo functionality


### License

MIT License
