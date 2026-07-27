# LeadDesk Mini Landing UI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor the LeadDesk Mini landing page into a premium pastel SaaS marketing site powered by a semantic design-token system, `next-themes` (Light/Dark/System), and token-only components — without changing architecture, routes, or component names.

**Architecture:** Token-first CSS variables live in `src/styles/design-tokens.css` and are bridged into Tailwind 4 via `@theme inline` in `globals.css`. A client `ThemeProvider` + cycling `ThemeToggle` handle theming. Shared `Surface` primitive standardizes section shells. Existing `common` / `layout` / `sections` components are restyled to consume semantic utilities only.

**Tech Stack:** Next.js 16 (App Router), React 19, Tailwind CSS 4, `next-themes`, `lucide-react`, `next/font/google` (Plus Jakarta Sans + DM Sans)

**Spec:** `docs/superpowers/specs/2026-07-25-leaddesk-landing-ui-design.md`

## Global Constraints

- Components may consume only semantic utilities and design tokens; never define brand styling internally.
- No raw hex / `rgb()` / Tailwind palette colors (`indigo-*`, `slate-*`) in component files.
- Do not change overall architecture, component hierarchy, routes, or rename existing components.
- Allowed additive files only: `design-tokens.css`, `Surface`, `ThemeProvider`, `ThemeToggle`, `useScrollReveal`, and tiny helpers (`lib/theme.ts`).
- No business logic, backend integration, or heavy motion libraries.
- Concrete CTAs must match spec §5.5 exactly.
- Pipeline mockup stages: New Leads → Qualified → Proposal Sent → Won.
- Commit only when the user explicitly requests it (skip plan commit steps unless asked).
- After implementation: mandatory holistic UI review pass before any commit.

---

## File Structure

| File | Responsibility |
|---|---|
| `frontend/src/styles/design-tokens.css` | All CSS custom properties (`:root` + `.dark`) |
| `frontend/src/app/globals.css` | Import tokens, `@theme inline` bridge, element defaults, motion utilities |
| `frontend/src/app/layout.tsx` | Fonts, ThemeProvider, metadata, html/body token classes |
| `frontend/src/app/page.tsx` | Composition only; tokenized page shell |
| `frontend/src/lib/theme.ts` | Pure `cycleTheme` helper |
| `frontend/src/lib/useScrollReveal.ts` | Intersection Observer hook |
| `frontend/src/components/common/ThemeProvider.tsx` | `next-themes` wrapper |
| `frontend/src/components/common/ThemeToggle.tsx` | Light → Dark → System cycle control |
| `frontend/src/components/common/Surface.tsx` | Section/panel shell primitive |
| `frontend/src/types/index.ts` | Add `SurfaceProps`; keep existing props |
| Existing common/layout/sections | Visual restyle only — consume tokens/`Surface` |

---

### Task 1: Install dependencies + design tokens

**Files:**
- Create: `frontend/src/styles/design-tokens.css`
- Modify: `frontend/package.json` (via npm install)
- Test: file exists + build can resolve CSS import (verified in Task 2)

**Interfaces:**
- Consumes: none
- Produces: CSS variables listed in spec §3 (colors, type roles, spacing, layout, opacity, radii, shadows, transitions, z-index, status)

- [ ] **Step 1: Install dependencies**

```bash
cd frontend
npm install next-themes lucide-react
```

Expected: both packages appear in `dependencies`.

- [ ] **Step 2: Create `frontend/src/styles/design-tokens.css`**

