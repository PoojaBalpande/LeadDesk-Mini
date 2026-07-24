# System Architecture — LeadDesk Mini

This document outlines the architectural blueprints for **LeadDesk Mini**, demonstrating system boundaries, data communication pathways, authentication mechanisms, and continuous deployment pipelines.

---

## 1. High-Level System Architecture Diagram

```mermaid
graph TD
    subgraph Client Layer
        A[Public Visitor Browser]
        B[Admin Browser]
    end

    subgraph Frontend Layer - Vercel Edge Network
        C[Next.js 16 App Router]
        C1[Public Landing Page / Lead Capture Form]
        C2[Admin Login Page]
        C3[Protected Admin Dashboard]
    end

    subgraph Backend Layer - Render Web Service
        D[FastAPI REST Application]
        D1[Public API Router: /api/v1/leads]
        D2[Auth API Router: /api/v1/auth]
        D3[JWT Middleware / Auth Guard]
        D4[CRUD Service Layer]
    end

    subgraph Persistence Layer - Neon Cloud
        E[(Neon PostgreSQL)]
        E1[(leads Table)]
        E2[(admins Table)]
    end

    %% Flow Connections
    A -->|1. HTTP GET Landing Page| C1
    A -->|2. POST /api/v1/leads| D1
    B -->|3. POST /api/v1/auth/login| D2
    B -->|4. Authenticated Request + Bearer Token| D3
    
    D1 -->|Validate & Insert Lead| D4
    D2 -->|Verify Bcrypt Password| D4
    D3 -->|Guard Passed| D4
    
    D4 -->|SQLAlchemy 2.0 Async Queries| E
    E --> E1
    E --> E2
```

---

## 2. Component Descriptions

### 2.1 Client Layer
- **Public Visitor**: Interacts with the landing page, submits business inquiries via the lead form.
- **Admin User**: Accesses the `/login` route, authenticates to receive a JWT, and manages leads on the `/dashboard` route.

### 2.2 Frontend Layer (Vercel)
- **Next.js 16 App Router**: Serves static and server-rendered React components.
- **Zod & React Hook Form**: Validates inputs client-side before sending network requests.
- **API Client Layer (Axios/Fetch)**: Communicates asynchronously with the backend API service, appending JWT authorization headers when required.

### 2.3 Backend Layer (Render)
- **FastAPI Core**: Handles incoming HTTP requests, route matching, and exception mapping.
- **Pydantic Validation Layer**: Validates payload structures and coerces data types on request entry.
- **Security Guard (`security.py`)**: Extracts HTTP Bearer JWT tokens, decodes claims, verifies signatures, and rejects invalid/expired access attempts with `401 Unauthorized`.
- **CRUD Service Layer (`crud/`)**: Encapsulates business logic and SQL database interactions away from the API routing handlers.

### 2.4 Persistence Layer (Neon PostgreSQL)
- Fully managed PostgreSQL serverless instance hosting database schema tables (`leads`, `admins`), constraints, triggers, and indices.

---

## 3. End-to-End Request Flow Diagram

The diagram below details the step-by-step execution lifecycle for a public visitor submitting a business lead.

```mermaid
sequenceDiagram
    autonumber
    actor Visitor as Visitor (Browser)
    participant Form as React Hook Form + Zod
    participant API as FastAPI Backend (/api/v1/leads)
    participant Schema as Pydantic LeadCreate
    participant DB as Neon PostgreSQL

    Visitor->>Form: Fill Name, Email, Budget, Message & Click Submit
    Form->>Form: Execute Zod Schema Validation
    alt Client Validation Fails
        Form-->>Visitor: Display Inline Field Error Messages
    else Client Validation Passes
        Form->>API: HTTP POST /api/v1/leads (JSON Payload)
        API->>Schema: Validate Request Body Data Types
        alt Server Validation Fails
            Schema-->>API: ValidationError Exception
            API-->>Visitor: HTTP 422 Unprocessable Entity (JSON Error Details)
        else Server Validation Passes
            API->>DB: SQLAlchemy INSERT INTO leads (status='NEW')
            DB-->>API: Record Created (Returns Lead ID & Timestamp)
            API-->>Visitor: HTTP 201 Created (Lead Response JSON)
            Visitor-->>Visitor: Show Toast "Inquiry Submitted Successfully!"
        end
    end
```

