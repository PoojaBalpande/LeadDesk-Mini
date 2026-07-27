# LeadDesk Mini — Landing Page UI & Design System Spec

**Date:** 2026-07-25  
**Status:** Ready to implement  
**Scope:** Visual design, theming, and UX polish of the existing marketing landing page; foundation for the rest of the LeadDesk Mini frontend  
**Out of scope:** Business logic, backend integration, routing changes, component renames, wholesale folder restructuring

---

## 1. Golden Rules

### 1.1 Visual decisions come from the design system

> **Every visual decision must come from the design system.**  
> No component may invent its own spacing, colors, border radius, shadows, transitions, opacity, layout metrics, or typography.  
> Components consume semantic tokens; they do not define them.

### 1.2 Components consume tokens — they never define brand styling

> **Components may consume only semantic utilities and design tokens.**  
> **Components must never define brand styling internally.**  
> They do not own colors, type scales, radii, shadows, spacing recipes, or motion curves. Those live in the token layer and reusable primitives (`Surface`, `Button`, `Card`, etc.).

### Enforcement

- Components must **never** reference raw color values (no hex, no `rgb()` / `rgba()` in component files, no Tailwind palette defaults like `indigo-600` / `slate-900` for brand UI).
- Components must use semantic Tailwind utilities mapped from CSS variables (e.g. `bg-background`, `text-heading`, `rounded-3xl`, `shadow-md`, `duration-base`, `opacity-muted`).
- Components must **not** embed one-off visual “recipes” (custom gradients, magic spacing, ad-hoc shadows) that are not expressed as tokens or shared primitives.
- New visual needs require a **token or primitive first**, then component consumption.
- These rules apply to the landing page now and to future dashboard / authenticated pages.

---

## 2. Goals & Constraints

### Goals

- Polish the existing LeadDesk Mini landing foundation into a premium pastel SaaS marketing site.
- Establish a production-grade semantic design-token system (Tailwind 4 `@theme` + CSS variables).
- Implement Light / Dark / System theming with `next-themes`.
- Preserve the current component architecture, hierarchy, names, and page composition.
- Make the design system reusable for dashboard and authenticated surfaces.

### Constraints

- Do **not** change overall architecture, component hierarchy, or rename existing components.
- Do **not** introduce business logic or backend integration.
- Do **not** change routing.
- Allowed additive design-system files: `src/styles/design-tokens.css`, `Surface`, `ThemeProvider`, `ThemeToggle`, `useScrollReveal`.
- Use only subtle animations (no heavy motion libraries).
- Maintain semantic HTML, keyboard navigation, and WCAG-compliant contrast in both themes.

### Aesthetic direction

Inspired by modern Dribbble / Figma SaaS landings:

- Large rounded containers
- Soft pastel colors
- Elegant whitespace
- Premium typography
- Floating navigation
- Soft shadows
- Calm, welcoming minimalism

---

## 3. Design System Specification

### 3.0 Token file location

| File | Responsibility |
|---|---|
| `frontend/src/styles/design-tokens.css` | **Single source of truth** for all CSS custom properties (`:root` + `.dark`) — colors, typography roles, spacing, radii, shadows, transitions, z-index, opacity, layout, status |
| `frontend/src/app/globals.css` | Imports Tailwind + `../styles/design-tokens.css`; bridges tokens into Tailwind via `@theme inline`; global element rules (`h1–h6`, `body`, reduced motion) |

Components never import raw hex maps. They only consume semantic utilities generated from tokens.

### 3.1 Color tokens

Semantic names only. Hex / alpha values live exclusively in `design-tokens.css`.

#### Light theme

| Token | Hex | Role |
|---|---|---|
| `background` | `#FBEFEF` | Page canvas |
| `surface` | `#FFF7F6` | Elevated panels, navbar, cards |
| `section` | `#FFE2E2` | Section card fills, soft bands |
| `accent` | `#F5CBCB` | Soft highlights, secondary fills |
| `primary` | `#C5B3D3` | Primary actions, brand mark, key accents |
| `heading` | `#2D2A32` | Headings and strong emphasis |
| `body` | `#5E5A66` | Body copy, nav links, labels |
| `card` | `#FFF7F6` | Same as surface in light — keeps `bg-card` portable |
| `border` | `#EBD4D4` | Dividers, card outlines |
| `muted` | `#8A8494` | Captions, footer meta |