```css
/**
 * LeadDesk Mini design tokens — single source of truth.
 * Components must consume semantic utilities bridged from these variables.
 * Never copy hex values into component files.
 */

:root {
  /* Color — light */
  --background: #fbefef;
  --surface: #fff7f6;
  --section: #ffe2e2;
  --card: #fff7f6;
  --accent: #f5cbcb;
  --primary: #c5b3d3;
  --heading: #2d2a32;
  --body: #5e5a66;
  --border: #ebd4d4;
  --muted: #8a8494;
  --ring: #c5b3d3;
  --primary-foreground: #2d2a32;
  --accent-foreground: #2d2a32;
  --overlay: rgba(45, 42, 50, 0.4);

  /* Status — light */
  --success: #7d9b7a;
  --success-foreground: #f5fbf4;
  --warning: #c4a574;
  --warning-foreground: #2d2a32;
  --danger: #c48b8b;
  --danger-foreground: #2d2a32;
  --info: #c5b3d3;
  --info-foreground: #2d2a32;
  --qualified: #b7c4e0;
  --qualified-foreground: #2d2a32;

  /* Type scale — font families bound from next/font on <html> */
  --text-display: clamp(2.5rem, 5vw, 3.75rem);
  --text-h2: clamp(1.75rem, 3vw, 2.5rem);
  --text-h3: 1.25rem;
  --text-body: 1rem;
  --text-body-lg: 1.125rem;
  --text-sm: 0.875rem;
  --text-xs: 0.75rem;
  --leading-display: 1.15;
  --leading-h2: 1.2;
  --leading-h3: 1.3;
  --leading-body: 1.6;
  --leading-sm: 1.5;
  --leading-xs: 1.4;

  /* Spacing */
  --space-section-y: 5rem;
  --space-section-x: 1.5rem;
  --space-stack-sm: 1.5rem;
  --space-stack-md: 2rem;
  --space-stack-lg: 3rem;
  --space-page-gutter: 1rem;

  /* Layout */
  --layout-max-width: 80rem;
  --layout-nav-height: 4rem;
  --layout-nav-inset: 1rem;
  --layout-hero-text: 45%;
  --layout-hero-media: 55%;
  --layout-section-gap: 2rem;

  /* Opacity */
  --opacity-subtle: 0.04;
  --opacity-muted: 0.08;
  --opacity-soft: 0.16;
  --opacity-medium: 0.4;
  --opacity-navbar: 0.72;
  --opacity-navbar-scrolled: 0.88;
  --opacity-blob: 0.35;
  --opacity-disabled: 0.5;

  /* Radius */
  --radius-2xl: 1rem;
  --radius-3xl: 1.5rem;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(45, 42, 50, 0.06);
  --shadow-md: 0 8px 24px rgba(45, 42, 50, 0.08);
  --shadow-lg: 0 16px 40px rgba(45, 42, 50, 0.12);

  /* Motion */
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --ease-standard: cubic-bezier(0.4, 0, 0.2, 1);

  /* Z-index */
  --z-nav: 50;
  --z-overlay: 100;
  --z-toast: 200;
}

@media (min-width: 640px) {
  :root {
    --space-section-y: 6rem;
    --space-section-x: 2rem;
    --space-page-gutter: 1.5rem;
  }
}

@media (min-width: 1024px) {
  :root {
    --space-section-x: 2.5rem;
    --space-page-gutter: 2rem;
  }
}

.dark {
  --background: #221d2e;
  --surface: #302740;
  --section: #3b324d;
  --card: #3b324d;
  --accent: #f5cbcb;
  --primary: #c5b3d3;
  --heading: #f7f3fa;
  --body: #d8cce6;
  --border: #4a415c;
  --muted: #a99bbb;
  --ring: #c5b3d3;
  --primary-foreground: #221d2e;
  --accent-foreground: #221d2e;
  --overlay: rgba(34, 29, 46, 0.6);

  --success: #9bb896;
  --success-foreground: #1a2419;
  --warning: #d4b88a;
  --warning-foreground: #221d2e;
  --danger: #d4a0a0;
  --danger-foreground: #221d2e;
  --info: #c5b3d3;
  --info-foreground: #221d2e;
  --qualified: #c5d0ea;
  --qualified-foreground: #221d2e;

  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.25);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.35);
  --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.45);
}

/* Theme color transitions only */
html {
  color-scheme: light;
}

html.dark {
  color-scheme: dark;
}

html,
body {
  transition:
    background-color var(--duration-base) var(--ease-standard),
    color var(--duration-base) var(--ease-standard),
    border-color var(--duration-base) var(--ease-standard);
}
```

- [ ] **Step 3: Verify file is present**

```bash
Test-Path frontend/src/styles/design-tokens.css
```

Expected: `True`

---

### Task 2: Bridge tokens in globals.css + fonts + metadata + ThemeProvider shell

**Files:**
- Modify: `frontend/src/app/globals.css`
- Modify: `frontend/src/app/layout.tsx`
- Create: `frontend/src/components/common/ThemeProvider.tsx`
- Create: `frontend/src/lib/theme.ts`
- Test: `frontend` build / lint

**Interfaces:**
- Consumes: tokens from Task 1; `SITE_CONFIG` from `@/lib/constants`
- Produces:
  - `ThemeProvider({ children: React.ReactNode })`
  - `cycleTheme(theme: "light" | "dark" | "system"): "light" | "dark" | "system"`
  - Tailwind semantic colors: `background`, `surface`, `section`, `card`, `accent`, `primary`, `heading`, `body`, `border`, `muted`, `ring`, status tokens, etc.

