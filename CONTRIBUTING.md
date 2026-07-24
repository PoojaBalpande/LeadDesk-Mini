# Contributing Guidelines — LeadDesk Mini

Thank you for contributing to **LeadDesk Mini**! To maintain code quality, consistency, and clear project history, please follow the guidelines established below.

---

## 1. Branch Strategy

We follow a structured Git branching model aligned with our development roadmap:

- **`main`**: Production branch. Must always contain stable, tested, and deployable code.
- **`feature/<feature-name>`**: Feature branches branching off `main`.
  * *Examples*: `feature/phase-3-frontend-landing`, `feature/phase-5-lead-api`
- **`fix/<bug-name>`**: Bug fix branches for resolving defects.
  * *Examples*: `fix/lead-form-toast-delay`, `fix/cors-allowed-origins`
- **`docs/<doc-topic>`**: Documentation updates.
  * *Examples*: `docs/update-readme-setup`

---

## 2. Conventional Commits Standard

All commit messages MUST adhere to the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <short description>
```

### Commit Types:
- **`feat`**: A new feature for the user or API.
- **`fix`**: A bug fix.
- **`docs`**: Documentation changes only.
- **`style`**: Changes that do not affect the meaning of the code (formatting, white-space, formatting check).
- **`refactor`**: Code changes that neither fix a bug nor add a feature.
- **`test`**: Adding or correcting tests.
- **`chore`**: Maintenance tasks, build configuration, or dependency updates.

### Examples:
- `feat(frontend): implement responsive lead capture form`
- `feat(backend): add POST /api/v1/leads endpoint`
- `fix(backend): resolve CORS headers for localhost origin`
- `docs: update CONTRIBUTING.md guidelines`
- `chore(deps): add Prettier configuration`

---

## 3. Pull Request Workflow

1. **Branch Out**: Create a topic branch from `main` (`git checkout -b feature/your-feature-name`).
2. **Commit Changes**: Make atomic, focused commits following Conventional Commits format.
3. **Verify Locally**: Run formatting and linting checks before opening a pull request:
   - Frontend: `npm run lint` & `npm run format:check`
   - Backend: Ensure Python code adheres to PEP 8 standards.
4. **Push & Open PR**: Push branch to GitHub and create a Pull Request against `main`.
5. **PR Template**: Fill out the provided Pull Request template detailing changes and verification steps.

---

## 4. Coding & Code Style Standards

### Frontend (Next.js / TypeScript)
- Use functional components with explicit TypeScript interfaces/types.
- Use path aliases `@/*` for imports instead of relative paths (`../../../components`).
- Follow Prettier formatting rules (`semi: true`, `tabWidth: 2`, `singleQuote: false`).
- Run `npm run format` to automatically format frontend files.

### Backend (FastAPI / Python)
- Use standard Python type hints (`str`, `int`, `Optional[T]`) for functions and Pydantic models.
- Maintain clean modular architecture (`api/`, `core/`, `crud/`, `models/`, `schemas/`).
- Format code cleanly according to PEP 8 guidelines (4 spaces indentation).

---

## 5. Local Development Setup

### Prerequisites
- Node.js v18.0.0+
- Python v3.10+

### Frontend Setup (`/frontend`)
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup (`/backend`)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