#### Dark theme

| Token | Hex | Role |
|---|---|---|
| `background` | `#221D2E` | Page canvas |
| `surface` | `#302740` | Elevated panels, navbar |
| `section` | `#3B324D` | Section card fills |
| `card` | `#3B324D` | Cards and inset panels |
| `primary` | `#C5B3D3` | Primary actions / brand |
| `accent` | `#F5CBCB` | Soft highlights |
| `heading` | `#F7F3FA` | Headings |
| `body` | `#D8CCE6` | Body copy |
| `border` | `#4A415C` | Dividers, outlines |
| `muted` | `#A99BBB` | Captions, footer meta |

Both themes expose the full semantic set (`background`, `surface`, `section`, `card`, `accent`, `primary`, `heading`, `body`, `border`, `muted`) so components never branch on missing tokens.

#### Status tokens (pipeline mockup + future dashboard)

| Token | Light | Dark | Intent |
|---|---|---|---|
| `success` | `#7D9B7A` | `#9BB896` | Positive / Won |
| `success-foreground` | `#F5FBF4` | `#1A2419` | Text on success |
| `warning` | `#C4A574` | `#D4B88A` | Attention / Proposal Sent |
| `warning-foreground` | `#2D2A32` | `#221D2E` | Text on warning |
| `danger` | `#C48B8B` | `#D4A0A0` | Errors / destructive |
| `danger-foreground` | `#2D2A32` | `#221D2E` | Text on danger |
| `info` | `#C5B3D3` | `#C5B3D3` | Neutral / New Leads (aligned to primary) |
| `info-foreground` | `#2D2A32` | `#221D2E` | Text on info |
| `qualified` | `#B7C4E0` | `#C5D0EA` | Qualified stage (soft blue-lavender) |
| `qualified-foreground` | `#2D2A32` | `#221D2E` | Text on qualified |

#### Interaction tokens

| Token | Light | Dark | Role |
|---|---|---|---|
| `ring` | `#C5B3D3` | `#C5B3D3` | Focus ring color |
| `primary-foreground` | `#2D2A32` | `#221D2E` | Text on primary fills |
| `accent-foreground` | `#2D2A32` | `#221D2E` | Text on accent fills |
| `overlay` | `rgba(45, 42, 50, 0.4)` | `rgba(34, 29, 46, 0.6)` | Future scrims |

### 3.2 Typography tokens

| Role | Family | Source | CSS variable |
|---|---|---|---|
| Headings (`h1`–`h6`) | Plus Jakarta Sans | `next/font/google` | `--font-heading` |
| Body / UI | DM Sans | `next/font/google` | `--font-sans` |

**Application rules**

- Configure both fonts in `layout.tsx` via `next/font/google`.
- Expose as CSS variables on `<html>`.
- Apply heading font globally to `h1–h6` in `globals.css`.
- Body, buttons, navigation, labels, and form fields use `--font-sans`.
- Components must **not** apply ad-hoc font family classes; they inherit from the design system.

**Type scale (semantic sizes)**

| Token / level | Size | Line height | Notes |
|---|---|---|---|
| `display` / `h1` | `clamp(2.5rem, 5vw, 3.75rem)` | `1.15` | Hero only |
| `h2` | `clamp(1.75rem, 3vw, 2.5rem)` | `1.2` | Section titles |
| `h3` | `1.25rem` | `1.3` | Card titles |
| `body` | `1rem` | `1.6` | Default copy |
| `body-lg` | `1.125rem` | `1.6` | Hero / lead paragraphs |
| `sm` | `0.875rem` | `1.5` | Nav, captions, labels |
| `xs` | `0.75rem` | `1.4` | Fine print, badges |

Avoid arbitrary one-off `text-[…]` sizes in components unless mapped to a token.

### 3.3 Spacing tokens

4px base scale exposed via Tailwind spacing. Semantic layout spacing:

| Token | Value | Usage |
|---|---|---|
| `space-section-y` | `5rem` (`80px`) / `6rem` at `sm+` | Section vertical padding |
| `space-section-x` | `1.5rem` / `2rem` / `2.5rem` | Section horizontal padding |
| `space-stack-sm` | `1.5rem` | Tight stacks |
| `space-stack-md` | `2rem` | Default stacks |
| `space-stack-lg` | `3rem` | Heading → content gaps |
| `space-page-gutter` | `1rem` / `1.5rem` / `2rem` | Page edge inset (Container) |