- [ ] **Step 1: Write `frontend/src/lib/theme.ts`**

```ts
export type ThemeMode = "light" | "dark" | "system";

const ORDER: ThemeMode[] = ["light", "dark", "system"];

export function cycleTheme(current: ThemeMode | undefined): ThemeMode {
  const index = ORDER.indexOf(current ?? "system");
  return ORDER[(index + 1) % ORDER.length];
}
```

- [ ] **Step 2: Verify cycle with Node**

```bash
cd frontend
node --input-type=module -e "import { cycleTheme } from './src/lib/theme.ts'; const a=['light','dark','system'].reduce((t)=>cycleTheme(t),'system'); if(cycleTheme('light')!=='dark'||cycleTheme('dark')!=='system'||cycleTheme('system')!=='light') process.exit(1); console.log('ok');"
```

If TS import fails under plain node, run equivalent asserts via `npx tsx` or temporarily duplicate the one-liner logic in the `-e` script. Expected: `ok`.

- [ ] **Step 3: Replace `frontend/src/app/globals.css`**

```css
@import "tailwindcss";
@import "../styles/design-tokens.css";

@theme inline {
  --color-background: var(--background);
  --color-surface: var(--surface);
  --color-section: var(--section);
  --color-card: var(--card);
  --color-accent: var(--accent);
  --color-primary: var(--primary);
  --color-heading: var(--heading);
  --color-body: var(--body);
  --color-border: var(--border);
  --color-muted: var(--muted);
  --color-ring: var(--ring);
  --color-primary-foreground: var(--primary-foreground);
  --color-accent-foreground: var(--accent-foreground);
  --color-overlay: var(--overlay);
  --color-success: var(--success);
  --color-success-foreground: var(--success-foreground);
  --color-warning: var(--warning);
  --color-warning-foreground: var(--warning-foreground);
  --color-danger: var(--danger);
  --color-danger-foreground: var(--danger-foreground);
  --color-info: var(--info);
  --color-info-foreground: var(--info-foreground);
  --color-qualified: var(--qualified);
  --color-qualified-foreground: var(--qualified-foreground);

  --font-sans: var(--font-sans);
  --font-heading: var(--font-heading);

  --radius-2xl: var(--radius-2xl);
  --radius-3xl: var(--radius-3xl);

  --shadow-sm: var(--shadow-sm);
  --shadow-md: var(--shadow-md);
  --shadow-lg: var(--shadow-lg);

  --ease-standard: var(--ease-standard);
  --default-transition-duration: var(--duration-base);
}

@layer base {
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-family: var(--font-heading), ui-sans-serif, system-ui, sans-serif;
    color: var(--heading);
  }

  body {
    font-family: var(--font-sans), ui-sans-serif, system-ui, sans-serif;
    background: var(--background);
    color: var(--body);
  }

  h1 {
    font-size: var(--text-display);
    line-height: var(--leading-display);
    font-weight: 700;
    letter-spacing: -0.02em;
  }

  h2 {
    font-size: var(--text-h2);
    line-height: var(--leading-h2);
    font-weight: 700;
    letter-spacing: -0.02em;
  }

  h3 {
    font-size: var(--text-h3);
    line-height: var(--leading-h3);
    font-weight: 600;
  }

  *:focus-visible {
    outline: 2px solid var(--ring);
    outline-offset: 2px;
  }
}

@layer utilities {
  .reveal {
    opacity: 0;
    transform: translateY(0.75rem);
    transition:
      opacity var(--duration-base) var(--ease-standard),
      transform var(--duration-base) var(--ease-standard);
  }

  .reveal-visible {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  html,
  body,
  .reveal {
    transition: none !important;
    transform: none !important;
  }

  .reveal {
    opacity: 1;
  }
}
```

- [ ] **Step 4: Create `ThemeProvider.tsx`**

```tsx
"use client";

import { ThemeProvider as NextThemesProvider } from "next-themes";
import { ReactNode } from "react";

export function ThemeProvider({ children }: { children: ReactNode }) {
  return (
    <NextThemesProvider attribute="class" defaultTheme="system" enableSystem>
      {children}
    </NextThemesProvider>
  );
}
```

- [ ] **Step 5: Update `layout.tsx`**