---

## 4. Authentication & Authorization Flow Diagram

The diagram below outlines the JWT authentication lifecycle for administrator access.

```mermaid
sequenceDiagram
    autonumber
    actor Admin as Admin User
    participant Frontend as Next.js Dashboard App
    participant AuthAPI as FastAPI /api/v1/auth/login
    participant JWTGuard as Auth Middleware
    participant DB as Neon PostgreSQL

    Admin->>Frontend: Enter Email & Password on /login
    Frontend->>AuthAPI: HTTP POST /api/v1/auth/login {email, password}
    AuthAPI->>DB: SELECT * FROM admins WHERE email = :email
    DB-->>AuthAPI: Admin Record (hashed_password)
    AuthAPI->>AuthAPI: Verify password with bcrypt.checkpw()
    alt Invalid Credentials
        AuthAPI-->>Frontend: HTTP 401 Unauthorized {"detail": "Invalid credentials"}
        Frontend-->>Admin: Show Error Alert "Invalid email or password"
    else Valid Credentials
        AuthAPI->>AuthAPI: Generate Signed JWT Token (exp: 24 hours)
        AuthAPI-->>Frontend: HTTP 200 OK {"access_token": "eyJ...", "token_type": "bearer"}
        Frontend->>Frontend: Store Token in Auth State / Cookie
        Frontend-->>Admin: Redirect to /dashboard
    end

    %% Subsequent Authenticated Request
    Admin->>Frontend: View Leads List / Filter Status
    Frontend->>JWTGuard: HTTP GET /api/v1/leads (Header: Authorization: Bearer eyJ...)
    JWTGuard->>JWTGuard: Verify Signature & Expiration Date
    alt Invalid or Expired Token
        JWTGuard-->>Frontend: HTTP 401 Unauthorized
        Frontend->>Frontend: Clear Token & Redirect to /login
    else Valid Token
        JWTGuard->>DB: SELECT * FROM leads ORDER BY created_at DESC
        DB-->>JWTGuard: Return Leads Records
        JWTGuard-->>Frontend: HTTP 200 OK [Leads JSON Array]
        Frontend-->>Admin: Render Dashboard Data Table
    end
```

---

## 5. Deployment & CI/CD Flow Diagram

```mermaid
graph LR
    subgraph Development Workflow
        Developer[Developer Machine] -->|Git Push| GitHub[GitHub Repository]
    end

    subgraph CI/CD Pipeline - GitHub Actions
        GitHub --> Workflows[GitHub Actions Runner]
        Workflows --> Lint[Frontend & Backend Linting]
        Workflows --> TypeCheck[TypeScript & MyPy Type Checking]
        Workflows --> Tests[Execute Unit & API Integration Tests]
    end

    subgraph Production Deployment
        Tests -->|Merge to main| Release[Production Release Trigger]
        Release -->|Webhook Deployment| Vercel[Vercel Edge Deployment - Frontend]
        Release -->|Webhook Deployment| Render[Render Web Service Deployment - Backend]
        Render -->|Apply Database Migrations| Neon[(Neon PostgreSQL Database)]
    end
```

---

## 6. Environment Configurations & Secrets Management

| Component | Variable Name | Purpose | Example / Value Source |
|---|---|---|---|
| Frontend | `NEXT_PUBLIC_API_URL` | Base Backend API URL | `https://leaddesk-api.onrender.com` |
| Backend | `DATABASE_URL` | Neon PostgreSQL Connection String | `postgresql+asyncpg://user:pass@ep-xyz.neon.tech/leaddesk` |
| Backend | `SECRET_KEY` | HS256 JWT Secret Signing Key | High-entropy 256-bit random string |
| Backend | `ALGORITHM` | JWT Signature Algorithm | `HS256` |
| Backend | `ACCESS_TOKEN_EXPIRE_MINUTES` | Token Validity Duration | `1440` (24 Hours) |
| Backend | `CORS_ORIGINS` | Permitted Frontend Origins | `["https://leaddesk.vercel.app"]` |