Content max width: `1280px` (`--layout-max-width`) via existing `Container`.

### 3.4 Layout tokens

| Token | Value | Usage |
|---|---|---|
| `--layout-max-width` | `80rem` (1280px) | `Container` max width |
| `--layout-nav-height` | `4rem` | Navbar inner height |
| `--layout-nav-inset` | `1rem` | Floating navbar top/side inset |
| `--layout-hero-text` | `45%` | Hero copy column |
| `--layout-hero-media` | `55%` | Hero mockup column |
| `--layout-section-gap` | `2rem` | Gap between section shells |

### 3.5 Opacity tokens

| Token | Value | Usage |
|---|---|---|
| `--opacity-subtle` | `0.04` | Faint washes |
| `--opacity-muted` | `0.08` | Soft overlays / blob base |
| `--opacity-soft` | `0.16` | Hover washes |
| `--opacity-medium` | `0.4` | Disabled-adjacent / overlays |
| `--opacity-navbar` | `0.72` | Floating navbar fill (pre-scroll) |
| `--opacity-navbar-scrolled` | `0.88` | Floating navbar fill (scrolled) |
| `--opacity-blob` | `0.35` | Decorative gradient blobs |
| `--opacity-disabled` | `0.5` | Disabled controls |

Expose as semantic utilities where practical (e.g. `opacity-muted`, `bg-surface/navbar` via tokenized alpha). Components must not invent `opacity-[0.73]`-style values.

### 3.6 Radius tokens

| Token | Usage |
|---|---|
| `rounded-full` | Buttons, badges, icon buttons |
| `rounded-2xl` | Floating navbar bar |
| `rounded-3xl` | Section shells (`Surface`), cards, hero container, CTA |

### 3.7 Shadow tokens

| Token | Usage |
|---|---|
| `shadow-sm` | Resting cards / controls |
| `shadow-md` | Hover elevation |
| `shadow-lg` | Scrolled navbar / emphasized panels |
| `shadow-none` | Navbar at top of page (pre-scroll) |

Soft, pastel-friendly shadows only — no multi-layer neon/glow stacks.

### 3.8 Transition tokens

| Token | Usage |
|---|---|
| `duration-fast` | Icon / micro interactions |
| `duration-base` | Hover, theme color transitions |
| `ease-standard` | Default easing |

**Theme switching:** animate **colors / backgrounds / borders only** (no layout motion on theme change).

### 3.9 Z-index tokens

| Token | Usage |
|---|---|
| `z-nav` | Floating navbar |
| `z-overlay` | Future modals/drawers |
| `z-toast` | Future notifications |

### 3.10 Theme switching

- Library: `next-themes`
- Modes: **Light → Dark → System** (cycle order)
- `attribute="class"`, `defaultTheme="system"`, `enableSystem`, persistence via library storage
- Respect OS preference when System is selected
- `ThemeProvider` wraps app children in root layout
- `suppressHydrationWarning` on `<html>`
- Toggle UI: Sun / Moon / Monitor icons from `lucide-react`
- Toggle lives in the floating navbar (right cluster)
- Lightweight icon transition; accessible name describing current/next mode

---

## 4. UI Specification

### 4.1 Page composition (unchanged architecture)

```
Navbar
main
  Hero (+ trust strip)
  Features
  WhyChooseUs
  HowItWorks
  CTA
  Contact
Footer
```

Existing component names and import graph remain. Section bodies wrap content in the shared `Surface` shell (see §5.3).

### 4.2 Layout shell

- Page uses `background` token.
- `Container` remains the width/padding primitive (`--layout-max-width`).
- Avoid edge-to-edge content: sections sit as individual premium `Surface` cards with page gutter inset.
- Vertical rhythm between shells uses `--layout-section-gap`.

### 4.3 Navbar

- Sticky floating navbar with `--layout-nav-inset`.
- Inner bar: **`rounded-2xl`** (not pill), backdrop blur, semi-transparent `surface` using `--opacity-navbar` / `--opacity-navbar-scrolled`, subtle border.
- **Scroll transition:** richer treatment combining opacity + shadow + border as the user scrolls.
- Shadow emphasized after scroll; quieter at page top.
- Layout: Logo (left) · nav links (center, md+) · ThemeToggle + **Admin Login** CTA (right).
- Keyboard accessible; existing nav config from `lib/navigation.ts` preserved.