```tsx
import type { Metadata } from "next";
import { DM_Sans, Plus_Jakarta_Sans } from "next/font/google";
import { ThemeProvider } from "@/components/common/ThemeProvider";
import { SITE_CONFIG } from "@/lib/constants";
import "./globals.css";

const plusJakarta = Plus_Jakarta_Sans({
  subsets: ["latin"],
  variable: "--font-heading",
  display: "swap",
});

const dmSans = DM_Sans({
  subsets: ["latin"],
  variable: "--font-sans",
  display: "swap",
});

export const metadata: Metadata = {
  title: `${SITE_CONFIG.name} — Modern Lead Management`,
  description: SITE_CONFIG.description,
  applicationName: SITE_CONFIG.name,
  robots: { index: true, follow: true },
  openGraph: {
    title: `${SITE_CONFIG.name} — Modern Lead Management`,
    description: SITE_CONFIG.description,
    type: "website",
    siteName: SITE_CONFIG.name,
  },
  twitter: {
    card: "summary_large_image",
    title: `${SITE_CONFIG.name} — Modern Lead Management`,
    description: SITE_CONFIG.description,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      suppressHydrationWarning
      className={`${plusJakarta.variable} ${dmSans.variable} h-full scroll-smooth antialiased`}
    >
      <body className="flex min-h-full flex-col bg-background font-sans text-body">
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  );
}
```

- [ ] **Step 6: Verify build**

```bash
cd frontend
npm run lint
npm run build
```

Expected: lint clean (or only pre-existing unrelated warnings); build succeeds.

---

### Task 3: ThemeToggle + Surface + types

**Files:**
- Create: `frontend/src/components/common/ThemeToggle.tsx`
- Create: `frontend/src/components/common/Surface.tsx`
- Modify: `frontend/src/types/index.ts`
- Test: `npm run lint` / `npm run build`

**Interfaces:**
- Consumes: `cycleTheme` from `@/lib/theme`; tokens via utilities
- Produces:
  - `ThemeToggle()` — client button, no required props
  - `SurfaceProps`: `{ children, variant?: "section" | "surface" | "accent" | "transparent", className?, as?: ElementType, hover?: boolean }`
  - `Surface(props: SurfaceProps)`

- [ ] **Step 1: Extend `types/index.ts` with SurfaceProps**

Add:

```ts
export interface SurfaceProps {
  children: ReactNode;
  variant?: "section" | "surface" | "accent" | "transparent";
  className?: string;
  as?: ElementType;
  hover?: boolean;
}
```

Keep all existing interfaces unchanged.

- [ ] **Step 2: Create `Surface.tsx`**

```tsx
import { SurfaceProps } from "@/types";
import { cn } from "@/lib/utils";

const variantStyles = {
  section: "bg-section border border-border shadow-sm",
  surface: "bg-surface border border-border shadow-sm",
  accent: "bg-section border border-border shadow-md",
  transparent: "bg-transparent border-transparent shadow-none",
} as const;

export function Surface({
  children,
  variant = "section",
  className,
  as: Component = "div",
  hover = false,
}: SurfaceProps) {
  return (
    <Component
      className={cn(
        "rounded-3xl",
        variantStyles[variant],
        hover &&
          "transition-[box-shadow,transform] duration-[var(--duration-base)] ease-[var(--ease-standard)] hover:-translate-y-0.5 hover:shadow-md",
        className
      )}
    >
      {children}
    </Component>
  );
}
```

- [ ] **Step 3: Create `ThemeToggle.tsx`**

```tsx
"use client";

import { useTheme } from "next-themes";
import { useEffect, useState } from "react";
import { Monitor, Moon, Sun } from "lucide-react";
import { cycleTheme, type ThemeMode } from "@/lib/theme";
import { cn } from "@/lib/utils";

const ICONS = {
  light: Sun,
  dark: Moon,
  system: Monitor,
} as const;

const LABELS = {
  light: "Light",
  dark: "Dark",
  system: "System",
} as const;

export function ThemeToggle() {
  const { theme, setTheme, resolvedTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const mode = (theme as ThemeMode | undefined) ?? "system";
  const Icon = mounted ? ICONS[mode] : Monitor;

  return (
    <button
      type="button"
      aria-label={`Theme: ${LABELS[mode]}. Click to switch to ${LABELS[cycleTheme(mode)]}`}
      onClick={() => setTheme(cycleTheme(mode))}
      className={cn(
        "inline-flex h-9 w-9 items-center justify-center rounded-full border border-border bg-surface text-heading",
        "transition-colors duration-[var(--duration-fast)] ease-[var(--ease-standard)]",
        "hover:bg-accent focus-visible:outline-none"
      )}
    >
      <Icon className="h-4 w-4" aria-hidden="true" />
      <span className="sr-only">
        {mounted
          ? `${LABELS[mode]} theme (resolved ${resolvedTheme})`
          : "Theme"}
      </span>
    </button>
  );
}
```

