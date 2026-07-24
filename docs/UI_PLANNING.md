# UI Planning & Design System — LeadDesk Mini

This document outlines the user interface specifications, design tokens, screen layouts, responsive behavior rules, and state management strategies for **LeadDesk Mini**.

> [!NOTE]
> **Wireframing Process**: Initial visual UI wireframes and visual design prototypes will be generated using **Google Stitch** during the design phase. Those layout concepts will then be manually refined into TailwindCSS code components prior to final implementation.

---

## 1. Design System Tokens

### 1.1 Color Palette (Modern Dark & Light Hybrid)

LeadDesk Mini utilizes a professional, high-contrast Slate and Indigo color palette tailored for enterprise SaaS products.

| Category | Token Name | Hex Code | Usage |
|---|---|---|---|
| **Primary Accent** | `indigo-600` | `#4F46E5` | Primary buttons, active tabs, focus rings |
| **Primary Hover** | `indigo-700` | `#4338CA` | Button hover state |
| **Background Light** | `slate-50` | `#F8FAFC` | App page background |
| **Surface Light** | `slate-0` | `#FFFFFF` | Cards, modal dialogs, data table container |
| **Text Primary** | `slate-900` | `#0F172A` | Primary headings, body copy |
| **Text Secondary** | `slate-500` | `#64748B` | Subheadings, field labels, metadata |
| **Border Neutral** | `slate-200` | `#E2E8F0` | Card borders, table dividers |
| **Status: NEW** | `amber-500 / bg-amber-50` | `#F59E0B` | Badge pill for new leads |
| **Status: CONTACTED**| `blue-500 / bg-blue-50` | `#3B82F6` | Badge pill for contacted leads |
| **Status: CLOSED** | `emerald-500 / bg-emerald-50` | `#10B981` | Badge pill for closed leads |
| **Destructive/Error** | `rose-600 / bg-rose-50` | `#E11D48` | Form error text, delete actions |

### 1.2 Typography System

- **Font Family**: Inter (`var(--font-inter)` via `next/font/google`).
- **Heading Hierarchy**:
  - **`h1` (Hero Headline)**: `text-4xl sm:text-5xl lg:text-6xl`, `font-extrabold`, `tracking-tight`
  - **`h2` (Section Title)**: `text-2xl sm:text-3xl`, `font-bold`, `tracking-tight`
  - **`h3` (Card/Header Title)**: `text-lg sm:text-xl`, `font-semibold`
  - **`Body Text`**: `text-base`, `font-normal`, `leading-relaxed`
  - **`Small / Label`**: `text-sm`, `font-medium`
  - **`Micro / Badge`**: `text-xs`, `font-semibold`, `uppercase`

### 1.3 Spacing & Grid System
- Based on an **8px linear scale** (`p-2` = 8px, `p-4` = 16px, `p-6` = 24px, `p-8` = 32px).
- Maximum layout width constrained to `max-w-7xl` with horizontal padding (`px-4 sm:px-6 lg:px-8`).

---

## 2. Screen Specifications & Layout Hierarchy

### 2.1 Public Landing Page (`/`)

#### Purpose
Capture prospective client inquiries through an engaging, responsive landing interface.

#### Component Layout Hierarchy
```
LandingPage (page.tsx)
├── Navbar (Logo, "Admin Login" Button)
├── HeroSection
│   ├── Badge ("Built for Scaling Teams")
│   ├── Main Heading ("Streamline Your Lead Pipeline")
│   ├── Subheading ("Capture, organize, and close deals faster...")
│   └── CTA Scroll Button ("Submit Inquiry")
├── FeatureGrid (3-card grid: Instant Capture, Status Tracking, Analytics)
├── LeadCaptureSection
│   └── LeadForm (Card Container)
│       ├── Input: Full Name
│       ├── Input: Email Address
│       ├── Select: Budget Range ($1k-$5k, $5k-$15k, $15k-$50k, $50k+)
│       ├── Textarea: Message
│       └── Submit Button (With Loading Spinner)
└── Footer
    └── Attribution Link ("Built for Digital Heroes Training Task" -> https://digitalheroesco.com)
```