### 4.4 Hero

- Large `Surface` (`rounded-3xl`, section/primary-tinted) with clipped decorative blobs.
- Decorative pastel CSS gradient blobs: **subtle**, clipped (`overflow-hidden`), opacity from `--opacity-blob`, `aria-hidden="true"`.
- Layout split: **`--layout-hero-text` (45%) / `--layout-hero-media` (55%)** (stacks on mobile: text then mockup).
- Content:
  - Brand signal: **LeadDesk Mini**
  - Heading: **Capture, organize, and close leads without the clutter**
  - Supporting paragraph: one sentence on modern pipeline capture for growing teams
  - Primary CTA: **Start free inquiry** → `#contact`
  - Secondary CTA: **See how it works** → `#how-it-works`
- Right side: **realistic sales pipeline mockup** (HTML/CSS tokens only — no stock art):

| Column | Status token |
|---|---|
| New Leads | `info` |
| Qualified | `qualified` |
| Proposal Sent | `warning` |
| Won | `success` |

  - Window chrome + four pipeline columns (collapse to horizontal scroll or 2×2 on small screens)
  - Soft lead cards with name/company stubs and stage tags
  - Mockup root: `aria-hidden="true"` (decorative)

### 4.5 Trust strip

- Rendered **inside the existing `Hero` component**, directly below the hero `Surface`.
- Three calm cues: **Secure** · **Fast** · **Production-ready**
- Decorative separators `aria-hidden="true"`.
- No stat theater, no card grid.

### 4.6 Features / WhyChooseUs / HowItWorks

- Each section rendered inside a premium `Surface` section shell.
- Features: three `Card` items from existing content.
- WhyChooseUs: three value props using the shared `Card` component.
- HowItWorks: three-step sequence; step markers use `primary` / heading tokens.

### 4.7 CTA

- Soft primary/accent-tinted `Surface` band.
- Heading: **Ready to take control of your lead pipeline?**
- Support: one short sentence.
- Primary button: **Submit an inquiry** → `#contact`
- Secondary button: **Open admin portal** → `/login`

### 4.8 Contact

- Visual polish only: tokenized form placeholder shell (fields remain placeholder until form milestone).
- Labels/inputs use DM Sans and form tokens (border, surface, ring).
- Placeholder primary action label (visual only): **Send inquiry**

### 4.9 Footer

- Quiet `surface` / muted treatment; preserve attribution link; tokenized colors only.

### 4.10 Motion

| Trigger | Behavior |
|---|---|
| Theme change | Color / background / border transitions only |
| Scroll reveal | Intersection Observer fade + slight lift on section `Surface`s |
| Hover | Card/button lift via shadow + translate tokens |
| Reduced motion | Disable non-essential motion via `prefers-reduced-motion` |

No Framer Motion or other heavy animation libraries.

### 4.11 Accessibility

- Semantic landmarks (`header`, `nav`, `main`, `section`, `footer`) preserved.
- Visible focus rings using `ring` token.
- WCAG contrast for `heading`/`body` on `background`/`surface`/`card` in both themes.
- Decorative blobs, mockup ornaments, and trust separators: hidden from AT.
- Theme toggle operable by keyboard; clear accessible name.

### 4.12 SEO & Metadata

Configure in root `layout.tsx` (and page-level overrides only if needed) using Next.js Metadata API — visual tokens do not replace metadata.

| Field | Value |
|---|---|
| `title` | `LeadDesk Mini — Modern Lead Management` |
| `description` | From `SITE_CONFIG.description` (keep single source in `lib/constants.ts`) |
| `applicationName` | `LeadDesk Mini` |
| `metadataBase` | Site origin from env when available; sensible localhost fallback for dev |
| Open Graph | `title`, `description`, `type: website`, `siteName: LeadDesk Mini` |
| Twitter | `card: summary_large_image`, matching title/description |
| `robots` | `index, follow` for the public landing page |
| Icons | Existing favicon / app icon paths under `public/` |

Do not invent marketing copy in multiple places — title/description should resolve from `SITE_CONFIG` where practical.

### 4.13 Performance Budget

Targets for the marketing landing page (measure in production build):