If `sr-only` is unavailable under Tailwind 4 defaults, use `className="absolute w-px h-px overflow-hidden whitespace-nowrap clip-[rect(0,0,0,0)]"` or add a tokenized utility in globals. Prefer Tailwind’s built-in `sr-only` when present.

- [ ] **Step 4: Lint + build**

```bash
cd frontend
npm run lint
npm run build
```

Expected: success.

---

### Task 4: Restyle shared common components

**Files:**
- Modify: `frontend/src/components/common/Button.tsx`
- Modify: `frontend/src/components/common/Card.tsx`
- Modify: `frontend/src/components/common/Badge.tsx`
- Modify: `frontend/src/components/common/SectionHeading.tsx`
- Modify: `frontend/src/components/common/Logo.tsx`
- Test: `npm run lint` / `npm run build`

**Interfaces:**
- Consumes: existing prop types; `Surface` optional for Card alignment
- Produces: same exports/names; token-only classNames

- [ ] **Step 1: Update Button variants to tokens**

Replace variant/size styles with:

```tsx
  const baseStyles =
    "inline-flex items-center justify-center font-semibold rounded-full transition-all duration-[var(--duration-base)] ease-[var(--ease-standard)] focus-visible:outline-none disabled:pointer-events-none disabled:opacity-[var(--opacity-disabled)] active:scale-[0.98]";

  const variantStyles = {
    primary:
      "bg-primary text-primary-foreground shadow-sm hover:opacity-90",
    secondary:
      "bg-heading text-background shadow-sm hover:opacity-90",
    outline:
      "border border-border bg-surface text-heading shadow-sm hover:bg-accent",
  };

  const sizeStyles = {
    sm: "px-3 py-1.5 text-xs",
    md: "px-4 py-2 text-sm",
    lg: "px-5 py-2.5 text-base",
  };
```

No indigo/slate classes remain.

- [ ] **Step 2: Update Card to token shell**

```tsx
export function Card({ title, description, icon, children, className }: CardProps) {
  return (
    <div
      className={cn(
        "rounded-3xl border border-border bg-card p-6 shadow-sm",
        "transition-[box-shadow,transform] duration-[var(--duration-base)] ease-[var(--ease-standard)]",
        "hover:-translate-y-0.5 hover:shadow-md",
        className
      )}
    >
      {icon && (
        <div className="mb-4 inline-flex h-10 w-10 items-center justify-center rounded-2xl bg-primary text-primary-foreground">
          {icon}
        </div>
      )}
      {title && <h3 className="text-heading">{title}</h3>}
      {description && (
        <p className="mt-2 text-sm leading-[var(--leading-body)] text-body">
          {description}
        </p>
      )}
      {children && <div className="mt-4">{children}</div>}
    </div>
  );
}
```

- [ ] **Step 3: Update Badge**

```tsx
  const variantStyles = {
    default: "bg-primary/20 text-heading ring-1 ring-inset ring-primary/30",
    outline: "bg-surface text-body ring-1 ring-inset ring-border",
    success: "bg-success/20 text-heading ring-1 ring-inset ring-success/40",
  };
```

Keep structure; ensure `rounded-full`, `text-xs`, etc. remain token-friendly.

- [ ] **Step 4: Update SectionHeading**

```tsx
      {eyebrow && <Badge>{eyebrow}</Badge>}
      <h2>{title}</h2>
      {description && (
        <p className="text-lg leading-[var(--leading-body)] text-body">
          {description}
        </p>
      )}
```

Wrapper keeps alignment utilities; remove slate/dark: color classes.

- [ ] **Step 5: Update Logo**

```tsx
      className={cn(
        "flex items-center gap-2 text-xl font-extrabold tracking-tight text-heading transition-opacity hover:opacity-90",
        className
      )}
...
      <span className="flex h-8 w-8 items-center justify-center rounded-2xl bg-primary text-sm font-bold text-primary-foreground shadow-sm">
        LM
      </span>
```