---

### 2.2 Admin Login Page (`/login`)

#### Purpose
Secure entry gate for administrators to authenticate with email and password.

#### Component Layout Hierarchy
```
LoginPage (page.tsx)
└── AuthCard (Centered Card Layout)
    ├── Brand Logo & Title ("Admin Portal Login")
    ├── LoginForm
    │   ├── Input: Email Address
    │   ├── Input: Password (With Toggle Show/Hide)
    │   ├── Alert: Error Banner (Rendered if auth fails)
    │   └── Submit Button ("Sign In to Dashboard")
    └── Back to Home Link ("← Return to Public Site")
```

---

### 2.3 Admin Dashboard Page (`/dashboard`)

#### Purpose
Provide authenticated admins with tools to list, search, filter, and update lead statuses.

#### Component Layout Hierarchy
```
DashboardPage (page.tsx)
├── DashboardHeader
│   ├── App Brand Logo
│   ├── Admin Profile Indicator ("Logged in as admin@leaddesk.com")
│   └── Logout Button
└── MainContent Area
    ├── MetricsRow (4 Summary Stat Cards)
    │   ├── Total Leads
    │   ├── New Leads (Amber)
    │   ├── Contacted Leads (Blue)
    │   └── Closed Leads (Green)
    ├── FilterBarCard
    │   ├── SearchInput ("Search by name, email, or message...")
    │   └── StatusFilterTabs ("All", "NEW", "CONTACTED", "CLOSED")
    └── LeadsDataTableCard
        ├── DataTable
        │   ├── Header Row (Name, Email, Budget, Message, Status, Submitted At, Actions)
        │   └── TableRows (Rendered Lead Records)
        │       └── StatusDropdown (Select: NEW | CONTACTED | CLOSED)
        └── PaginationControls (Page indicators, Next/Prev buttons)
```

---

## 3. UI State Handling Specifications

### 3.1 Loading States
- **Landing Page Form Submission**: Submit button transitions to a disabled state with an inline Lucide `Loader2` rotating spinner.
- **Dashboard Table Skeleton**: Renders 5 animated pulses (`<Skeleton />` rows) while lead data is being fetched over the network.

### 3.2 Empty States
- **Zero Leads Submitted**: Renders an empty state illustration/icon with text: `"No leads submitted yet. New inquiries from your landing page will appear here."`
- **Zero Filter Search Results**: Renders text: `"No leads match your current search query or status filter."` with a `"Clear Filters"` button.

### 3.3 Error States
- **Form Input Errors**: Inline red error labels below input fields (`"Please enter a valid email address"`).
- **Network / API Outage**: Top alert toast banner (`"Unable to connect to server. Please try again."`).
- **401 Session Expiry**: Redirects immediately to `/login` with toast notification (`"Your session has expired. Please log in again."`).

---

## 4. Responsive Behavior Rules

| Screen Breakpoint | Target Width | Layout Adaptations |
|---|---|---|
| **Mobile (`< 640px`)** | iPhones, Android | • Landing Hero: Single column stacked text & CTA.<br>• Lead Form: 100% width inputs.<br>• Dashboard Table: Horizontally scrollable container (`overflow-x-auto`) or mobile card stack.<br>• Header: Compact navbar layout. |
| **Tablet (`640px - 1024px`)** | iPads, Tablets | • Feature Grid: 2-column layout.<br>• Stat Cards: 2x2 grid.<br>• Dashboard Table: Standard full table rendering. |
| **Desktop (`> 1024px`)** | Laptops, Monitors | • Feature Grid: 3-column layout.<br>• Stat Cards: 4-column single row layout.<br>• Full width data table with inline action dropdowns. |
