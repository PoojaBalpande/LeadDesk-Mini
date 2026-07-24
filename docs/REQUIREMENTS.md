# Requirements Specification — LeadDesk Mini

## 1. Project Overview
**LeadDesk Mini** is a modern, single-tenant Lead Management SaaS application. It provides a public-facing landing page for potential client lead capture and a secure, authenticated administration dashboard for managing lead pipelines. 

---

## 2. User Roles & Access Control

| Role | Access Level | Responsibilities |
|---|---|---|
| **Public Visitor** | Unauthenticated | • View landing page, hero section, and company information.<br>• Submit business inquiries via the lead capture form.<br>• Access external partner/training links. |
| **Admin User** | Authenticated (JWT) | • Authenticate via email & password.<br>• Access the protected Admin Dashboard.<br>• Search and filter submitted lead records.<br>• Transition lead pipeline status (`NEW` → `CONTACTED` → `CLOSED`). |

---

## 3. Functional Requirements

### 3.1 Public Landing Page & Lead Capture
- **FR-1.1**: The application MUST display a responsive, modern hero section outlining value propositions.
- **FR-1.2**: The application MUST render a public lead capture form collecting the following mandatory fields:
  - `Name` (String, 2-100 characters)
  - `Email` (String, valid RFC 5322 email format)
  - `Budget Range` (Selectable Option: `$1k - $5k`, `$5k - $15k`, `$15k - $50k`, `$50k+`)
  - `Message` (Text, 10-1000 characters)
- **FR-1.3**: The lead form MUST execute client-side schema validation using Zod and React Hook Form prior to HTTP submission.
- **FR-1.4**: The lead form MUST handle submission states gracefully with visual loading indicators and success/error feedback toasts.
- **FR-1.5**: The public footer MUST include the exact attribution text: `"Built for Digital Heroes Training Task"` hyperlinked directly to `https://digitalheroesco.com`.

### 3.2 Lead Ingestion & Validation (Backend)
- **FR-2.1**: The API MUST execute server-side payload validation using Pydantic schemas for all incoming lead submissions.
- **FR-2.2**: The API MUST reject malformed payloads with a `422 Unprocessable Entity` or `400 Bad Request` HTTP status and structured error details.
- **FR-2.3**: Upon successful validation, the backend MUST persist lead records to the Neon PostgreSQL database with a default status of `NEW` and an auto-generated timestamp.

### 3.3 Admin Authentication & Authorization
- **FR-3.1**: The API MUST provide a secure login endpoint (`POST /api/v1/auth/login`) accepting email and password credentials.
- **FR-3.2**: User passwords MUST be hashed using `bcrypt` (work factor >= 12) before database comparison or storage.
- **FR-3.3**: Upon successful login, the API MUST issue a JSON Web Token (JWT) containing standard claims (`sub`, `exp`, `iat`) signed with HS256.
- **FR-3.4**: All admin endpoints MUST verify the HTTP `Authorization: Bearer <token>` header before granting access.

### 3.4 Admin Dashboard & Lead Management
- **FR-4.1**: Authenticated admins MUST be able to view a paginated/scrollable list of all submitted leads sorted by `created_at` descending.
- **FR-4.2**: The dashboard MUST support real-time search filtering across `Name`, `Email`, and `Message` fields.
- **FR-4.3**: The dashboard MUST support filtering leads by status (`ALL`, `NEW`, `CONTACTED`, `CLOSED`).
- **FR-4.4**: Admins MUST be able to transition a lead's status between `NEW`, `CONTACTED`, and `CLOSED`.
- **FR-4.5**: Status changes MUST update the database record along with an `updated_at` timestamp trigger.

---

## 4. Non-Functional Requirements

### 4.1 Security
- **NFR-1.1 Password Safety**: No plain-text passwords stored or logged.
- **NFR-1.2 Transport Security**: All communications forced over HTTPS in production.
- **NFR-1.3 CORS Policy**: Restrict API origin access to verified frontend domains (`*.vercel.app` & custom domain).
- **NFR-1.4 Vulnerability Mitigation**: Prevent SQL Injection (handled via SQLAlchemy parameterization) and XSS (React DOM auto-escaping).

### 4.2 Performance & Scalability
- **NFR-2.1 Response Latency**: Public lead submission API endpoint latency < 200ms (P95).
- **NFR-2.2 Database Query Efficiency**: Database indexing on `leads.status` and `leads.created_at` to ensure fast search and filter queries.
- **NFR-2.3 Asset Optimization**: Frontend bundle optimized via Next.js App Router code-splitting and server components.

### 4.3 Maintainability & Code Quality
- **NFR-3.1 Type Safety**: End-to-end type safety (TypeScript on Frontend, Python Type Hints + Pydantic on Backend).
- **NFR-3.2 Architecture Pattern**: Strict separation of concerns (Presentation → API Router → CRUD Service → Database Model).
- **NFR-3.3 Automated Linting**: ESLint + Prettier for TypeScript; Black + Flake8 / Ruff for Python.

---

## 5. Core Features Matrix

| Feature | Target User | Priority | Complexity |
|---|---|---|---|
| Public Responsive Landing Page | Visitor | P0 | Low |
| Lead Submission Form + Validation | Visitor | P0 | Low |
| Admin JWT Login System | Admin | P0 | Medium |
| Protected Admin Dashboard | Admin | P0 | Medium |
| Lead Search & Filter | Admin | P0 | Medium |
| Lead Status Updater (`NEW`/`CONTACTED`/`CLOSED`) | Admin | P0 | Low |
| Footer Link (`https://digitalheroesco.com`) | Visitor | P0 | Low |

---

## 6. Future Improvements (Post-MVP Roadmap)

1. **Email Notifications**: Integration with Resend or SendGrid to send instant lead receipt emails to admins and auto-responders to visitors.
2. **Multi-Tenancy Support**: Support for multiple organizations with separate lead pipelines and admin team permissions.
3. **CSV/Excel Export**: Export filtered lead lists for offline CRM imports.
4. **Analytics & Funnel Charts**: Visual conversion rates, budget distribution charts, and lead response velocity metrics.
5. **Webhook Integrations**: Trigger Slack / Discord notifications on new lead submissions.