- [ ] **Step 6: Grep for forbidden raw colors in common/**

```bash
cd frontend
rg -n "indigo-|slate-|#[0-9A-Fa-f]{3,8}|rgb\(" src/components/common
```

Expected: no matches (except possibly comments).

- [ ] **Step 7: Lint + build**

```bash
npm run lint
npm run build
```

---

### Task 5: Layout components (Container, Navbar, Footer)

**Files:**
- Modify: `frontend/src/components/layout/Container.tsx`
- Modify: `frontend/src/components/layout/Navbar.tsx`
- Modify: `frontend/src/components/layout/Footer.tsx`
- Create: `frontend/src/lib/useScrollReveal.ts` (also used by sections in Task 6–7; create here if Navbar needs scroll state separately)
- Test: manual navbar scroll + theme toggle; `npm run build`

**Interfaces:**
- Consumes: `ThemeToggle`, layout tokens, `NAV_ITEMS`, `Button`, `Logo`
- Produces: scroll-aware Navbar; tokenized Footer/Container

- [ ] **Step 1: Update Container**

```tsx
    <Component
      className={cn(
        "mx-auto w-full max-w-[var(--layout-max-width)] px-[var(--space-page-gutter)]",
        className
      )}
    >
```

- [ ] **Step 2: Implement floating Navbar with scroll transition + ThemeToggle**

Navbar must be a client component (or extract a thin client `NavbarBar` child). Preferred: mark `Navbar.tsx` as `"use client"` since it needs scroll + theme.

```tsx
"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Container } from "./Container";
import { Logo } from "@/components/common/Logo";
import { Button } from "@/components/common/Button";
import { ThemeToggle } from "@/components/common/ThemeToggle";
import { NAV_ITEMS } from "@/lib/navigation";
import { cn } from "@/lib/utils";

export function Navbar() {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      className="sticky top-0 z-[var(--z-nav)] w-full"
      style={{ padding: "var(--layout-nav-inset)" }}
    >
      <Container className="px-0 sm:px-0 lg:px-0">
        <div
          className={cn(
            "flex items-center justify-between gap-4 rounded-2xl border px-4 backdrop-blur-md",
            "transition-[background-color,box-shadow,border-color,opacity] duration-[var(--duration-base)] ease-[var(--ease-standard)]",
            scrolled
              ? "border-border bg-surface/90 shadow-lg"
              : "border-border/60 bg-surface/70 shadow-none"
          )}
          style={{
            minHeight: "var(--layout-nav-height)",
            backgroundColor: scrolled
              ? undefined
              : undefined,
          }}
        >
          <Logo />
          <nav aria-label="Main Navigation" className="hidden items-center gap-8 md:flex">
            {NAV_ITEMS.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="text-sm font-medium text-body transition-colors hover:text-heading"
              >
                {item.label}
              </Link>
            ))}
          </nav>
          <div className="flex items-center gap-3">
            <ThemeToggle />
            <Button href="/login" variant="primary" size="sm">
              Admin Login
            </Button>
          </div>
        </div>
      </Container>
    </header>
  );
}
```

**Important:** Prefer opacity tokens for navbar fill. If `/70` `/90` arbitrary alphas appear, map to CSS like `background: color-mix(in srgb, var(--surface) calc(var(--opacity-navbar) * 100%), transparent)` via a utility class in `globals.css`:

```css
.navbar-shell {
  background: color-mix(
    in srgb,
    var(--surface) calc(var(--opacity-navbar) * 100%),
    transparent
  );
}
.navbar-shell-scrolled {
  background: color-mix(
    in srgb,
    var(--surface) calc(var(--opacity-navbar-scrolled) * 100%),
    transparent
  );
}
```

Use those classes instead of inventing opacity in the component.

- [ ] **Step 3: Update Footer to tokens**

Replace all `slate`/`indigo` with `border-border`, `bg-surface`, `text-body`, `text-muted`, `text-primary`, etc. Preserve attribution link and year logic.

- [ ] **Step 4: Build + manual check**

```bash
npm run build
npm run dev
```

Manual: scroll page → navbar opacity/shadow/border change; click theme toggle three times → Light/Dark/System icons cycle and persist after refresh.

---

### Task 6: Hero — 45/55, blobs, pipeline mockup, trust strip, CTAs

**Files:**
- Modify: `frontend/src/components/sections/Hero.tsx`
- Test: visual + `npm run build`

**Interfaces:**
- Consumes: `Container`, `Surface`, `Button`, `SECTION_IDS`, layout tokens
- Produces: Hero with trust strip; decorative mockup `aria-hidden`

- [ ] **Step 1: Rewrite Hero per spec**

Structure (normative):

```tsx
<section id={id} className={cn("pt-[var(--layout-section-gap)]", className)}>
  <Container>
    <Surface variant="accent" className="relative overflow-hidden p-[var(--space-section-x)] py-[var(--space-section-y)]">
      {/* blobs: absolute, blurred, pointer-events-none, aria-hidden, opacity token */}
      <div className="relative grid items-center gap-[var(--space-stack-lg)] lg:grid-cols-[var(--layout-hero-text)_var(--layout-hero-media)]">
        <div>
          <p className="text-sm font-semibold text-heading">LeadDesk Mini</p>
          <h1 className="mt-4">Capture, organize, and close leads without the clutter</h1>
          <p className="mt-6 text-[length:var(--text-body-lg)] leading-[var(--leading-body)] text-body">
            A calm pipeline for growing teams to capture inquiries and move deals from first touch to won.
          </p>
          <div className="mt-8 flex flex-wrap gap-4">
            <Button href={`#${SECTION_IDS.contact}`} variant="primary" size="lg">
              Start free inquiry
            </Button>
            <Button href={`#${SECTION_IDS.howItWorks}`} variant="outline" size="lg">
              See how it works
            </Button>
          </div>
        </div>
        {/* Pipeline mockup: New Leads / Qualified / Proposal Sent / Won */}
        <div aria-hidden="true" className="...">
          {/* window chrome + 4 columns using bg-info, bg-qualified, bg-warning, bg-success tags */}
        </div>
      </div>
    </Surface>

    {/* Trust strip */}
    <ul className="mt-[var(--space-stack-md)] flex flex-wrap items-center justify-center gap-3 text-sm text-muted">
      <li>Secure</li>
      <li aria-hidden="true">·</li>
      <li>Fast</li>
      <li aria-hidden="true">·</li>
      <li>Production-ready</li>
    </ul>
  </Container>
