# Production-Grade Folder Structure — LeadDesk Mini

This document details the modular, maintainable project structure for both the **Next.js 16 Frontend** and the **FastAPI Backend** repository components.

---

## 1. Top-Level Repository Overview

```
LeadDesk-Mini/
├── docs/                     # System design & architectural documentation
├── frontend/                 # Next.js 16 App Router Frontend Application
├── backend/                  # FastAPI + SQLAlchemy Backend API Application
├── .github/
│   └── workflows/            # GitHub Actions CI/CD pipeline definitions
├── .gitignore                # Global git ignore configuration
├── LICENSE                   # Project license file
└── README.md                 # Project introduction and quick-start guide
```

---

## 2. Frontend Folder Structure (`frontend/`)

Built using **Next.js 16 (App Router)**, **TypeScript**, **TailwindCSS**, **shadcn/ui**, **React Hook Form**, and **Zod**.

```
frontend/
├── public/                   # Static assets (favicons, images, logos)
│   └── favicon.ico
├── src/
│   ├── app/                  # Next.js App Router file-system routes
│   │   ├── layout.tsx        # Root Application Layout & Font providers
│   │   ├── page.tsx          # Public Landing Page Component
│   │   ├── login/
│   │   │   └── page.tsx      # Admin Authentication Page
│   │   ├── dashboard/
│   │   │   ├── layout.tsx    # Dashboard Protected Layout with Header/Sidebar
│   │   │   └── page.tsx      # Admin Leads Management Dashboard Page
│   │   └── globals.css       # TailwindCSS direct directives & Design Tokens
│   │
│   ├── components/           # Modular React components
│   │   ├── ui/               # Primitive shadcn/ui components (Button, Input, Table, Badge)
│   │   │   ├── button.tsx
│   │   │   ├── input.tsx
│   │   │   ├── select.tsx
│   │   │   ├── table.tsx
│   │   │   ├── badge.tsx
│   │   │   └── toast.tsx
│   │   ├── landing/          # Landing page specific components
│   │   │   ├── Hero.tsx      # High-converting Hero section
│   │   │   ├── LeadForm.tsx  # Lead capture form (React Hook Form + Zod)
│   │   │   └── Footer.tsx    # Attribution footer with Digital Heroes link
│   │   └── dashboard/        # Dashboard specific components
│   │       ├── Header.tsx    # Dashboard navbar with Admin Logout button
│   │       ├── LeadTable.tsx # Data table with sorting & inline status dropdown
│   │       ├── LeadFilter.tsx# Search input and status filter buttons
│   │       └── StatCards.tsx # Metrics summary (Total, New, Contacted, Closed)
│   │
│   ├── hooks/                # Custom React Hooks
│   │   ├── useAuth.ts        # Admin Auth state hook (token, login, logout)
│   │   └── useLeads.ts       # Data fetching & status mutation hook
│   │
│   ├── lib/                  # Application utilities & external clients
│   │   ├── api.ts            # Axios HTTP Client instance with Interceptors
│   │   ├── utils.ts          # Tailwind class merger (clsx + tailwind-merge)
│   │   └── validations/      # Zod validation schemas
│   │       ├── lead.ts       # Client-side Lead form validation schema
│   │       └── auth.ts       # Client-side Login validation schema
│   │
│   └── types/                # TypeScript Interface & Type Definitions
│       ├── lead.ts           # Lead data interfaces & Status enums
│       └── auth.ts           # Auth response & User interfaces
│
├── .env.example              # Template environment variables file
├── next.config.ts            # Next.js framework configuration
├── package.json              # NPM dependencies and scripts
├── postcss.config.mjs        # PostCSS configuration for Tailwind
├── tailwind.config.ts        # TailwindCSS design system theme extension
└── tsconfig.json             # TypeScript compiler settings
```

### Folder Responsibilities (`frontend/`)
- **`src/app/`**: Route definitions using Next.js App Router conventions (`page.tsx`, `layout.tsx`).
- **`src/components/ui/`**: Reusable primitive design system components (shadcn/ui).
- **`src/components/landing/`**: Unauthenticated public landing page views.
- **`src/components/dashboard/`**: Authenticated administrative views.
- **`src/lib/api.ts`**: Handles centralized network calls, automatically attaching the JWT Bearer token to headers.
- **`src/lib/validations/`**: Zod schemas used to validate form input client-side.

---

## 3. Backend Folder Structure (`backend/`)

Built using **FastAPI**, **SQLAlchemy 2.0**, **Alembic**, **Pydantic v2**, and **PostgreSQL**.

```
backend/
├── alembic/                  # Alembic database migration management
│   ├── env.py                # Migration environment execution context
│   ├── script.py.mjs         # Migration revision script template
│   └── versions/             # Timestamped database migration scripts
│       └── 0001_initial_schema.py
│
├── app/                      # Main application source module
│   ├── main.py               # FastAPI App instance instantiation & middleware
│   │
│   ├── api/                  # HTTP API Layer
│   │   ├── deps.py           # FastAPI Dependencies (DB session, Auth Guard)
│   │   └── v1/               # Version 1 API Routes
│   │       ├── router.py     # Central Router aggregation
│   │       ├── endpoints/
│   │       │   ├── leads.py  # Lead endpoints (POST /leads, GET /leads, PATCH /status)
│   │       │   ├── auth.py   # Auth endpoints (POST /login, GET /me)
│   │       │   └── health.py # Health check endpoint (GET /health)
│   │
│   ├── core/                 # Infrastructure & Core Configuration
│   │   ├── config.py         # Pydantic BaseSettings (Reads .env variables)
│   │   ├── database.py       # SQLAlchemy engine & SessionLocal factory
│   │   └── security.py       # Password hashing (bcrypt) & JWT issuance/decoding
│   │
│   ├── crud/                 # Data Access Layer (Repository Pattern)
│   │   ├── crud_lead.py      # Lead SQL query operations (create, list, filter, update)
│   │   └── crud_admin.py     # Admin SQL query operations (get_by_email, create)
│   │
│   ├── models/               # SQLAlchemy ORM Database Models
│   │   ├── base.py           # Declarative base model
│   │   ├── lead.py           # Lead SQLAlchemy model definition
│   │   └── admin.py          # Admin SQLAlchemy model definition
│   │
│   └── schemas/              # Pydantic Request / Response Data Contracts
│       ├── lead.py           # LeadCreate, LeadResponse, LeadStatusUpdate schemas
│       ├── auth.py           # Token, LoginRequest, AdminResponse schemas
│       └── common.py         # Standardized API response wrapper schemas
│
├── scripts/                  # Auxiliary operational scripts
│   └── seed_admin.py         # Initial admin creation script
│
├── .env.example              # Template backend environment variables file
├── alembic.ini               # Alembic CLI configuration file
├── pyproject.toml            # Dependencies and linter config (Ruff/Black)
├── requirements.txt          # Python dependencies list for deployment
└── uvicorn_start.sh          # Server startup script for Render deployment
```

### Folder Responsibilities (`backend/`)
- **`app/main.py`**: Initializes the FastAPI application, configures CORS middleware, and mounts API routers.
- **`app/api/`**: Contains HTTP endpoints. Maps request HTTP methods to CRUD service functions.
- **`app/core/`**: Security primitives (bcrypt, JWT verification) and database connection setup.
- **`app/crud/`**: Database operations layer completely detached from HTTP routing logic.
- **`app/models/`**: SQLAlchemy ORM definitions corresponding to PostgreSQL tables.
- **`app/schemas/`**: Pydantic models for request validation and response serialization.
- **`alembic/`**: Version-controlled database migrations.
