# REST API Specification & Contract — LeadDesk Mini

This document serves as the official REST API specification for **LeadDesk Mini**. All request payloads and response bodies adhere strictly to JSON (`Content-Type: application/json`).

---

## 1. Base API Information
- **Base Production URL**: `https://leaddesk-api.onrender.com`
- **Base Local URL**: `http://localhost:8000`
- **API Version Segment**: `/api/v1`
- **Interactive OpenAPI Documentation**: `/docs` (Swagger UI) & `/redoc` (ReDoc UI)

---

## 2. Global Error Response Schema

All error responses return a standardized JSON structure:

```json
{
  "success": false,
  "error": {
    "code": "UNAUTHORIZED_ACCESS",
    "message": "Invalid or expired authentication token",
    "details": null,
    "timestamp": "2026-07-24T18:30:00Z"
  }
}
```

### Standard HTTP Status Codes

| Code | Status | Meaning |
|---|---|---|
| `200 OK` | Success | Request succeeded and returned requested data. |
| `201 Created` | Created | Resource successfully created (e.g. Lead submitted). |
| `400 Bad Request` | Client Error | Malformed request or business logic failure. |
| `401 Unauthorized` | Auth Error | Missing, invalid, or expired JWT Bearer token. |
| `404 Not Found` | Resource Error | Requested Lead ID or endpoint does not exist. |
| `422 Unprocessable` | Schema Error | Validation error on incoming JSON request body. |
| `500 Server Error` | System Error | Unexpected internal backend error. |

---

## 3. Endpoints Breakdown

### 3.1 Public Lead Submission

#### `POST /api/v1/leads`
- **Purpose**: Accepts and stores a public business lead submission from the landing page.
- **Authentication Required**: `No` (Public Endpoint)
- **Request Headers**: `Content-Type: application/json`

#### Request Body Schema (Pydantic / Zod)
| Field | Type | Required | Validation Rules |
|---|---|---|---|
| `name` | String | Yes | Min length 2, Max length 100 |
| `email` | String | Yes | Valid email format (RFC 5322) |
| `budget_range` | String | Yes | Enum: `"$1k - $5k"`, `"$5k - $15k"`, `"$15k - $50k"`, `"$50k+"` |
| `message` | String | Yes | Min length 10, Max length 1000 |

#### Example Request
```bash
curl -X POST "https://leaddesk-api.onrender.com/api/v1/leads" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "budget_range": "$5k - $15k",
    "message": "We need a custom lead management portal built within 4 weeks."
  }'
```

#### Example Response (`201 Created`)
```json
{
  "success": true,
  "data": {
    "id": "e4b8a1c9-8d3f-42e1-91a0-123456789abc",
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "budget_range": "$5k - $15k",
    "message": "We need a custom lead management portal built within 4 weeks.",
    "status": "NEW",
    "created_at": "2026-07-24T18:35:10.123Z",
    "updated_at": "2026-07-24T18:35:10.123Z"
  }
}
```

#### Possible Errors
- `422 Unprocessable Entity`: Invalid email format or message length < 10 characters.

---

### 3.2 Admin Login

#### `POST /api/v1/auth/login`
- **Purpose**: Authenticates administrator credentials and returns a signed JWT access token.
- **Authentication Required**: `No`
- **Request Headers**: `Content-Type: application/json`

#### Request Body Schema
| Field | Type | Required | Description |
|---|---|---|---|
| `email` | String | Yes | Admin registered email address |
| `password` | String | Yes | Plaintext password to compare against bcrypt hash |

#### Example Request
```bash
curl -X POST "https://leaddesk-api.onrender.com/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@leaddesk.com",
    "password": "SuperSecretAdminPassword123!"
  }'
```

#### Example Response (`200 OK`)
```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer",
    "expires_in": 86400,
    "user": {
      "id": "b3191f6a-40a2-4a25-83e9-987654321fed",
      "email": "admin@leaddesk.com"
    }
  }
}
```