</section>
```

Blob implementation must use tokenized colors (e.g. `bg-primary`, `bg-accent`) + `opacity-[var(--opacity-blob)]` or a utility class — not raw hex gradients in JSX. Prefer utility classes in `globals.css`:

```css
.hero-blob-primary {
  background: var(--primary);
  opacity: var(--opacity-blob);
}
.hero-blob-accent {
  background: var(--accent);
  opacity: var(--opacity-blob);
}
```

- [ ] **Step 2: Build + visual check**

```bash
npm run build
```

Manual: desktop shows ~45/55; mobile stacks text then mockup; blobs clipped; mockup stages labeled correctly; CTAs match §5.5.

---

### Task 7: Remaining sections + page shell + scroll reveal

**Files:**
- Create: `frontend/src/lib/useScrollReveal.ts` (if not created earlier)
- Modify: `frontend/src/components/sections/Features.tsx`
- Modify: `frontend/src/components/sections/WhyChooseUs.tsx`
- Modify: `frontend/src/components/sections/HowItWorks.tsx`
- Modify: `frontend/src/components/sections/CTA.tsx`
- Modify: `frontend/src/components/sections/Contact.tsx`
- Modify: `frontend/src/app/page.tsx`
- Test: `npm run build`; reduced-motion check

**Interfaces:**
- Consumes: `Surface`, `Card`, `SectionHeading`, `Button`, `useScrollReveal`
- Produces: tokenized sections; page `bg-background`

- [ ] **Step 1: Create `useScrollReveal.ts`**

```ts
"use client";

import { useEffect, useRef } from "react";

export function useScrollReveal<T extends HTMLElement>() {
  const ref = useRef<T | null>(null);

  useEffect(() => {
    const node = ref.current;
    if (!node) return;

    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce) {
      node.classList.add("reveal-visible");
      return;
    }

    node.classList.add("reveal");
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          node.classList.add("reveal-visible");
          observer.unobserve(node);
        }
      },
      { threshold: 0.15 }
    );
    observer.observe(node);
    return () => observer.disconnect();
  }, []);

  return ref;
}
```

Because section components are currently Server Components, either:
- keep sections as server components and wrap content in a tiny client `Reveal` component, **or**
- mark section files `"use client"` only when using the hook.

**Preferred (minimal client surface):** create `components/common/Reveal.tsx`:

```tsx
"use client";

import { ReactNode } from "react";
import { useScrollReveal } from "@/lib/useScrollReveal";
import { cn } from "@/lib/utils";

