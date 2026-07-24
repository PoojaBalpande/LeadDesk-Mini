# Development Roadmap & Implementation Plan — LeadDesk Mini

This document outlines the phased milestone strategy for constructing **LeadDesk Mini**. Development follows standard Git branch workflows (`feature/<feature-name>`) and Conventional Commits syntax (`feat:`, `fix:`, `docs:`, `chore:`).

---

## Roadmap Overview

```
Phase 1: Project Initialization ──> Phase 2: CI/CD Setup ──> Phase 3: Frontend Development
                                                                       │
Phase 6: Auth Integration <── Phase 5: Lead Management API <── Phase 4: Backend Core
        │
        ▼
Phase 7: End-to-End Testing ──> Phase 8: Production Deployment ──> Phase 9: Documentation
```

---

## Detailed Milestone Phases

### Phase 1: Project Initialization & Repository Setup
- **Objectives**: Initialize monorepo directory structure, Git configuration, base environment configurations, and core README.
- **Tasks**:
  1. Create top-level repository folders (`frontend/`, `backend/`, `docs/`).
  2. Configure `.gitignore` for Python (`.venv`, `__pycache__`) and Node.js (`node_modules`, `.next`).
  3. Initialize Next.js 16 App Router application in `frontend/` with TypeScript, TailwindCSS, and ESLint.
  4. Initialize FastAPI application environment in `backend/` with `requirements.txt` and `pyproject.toml`.
- **Expected Deliverables**: Clean repository structure with building frontend skeleton and running FastAPI hello world endpoint.
- **Git Branch Name**: `feature/phase-1-init`
- **Suggested Commit Messages**:
  - `chore: initialize repository directory structure and docs`
  - `feat(frontend): setup Next.js 16 app router with TypeScript and TailwindCSS`
  - `feat(backend): initialize FastAPI app with base configuration`

---

### Phase 2: CI/CD Pipeline & Code Quality Setup
- **Objectives**: Automate code quality verification and type safety checks on git push.
- **Tasks**:
  1. Set up GitHub Actions workflow `.github/workflows/ci.yml`.
  2. Configure frontend linting (`npm run lint`) and TypeScript checking (`npm run type-check`).
  3. Configure backend linting (`ruff` / `flake8`) and Python type checking (`mypy`).
- **Expected Deliverables**: Passing GitHub Actions pipeline triggering on pull requests.
- **Git Branch Name**: `feature/phase-2-cicd`
- **Suggested Commit Messages**:
  - `ci: add GitHub Actions workflow for linting and type checking`
  - `chore: configure ESLint, Prettier, and Ruff code standards`

---

### Phase 3: Public Frontend Landing Page & Lead Form
- **Objectives**: Build responsive public landing page, hero section, lead form, and footer attribution.
- **Tasks**:
  1. Install shadcn/ui components (`button`, `input`, `select`, `textarea`, `card`, `toast`).
  2. Implement `Hero` component with responsive typography and CTA.
  3. Implement `LeadForm` using React Hook Form + Zod schema validation.
  4. Implement `Footer` component with attribution text: `"Built for Digital Heroes Training Task"` linked to `https://digitalheroesco.com`.
- **Expected Deliverables**: Fully functional landing page with client-side validation.
- **Git Branch Name**: `feature/phase-3-frontend-landing`
- **Suggested Commit Messages**:
  - `feat(frontend): create hero section and value proposition components`
  - `feat(frontend): implement lead capture form with React Hook Form and Zod`
  - `feat(frontend): add attribution footer with Digital Heroes link`

---

### Phase 4: Backend Core Setup & Database Models
- **Objectives**: Establish Neon PostgreSQL connection, SQLAlchemy models, and Alembic migrations.
- **Tasks**:
  1. Set up SQLAlchemy 2.0 database engine in `app/core/database.py`.
  2. Define `Lead` and `Admin` ORM models in `app/models/`.
  3. Initialize Alembic and create initial migration script (`0001_initial_schema.py`).
  4. Write `scripts/seed_admin.py` to populate initial administrator credentials.
- **Expected Deliverables**: Executable database migrations creating `leads` and `admins` tables in Neon Postgres.
- **Git Branch Name**: `feature/phase-4-backend-core`
- **Suggested Commit Messages**:
  - `feat(backend): configure SQLAlchemy database engine for Neon Postgres`
  - `feat(backend): define Lead and Admin database models`
  - `feat(backend): add Alembic migration for initial database schema`
  - `chore(backend): create admin seed script`

