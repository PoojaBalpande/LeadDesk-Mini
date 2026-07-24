# LeadDesk Mini — Modern Lead Management System

**LeadDesk Mini** is a production-grade Lead Management SaaS application built for the **Digital Heroes Training Task**. It allows visitors to submit business inquiries through a responsive landing page and provides authenticated administrators with a dashboard to search, filter, and transition lead pipeline statuses.

---

## 🏗️ Architecture Overview

The application follows a decoupled single-tenant architecture:

- **Frontend (`/frontend`)**: Next.js 16 (App Router), TypeScript, TailwindCSS, hosted on Vercel.
- **Backend (`/backend`)**: FastAPI (Python 3.12+), Uvicorn, Pydantic, hosted on Render.
- **Database (Phase 4+)**: Neon PostgreSQL, SQLAlchemy 2.0 ORM, Alembic migrations.
- **System Design & Specs (`/docs`)**: Full architecture blueprints, database ERDs, API contracts, and roadmap documents.

---

## 📁 Repository Structure

```
LeadDesk-Mini/
├── docs/                     # System design & architectural specifications
│   ├── REQUIREMENTS.md       # Functional & non-functional requirements
│   ├── TECH_STACK.md         # Technology rationale & tradeoffs
│   ├── SYSTEM_ARCHITECTURE.md# High-level diagrams (Mermaid)
│   ├── DATABASE_DESIGN.md    # ERD & schema specifications
│   ├── API_CONTRACT.md       # REST API contracts & payloads
│   ├── FOLDER_STRUCTURE.md   # Detailed directory layouts
│   ├── UI_PLANNING.md        # UI design system & layout specs
│   └── DEVELOPMENT_ROADMAP.md# 9-phase milestone implementation plan
│
├── frontend/                 # Next.js 16 App Router Frontend
│   ├── public/               # Static assets
│   └── src/                  # Source code (app, components, hooks, lib, services, types)
│
├── backend/                  # FastAPI Backend API Service
│   └── app/                  # Source code (api, core, db, middleware, models, schemas, services)
│
├── .github/                  # GitHub configuration
├── .gitignore                # Global gitignore configuration
└── README.md                 # Project introduction
```

---

## 🚀 Quick Start (Local Development)

### Prerequisites
- **Node.js**: v18.0.0 or higher
- **Python**: v3.10 or higher
- **npm**: v9.0.0 or higher

---

### 1. Running the Frontend (Next.js)

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start local development server
npm run dev
```

The frontend will be available at **`http://localhost:3000`**.

---

### 2. Running the Backend (FastAPI)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start uvicorn server with hot reload
uvicorn app.main:app --reload
```

The API will be available at **`http://localhost:8000`**.
- Interactive Swagger API Documentation: **`http://localhost:8000/docs`**
- Health Check Endpoint: **`http://localhost:8000/health`**

---

## 🔗 Attribution
Built for **[Digital Heroes Training Task](https://digitalheroesco.com)**.