export function Reveal({ children, className }: { children: ReactNode; className?: string }) {
  const ref = useScrollReveal<HTMLDivElement>();
  return (
    <div ref={ref} className={cn(className)}>
      {children}
    </div>
  );
}
```

This additive file is allowed as part of scroll-reveal support (same intent as `useScrollReveal`).

- [ ] **Step 2: Update Features**

Wrap with `Container` → `Reveal` → `Surface variant="section"` → `SectionHeading` + Card grid. Remove `bg-slate-*`. Use `py` / `mt` from spacing tokens.

- [ ] **Step 3: Update WhyChooseUs**

Three value props via `Card` (e.g. Clean architecture, Fast performance, Reliable processing). Inside `Surface`.

- [ ] **Step 4: Update HowItWorks**

Three steps using `Card` or tokenized step blocks; step numbers `text-primary` not indigo.

- [ ] **Step 5: Update CTA**

```tsx
<Surface variant="accent" className="px-[var(--space-section-x)] py-[var(--space-section-y)] text-center">
  <h2>Ready to take control of your lead pipeline?</h2>
  <p className="mt-4 text-body">Start capturing qualified inquiries today with LeadDesk Mini.</p>
  <div className="mt-8 flex flex-wrap justify-center gap-4">
    <Button href={`#${SECTION_IDS.contact}`} variant="primary" size="lg">
      Submit an inquiry
    </Button>
    <Button href="/login" variant="outline" size="lg">
      Open admin portal
    </Button>
  </div>
</Surface>
```

- [ ] **Step 6: Update Contact**

Tokenized `Surface variant="surface"` placeholder form shell; button label **Send inquiry** (disabled or non-functional visual only).

- [ ] **Step 7: Update `page.tsx`**

```tsx
<div className="flex min-h-screen flex-col bg-background text-body">
  <Navbar />
  <main className="flex-1">{/* same sections */}</main>
  <Footer />
</div>
```

- [ ] **Step 8: Repo-wide forbidden color grep**

```bash
cd frontend
rg -n "indigo-|slate-|#[0-9A-Fa-f]{3,8}|rgb\(|rgba\(" src/components src/app/page.tsx src/app/layout.tsx
```

Expected: no matches in components/page/layout (hex/`rgba` allowed only in `src/styles/design-tokens.css`).

- [ ] **Step 9: Final build**

```bash
npm run lint
npm run build
```

Expected: success. Confirm First Load JS stays reasonable (no unexpected heavy deps).

---

### Task 8: Holistic UI review pass (mandatory before commit)

**Files:** none new — review only

- [ ] **Step 1: Run checklist from spec §8**

Verify every checkbox in `docs/superpowers/specs/2026-07-25-leaddesk-landing-ui-design.md` §8, including:

- Token-only components / no internal brand styling
- Tokens in `design-tokens.css`
- `Surface` used for section shells
- Theme cycle + persistence + system
- Pipeline stages correct
- CTA labels exact
- Metadata present (view page source / Next metadata)
- Reduced motion respected
- Responsive navbar/hero/pipeline/footer
- Focus states visible in both themes

- [ ] **Step 2: Fix any review findings**

Re-run `npm run lint` && `npm run build` after fixes.

- [ ] **Step 3: Stop for user commit approval**

Do **not** commit unless the user explicitly asks. Summarize what changed and request commit permission.

---

## Spec coverage self-review

| Spec area | Task(s) |
|---|---|
| Golden rules / token-only | Global + Tasks 1–7 grep gates |
| `design-tokens.css` + layout/opacity | Task 1 |
| `@theme` bridge, fonts, metadata | Task 2 |
| next-themes Light/Dark/System cycle | Tasks 2–3, 5 |
| Surface shell | Tasks 3, 6–7 |
| Navbar floating rounded-2xl + scroll | Task 5 |
| Hero 45/55, blobs, pipeline, trust, CTAs | Task 6 |
| Features / Why / How / CTA / Contact | Task 7 |
| SEO & metadata | Task 2 |
| Performance budget | Tasks 1–2 deps only; Task 7 build check |
| UI review before commit | Task 8 |

## Placeholder scan

No TBD/TODO left in tasks. Commit steps deferred to explicit user request per repo rules.

## Type consistency

- `ThemeMode` + `cycleTheme` defined in Task 1/2, consumed by ThemeToggle Task 3
- `SurfaceProps` / variants aligned across Tasks 3, 6, 7
- CTA strings match spec §5.5 in Tasks 5–7