| Metric / budget | Target |
|---|---|
| LCP | ≤ 2.5s on mid-tier mobile |
| CLS | ≤ 0.1 |
| INP | ≤ 200ms |
| JS shipped (First Load JS, app route) | Prefer ≤ 150KB gzipped incremental; avoid new heavy client libraries |
| Animation libraries | None (CSS + small Intersection Observer hook only) |
| Images / illustrations | None required for v1 hero (CSS mockup only) |
| Fonts | Two families via `next/font` (self-hosted, subset `latin`); no extra weights beyond those used |
| Theme flash | Mitigated via `next-themes` + `suppressHydrationWarning` on `<html>` |
| Client components | Limit to `ThemeProvider`, `ThemeToggle`, scroll-aware Navbar bits, `useScrollReveal` consumers |

If a dependency would break this budget, prefer a token/CSS solution.

---

## 5. Component Specification

### 5.1 Architecture preservation

| Keep | Do not |
|---|---|
| Folder structure under `components/{common,layout,sections}` | Rename existing components |
| `page.tsx` composition order | Add business logic |
| Props interfaces in `types/index.ts` (extend for new primitives) | Change routes |
| `Container`, `Navbar`, `Footer`, section components | Invent per-file brand styling |

### 5.2 New / extended UI pieces

| Piece | Placement | Notes |
|---|---|---|
| Design tokens | `src/styles/design-tokens.css` | Single source of truth for CSS variables |
| Token bridge + globals | `app/globals.css` | `@import` tokens; `@theme inline`; element defaults |
| `Surface` | `components/common/Surface.tsx` | Reusable section / panel shell |
| `ThemeProvider` | `components/common/ThemeProvider.tsx` (client) | Wraps children in root layout |
| `ThemeToggle` | `components/common/ThemeToggle.tsx` (client) | Used by `Navbar` only |
| `useScrollReveal` | `lib/useScrollReveal.ts` (client hook) | Tiny Intersection Observer helper |

### 5.3 Surface (section shell pattern)

`Surface` is the shared primitive for premium rounded panels. Sections must not re-implement this recipe with one-off classes.

**Responsibilities**

- Apply tokenized radius (`rounded-3xl`), border (`border-border`), background variant, padding, and resting shadow.
- Optional hover elevation only when interactive (default: static for section shells).
- Support polymorphic `as` prop (default `div`) for semantic flexibility.
- Variants:

| Variant | Background token | Typical use |
|---|---|---|
| `section` | `section` | Default marketing section shell |
| `surface` | `surface` | Lighter panels, contact shell |
| `accent` | soft accent/primary blend via tokens | Hero / CTA emphasis |
| `transparent` | none | Rare; layout-only wrapper |

**Explicit section shell pattern**

```tsx
<section id={id} className="py-[length:var(--layout-section-gap)]">
  <Container>
    <Surface variant="section" className="p-space-section">
      <SectionHeading ... />
      {/* section content */}
    </Surface>
  </Container>
</section>
```

(Exact class names must map to tokens/`@theme`; the structure above is normative.)

Hero, Features, WhyChooseUs, HowItWorks, CTA, and Contact each compose `Surface` rather than inventing their own card chrome.

### 5.4 Shared component updates (visual only)

#### Button

- `rounded-full`
- Variants: primary (pastel `primary`), secondary (surface/heading treatment), outline (border + surface)
- Sizes sm/md/lg via spacing/type tokens
- Smooth hover/active using transition tokens
- Focus-visible ring token
- Labels come from callers (see concrete CTAs in §4)

#### Card

- Built on or aligned with `Surface` styling (`rounded-3xl`, soft border, minimal shadow)
- Hover elevation (shadow + slight lift)
- Title/description use heading/body tokens
- No internal brand color literals

#### Badge

- Soft accent/primary surfaces via tokens
- Status variant maps to status tokens
- No raw indigo/emerald utilities

#### SectionHeading

- Generous spacing below via spacing tokens
- Title uses heading font via global `h2` styles
- Description uses body tokens

#### Logo

- Mark uses `primary` / `primary-foreground`
- Wordmark uses `heading`

#### Container

- Remains max-width + horizontal padding primitive using layout tokens
- No color opinions

#### Navbar

- Floating sticky shell + scroll-aware opacity/shadow/border via opacity + shadow tokens
- Integrates `ThemeToggle`
- Admin CTA label: **Admin Login**

#### Section components

- Compose `Surface` for shells
- Hero: clipped blobs, 45/55 split, sales pipeline mockup, trust strip, concrete CTAs
- Replace leftover slate/indigo placeholder styles with tokens