---

### Phase 5: Lead Management API & CRUD Layer
- **Objectives**: Implement public lead creation endpoint and protected lead querying endpoints.
- **Tasks**:
  1. Define Pydantic request/response schemas (`LeadCreate`, `LeadResponse`, `LeadStatusUpdate`).
  2. Implement CRUD functions in `app/crud/crud_lead.py` (create lead, list leads, search/filter, status update).
  3. Create endpoints `POST /api/v1/leads`, `GET /api/v1/leads`, and `PATCH /api/v1/leads/{id}/status`.
- **Expected Deliverables**: Tested REST API endpoints for submitting and updating leads.
- **Git Branch Name**: `feature/phase-5-lead-api`
- **Suggested Commit Messages**:
  - `feat(backend): create Pydantic schemas for lead requests and responses`
  - `feat(backend): implement CRUD operations for lead management`
  - `feat(backend): add POST /api/v1/leads public submission endpoint`
  - `feat(backend): add GET and PATCH endpoints for admin lead management`

---

### Phase 6: Admin Authentication & Guard Integration
- **Objectives**: Implement JWT token issuance, bcrypt password verification, protected admin routes, and dashboard interface.
- **Tasks**:
  1. Implement password hashing & verification utilities using `bcrypt`.
  2. Implement JWT token issuance and decoding functions in `app/core/security.py`.
  3. Create auth endpoints `POST /api/v1/auth/login` and `GET /api/v1/auth/me`.
  4. Create FastAPI dependency `get_current_admin` to guard protected lead endpoints.
  5. Connect frontend `/login` and `/dashboard` pages to API authentication.
- **Expected Deliverables**: Secure admin login flow and protected dashboard showing live lead records.
- **Git Branch Name**: `feature/phase-6-authentication`
- **Suggested Commit Messages**:
  - `feat(backend): implement bcrypt password hashing and JWT token management`
  - `feat(backend): add login endpoint and authentication middleware guard`
  - `feat(frontend): build admin login page and integrate JWT auth state`
  - `feat(frontend): build admin dashboard with search, filter, and status update`

---

### Phase 7: Testing & Verification
- **Objectives**: Verify API endpoints, form validations, search filters, and authentication security.
- **Tasks**:
  1. Write backend pytest suite for lead submission, login, and auth guard.
  2. Perform cross-browser testing for responsive layout alignment.
  3. Verify client-side and server-side validation error handling.
- **Expected Deliverables**: Passing pytest test suite and clean manual verification.
- **Git Branch Name**: `feature/phase-7-testing`
- **Suggested Commit Messages**:
  - `test(backend): add pytest unit tests for authentication and lead APIs`
  - `fix(frontend): refine mobile responsive layouts and form validation toasts`

---

### Phase 8: Deployment (Vercel + Render + Neon)
- **Objectives**: Deploy production frontend to Vercel and backend to Render connected to Neon PostgreSQL.
- **Tasks**:
  1. Deploy `frontend/` to Vercel and set `NEXT_PUBLIC_API_URL`.
  2. Deploy `backend/` to Render Web Service and set production environment variables (`DATABASE_URL`, `SECRET_KEY`, `CORS_ORIGINS`).
  3. Run Alembic migrations against production Neon database.
  4. Run production seed script for admin account.
- **Expected Deliverables**: Live production URLs for Frontend (Vercel) and Backend API (Render).
- **Git Branch Name**: `feature/phase-8-deployment`
- **Suggested Commit Messages**:
  - `chore(deploy): configure Vercel deployment settings`
  - `chore(deploy): add uvicorn start script and Render build configuration`

---

### Phase 9: Final Review & Documentation
- **Objectives**: Conduct final system audit, update repository README, and publish complete docs.
- **Tasks**:
  1. Complete README with architecture overview, live deployment URLs, and local setup instructions.
  2. Verify all 8 files in `docs/` match final deployment configuration.
- **Expected Deliverables**: Complete, production-ready LeadDesk Mini repository.
- **Git Branch Name**: `feature/phase-9-documentation`
- **Suggested Commit Messages**:
  - `docs: update main README with live deployment links and architectural setup`
  - `docs: finalize system design documentation suite`