#### Possible Errors
- `401 Unauthorized`: Invalid email or password credentials.

---

### 3.3 Admin List & Search Leads

#### `GET /api/v1/leads`
- **Purpose**: Retrieves a paginated list of leads with optional search and status filtering.
- **Authentication Required**: `Yes` (`Authorization: Bearer <token>`)
- **Query Parameters**:
  - `status` (Optional): Filter by `NEW`, `CONTACTED`, or `CLOSED`.
  - `search` (Optional): Search string matching `name`, `email`, or `message`.
  - `page` (Optional, Default: `1`): Page index.
  - `limit` (Optional, Default: `20`, Max: `100`): Page size limit.

#### Example Request
```bash
curl -X GET "https://leaddesk-api.onrender.com/api/v1/leads?status=NEW&search=Jane&page=1&limit=20" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6..."
```

#### Example Response (`200 OK`)
```json
{
  "success": true,
  "data": [
    {
      "id": "e4b8a1c9-8d3f-42e1-91a0-123456789abc",
      "name": "Jane Doe",
      "email": "jane.doe@example.com",
      "budget_range": "$5k - $15k",
      "message": "We need a custom lead management portal built within 4 weeks.",
      "status": "NEW",
      "created_at": "2026-07-24T18:35:10.123Z",
      "updated_at": "2026-07-24T18:35:10.123Z"
    }
  ],
  "meta": {
    "total": 1,
    "page": 1,
    "limit": 20,
    "total_pages": 1
  }
}
```

#### Possible Errors
- `401 Unauthorized`: Missing or invalid Bearer token.

---

### 3.4 Update Lead Status

#### `PATCH /api/v1/leads/{id}/status`
- **Purpose**: Updates the processing status of a specific lead record.
- **Authentication Required**: `Yes` (`Authorization: Bearer <token>`)
- **Path Parameter**: `id` (UUID string)

#### Request Body Schema
| Field | Type | Required | Allowed Values |
|---|---|---|---|
| `status` | String | Yes | `NEW`, `CONTACTED`, `CLOSED` |

#### Example Request
```bash
curl -X PATCH "https://leaddesk-api.onrender.com/api/v1/leads/e4b8a1c9-8d3f-42e1-91a0-123456789abc/status" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6..." \
  -H "Content-Type: application/json" \
  -d '{
    "status": "CONTACTED"
  }'
```

#### Example Response (`200 OK`)
```json
{
  "success": true,
  "data": {
    "id": "e4b8a1c9-8d3f-42e1-91a0-123456789abc",
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "budget_range": "$5k - $15k",
    "message": "We need a custom lead management portal built within 4 weeks.",
    "status": "CONTACTED",
    "created_at": "2026-07-24T18:35:10.123Z",
    "updated_at": "2026-07-24T18:42:00.456Z"
  }
}
```

#### Possible Errors
- `401 Unauthorized`: Invalid Bearer token.
- `404 Not Found`: No lead exists with the specified UUID.
- `422 Unprocessable Entity`: Status value is not one of `NEW`, `CONTACTED`, `CLOSED`.

---

### 3.5 Check Current Admin Profile

#### `GET /api/v1/auth/me`
- **Purpose**: Verifies token validity and returns current authenticated admin details.
- **Authentication Required**: `Yes` (`Authorization: Bearer <token>`)

#### Example Response (`200 OK`)
```json
{
  "success": true,
  "data": {
    "id": "b3191f6a-40a2-4a25-83e9-987654321fed",
    "email": "admin@leaddesk.com",
    "created_at": "2026-07-24T12:00:00.000Z"
  }
}
```

---

### 3.6 System Health Check

#### `GET /api/v1/health`
- **Purpose**: Ping endpoint for Render health checks and uptime monitoring.
- **Authentication Required**: `No`

#### Example Response (`200 OK`)
```json
{
  "status": "healthy",
  "database": "connected",
  "timestamp": "2026-07-24T18:50:00Z"
}
```