### 5.5 Concrete CTA labels (canonical)

| Location | Label | Target |
|---|---|---|
| Navbar | Admin Login | `/login` |
| Hero primary | Start free inquiry | `#contact` |
| Hero secondary | See how it works | `#how-it-works` |
| CTA primary | Submit an inquiry | `#contact` |
| CTA secondary | Open admin portal | `/login` |
| Contact (placeholder) | Send inquiry | (visual only until form milestone) |

### 5.6 Token consumption examples (illustrative)

Allowed:

```tsx
className="bg-surface text-heading rounded-3xl shadow-sm border border-border"
```

Forbidden:

```tsx
className="bg-[#FFF7F6] text-[#2D2A32] bg-indigo-600 text-slate-900"
```

Also forbidden: defining brand gradients, shadows, or spacing scales inside a feature component instead of tokens / `Surface`.

---

## 6. Implementation Approach

**Token-first CSS variables + Tailwind 4 `@theme` (Approach 1)**

1. Create `src/styles/design-tokens.css` with full `:root` + `.dark` token sets (including layout + opacity).
2. Import tokens from `globals.css`; bridge into Tailwind via `@theme inline`; set global heading/body rules.
3. Load Plus Jakarta Sans + DM Sans in `layout.tsx`; bind CSS variables; wire Metadata per §4.12.
4. Add `next-themes` `ThemeProvider` + cycling `ThemeToggle`.
5. Add `Surface` primitive; restyle shared components to semantic utilities only.
6. Enhance Hero (45/55, pipeline mockup stages, clipped blobs, trust strip, concrete CTAs) and wrap sections in `Surface`.
7. Add Intersection Observer scroll reveals + reduced-motion support.
8. Verify performance budget (§4.13) on production build.
9. Holistic UI review pass before commit (see §8).

Dependencies to add: `next-themes`, `lucide-react`.

---

## 7. Delivery workflow

1. **Phase 3 Planning** — implementation plan from this spec  
2. **Design System Specification** — §3 (this doc)  
3. **UI Specification** — §4 (this doc)  
4. **Component Specification** — §5 (this doc)  
5. **Write** — this file under `docs/superpowers/specs/`  
6. **Review** — stakeholder review of this spec  
7. **Implementation** — visual-only changes per plan  
8. **Code Review** — correctness + golden rule compliance  
9. **Manual Testing** — themes, a11y, responsive, motion, SEO tags  
10. **UI Review Pass** — holistic polish (mandatory before commit)  
11. **Commit** — only after UI review pass  

---

## 8. Mandatory pre-commit UI review checklist

Before committing implementation, verify as one holistic pass:

- [ ] No raw colors / invented spacing / one-off radii / shadows / opacity / type in components
- [ ] Components consume tokens only; no internal brand styling
- [ ] Tokens live in `src/styles/design-tokens.css`; globals only bridges + element rules
- [ ] Sections use `Surface` (or the explicit shell pattern) consistently
- [ ] Spacing rhythm consistent across section cards
- [ ] Typography hierarchy clear on mobile and desktop
- [ ] Focus states visible and tokenized in both themes
- [ ] Responsive: navbar, 45/55 hero stack, pipeline columns, grids, footer
- [ ] Theme cycle Light → Dark → System; persistence; OS respect
- [ ] Theme transitions affect colors only
- [ ] Scroll reveals respect `prefers-reduced-motion`
- [ ] Decorative elements hidden from assistive technologies
- [ ] Contrast acceptable for heading/body on surfaces in both themes
- [ ] Pipeline mockup reads as sales pipeline: New Leads → Qualified → Proposal Sent → Won
- [ ] CTA labels match §5.5 exactly
- [ ] Metadata / SEO fields present per §4.12
- [ ] Performance budget sanity-checked per §4.13

---

## 9. Success criteria

- Landing page feels like a premium pastel SaaS marketing site.
- Light / Dark / System theming works and persists.
- Design tokens in `src/styles/design-tokens.css` are the single source of visual truth.
- Components consume semantic tokens/utilities only and never define brand styling themselves.
- `Surface` standardizes section/panel chrome for landing and future dashboard reuse.
- Existing architecture, names, routes, and page composition are unchanged.
- SEO metadata and performance budget are explicit and verifiable.
- Page remains production-ready: accessible, responsive, and maintainable for the rest of LeadDesk Mini’s frontend.
