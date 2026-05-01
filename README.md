# Handoff: Neural Nautic — Brand & Design System

## Overview

Neural Nautic is a brand identity and design system for a luxury / atelier-style product line that lives at the intersection of **neural intelligence** and **nautical heritage**. The system covers the full visual language: brand marks, color, typography, spacing, components, and a marketing website UI kit.

The brand metaphor: *a luminous mesh beneath still water — a brushed-silver compass star catching light.* Editorial, quiet, never tech-bro. Think Vogue × Patek Philippe × an AI lab.

## About the Design Files

The files in `source/` are **design references created in HTML/CSS/JSX** — prototypes showing intended look and feel, not production code to copy directly.

The task is to **recreate these designs in the target codebase's existing environment** (React, Vue, SwiftUI, native, etc.) using its established patterns and libraries. If no environment exists yet, choose the most appropriate framework and implement there.

The `colors_and_type.css` file is the **canonical token source** — port its CSS custom properties to whatever token system the codebase uses (Tailwind theme, Style Dictionary, design-tokens.json, etc.).

## Fidelity

**High-fidelity.** All colors, typography, spacing, and brand assets are final. Recreate pixel-perfectly using the codebase's existing libraries — but adapt the layout to its grid/spacing primitives rather than copying inline styles 1:1.

---

## Brand Marks

Two primary marks; either may stand alone, or appear in lockup.

| Mark | File | Use |
|---|---|---|
| **Compass Star (silver)** | `assets/logo-star.png` | Primary brand seal. Brushed-silver six-pointer. Use on dark/teal backgrounds. |
| **Compass Star (gold)** | `assets/logo-star-gold.png` | Alternate warmth. Use on cream / ivory backgrounds. |
| **NN Monogram** | `assets/logo-monogram.png` | Calligraphic NN with descending flourish. Wordmark-style. Use beside the star or alone in atelier contexts. |
| **NN Monogram (script)** | `assets/logo-monogram-script.png` | Simpler script variant for tight footprints. |
| **Key Visual** | `assets/brand-key-visual.png` | Hero composition — both marks on neural-network field. For website headers, presentation covers, app splashscreens. |
| **Neural BG** | `assets/bg-neural-network.png` | Signature background — luminous teal mesh. The brand's "wallpaper". |

**Clear space** — minimum 0.5× the mark's height on all sides.
**Minimum size** — Star 24px digital / 12mm print. Monogram 32px / 16mm.
**Don't** — recolor the marks beyond the silver/gold variants provided. Don't place silver mark on ivory or gold mark on dark teal.

---

## Color System

Source: `source/colors_and_type.css`

### Deep Sea (primary surface)
Dark teals — the "underwater" feel of the brand. Backgrounds, hero sections, footers.

| Token | Hex | Use |
|---|---|---|
| `--ink-abyss` | `#04141A` | Deepest background — page bg, modal scrim base |
| `--ink-deep` | `#06141A` | Body bg on dark surfaces |
| `--ink-tide` | `#0A2028` | Section bg, card bg on dark |
| `--ink-current` | `#0F2C36` | Elevated card on dark |
| `--ink-foam` | `#143744` | Border / divider on dark |

### Cyan / Synapse (signal)
The glow. Use sparingly — accent only.

| Token | Hex | Use |
|---|---|---|
| `--cyan-synapse` | `#00D4FF` | Primary accent, links, focused states, tiny halos |
| `--cyan-deep` | `#0098B8` | Hover state of synapse |
| `--cyan-veil` | `rgba(0,212,255,.15)` | Glow / halo wash |

### Platinum / Silver (metal)
The brand mark's hue — also typography on dark.

| Token | Hex | Use |
|---|---|---|
| `--platinum-100` | `#F4F4F2` | Lightest text on dark |
| `--platinum-300` | `#D6D6D2` | Body text on dark |
| `--platinum-500` | `#A8A8A4` | Muted text on dark |
| `--platinum-700` | `#6E6E6A` | Captions, meta |

### Champagne / Gold
Warm metal — use with the gold star variant or for premium accents.

| Token | Hex |
|---|---|
| `--champagne` | `#D4AF37` |
| `--champagne-soft` | `#D8C09E` |

### Ivory (light surface)
Counterpoint to the dark theme — editorial, journal, atelier moments.

| Token | Hex | Use |
|---|---|---|
| `--ivory-100` | `#FAF7F1` | Page bg |
| `--ivory-200` | `#F2EEE5` | Card bg, sectioning |
| `--ivory-300` | `#E8E2D5` | Borders on light |
| `--ivory-ink` | `#1A1F24` | Primary text on ivory |
| `--ivory-muted` | `#5C6168` | Secondary text on ivory |

### Semantic
| Token | Hex | Use |
|---|---|---|
| `--signal-positive` | `#5DB996` | Success, in-stock |
| `--signal-warning` | `#D4A85C` | Warning, low stock |
| `--signal-critical` | `#C76A6A` | Error, sold out |

---

## Typography

All four faces are free, served via Google Fonts.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Italiana&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

| Face | Role | When |
|---|---|---|
| **Italiana** | Display | Hero titles, "NEURAL NAUTIC" wordmark, large numerals. Hairline serif — looks fragile, intentionally so. |
| **Cormorant Garamond** | Editorial | Pull quotes, journal-style body, italic accents, atelier notes. |
| **Inter** | UI / Body | All UI chrome — nav, buttons, forms, body text, labels. |
| **JetBrains Mono** | Code / Tag | Tags ("01 / 02"), system labels, technical codes. |

### Type scale (UI / Inter unless noted)

| Token | Size / line | Use |
|---|---|---|
| `--t-display-xl` | 96 / 1.0, Italiana, ls -0.02em | Hero |
| `--t-display-l` | 64 / 1.05, Italiana | Section hero |
| `--t-display-m` | 44 / 1.1, Italiana | Page title |
| `--t-editorial` | 28 / 1.4, Cormorant 400 italic | Pull quote |
| `--t-h1` | 36 / 1.2, Inter 600 | |
| `--t-h2` | 24 / 1.3, Inter 600 | |
| `--t-h3` | 18 / 1.4, Inter 600 | |
| `--t-body` | 16 / 1.6, Inter 400 | |
| `--t-body-s` | 14 / 1.55, Inter 400 | |
| `--t-meta` | 12 / 1.4, Inter 500, ls 0.08em, uppercase | Meta lines |
| `--t-tag` | 10 / 1.2, JetBrains 500, ls 0.18em, uppercase | Tags, codes |

### Voice

- **Display tone:** quiet luxury. "Meridian 01", "Atelier Notes", never "Buy now!".
- **UI tone:** declarative, present-tense, no exclamation marks.
- **No emoji** in product copy.

---

## Spacing & Radii

```
--space-1: 4px;   --space-2: 8px;   --space-3: 12px;
--space-4: 16px;  --space-5: 20px;  --space-6: 24px;
--space-8: 32px;  --space-10: 40px; --space-12: 48px;
--space-16: 64px; --space-20: 80px; --space-24: 96px;

--radius-sm: 2px;   /* tags, chips */
--radius-md: 4px;   /* buttons, inputs */
--radius-lg: 8px;   /* cards */
--radius-xl: 16px;  /* hero cards, modals */
--radius-pill: 999px;
```

**Default page rhythm:** sections separated by `--space-20` (80px) on desktop, `--space-12` (48px) on mobile. Card grids: `--space-6` (24px) gap.

## Shadows

Designed for dark backgrounds primarily — shadows are subtle and warm.

```
--shadow-sm: 0 2px 8px rgba(0,0,0,.18);
--shadow-md: 0 8px 24px rgba(0,0,0,.32);
--shadow-lg: 0 24px 60px rgba(0,0,0,.45);
--shadow-glow: 0 0 40px rgba(0,212,255,.18); /* synapse halo */
```

---

## Components

Each one has a preview HTML file in `source/preview/`. Read those for exact layout & state.

| Component | File | Notes |
|---|---|---|
| Buttons | `preview/buttons.html` | Primary (synapse cyan), Secondary (platinum outline), Ghost, Disabled. Pill or md radius. Hover lifts shadow + halos. |
| Forms | `preview/forms.html` | Input, textarea, select. Underline-style (no border box) on dark surface; bordered on ivory. Focus = synapse glow under the input. |
| Tags | `preview/tags.html` | JetBrains Mono, uppercase. Filled or outline. |
| Cards | `preview/cards.html` | Object card pattern: image top, meta line, title, price. Subtle hover lift. |
| Nav | `preview/nav.html` | Star mark left, link list center, account/cart right. Sticky. Translucent on scroll. |
| Notices | `preview/notices.html` | Info, success, warning, error — semantic-tinted left rule, ivory or dark surface. |
| Stats / Quote | `preview/stats-quote.html` | Editorial blocks. |
| Iconography | `preview/iconography.html` | 1.5px stroke, rounded caps. ~20 stock icons defined as SVG inline. |

### Website UI Kit (`source/ui_kits/website/`)

Built as React + Babel inline JSX. Treat as visual reference; reimplement with the codebase's component model.

| Component | File | Purpose |
|---|---|---|
| `Header` | `Header.jsx` | Sticky top nav with star mark and primary links. |
| `Hero` | `Hero.jsx` | Full-bleed neural-bg hero with display title + sub. |
| `FeaturedCollection` | `FeaturedCollection.jsx` | Grid of object cards (chronometers, instruments). |
| `AtelierNote` | `AtelierNote.jsx` | Editorial pull-quote block on ivory. |
| `JournalList` | `JournalList.jsx` | Article list, journal-style. |
| `ObjectDetail` | `ObjectDetail.jsx` | Single product detail. |
| `Footer` | `Footer.jsx` | Footer with star mark, columns, fine print. |
| `atoms.jsx` | | Button, Input, Tag, etc. |

---

## Interactions & Behavior

- **Hover** — 200ms ease-out. Buttons gain shadow + 1px lift. Cards gain `--shadow-md` and the meta line shifts hue from `platinum-500` → `platinum-300`.
- **Focus** — Synapse cyan ring (2px outer, 1px offset). Always visible — never `outline:none` without a replacement.
- **Page transitions** — Crossfade 240ms; no slide.
- **Scroll behavior** — Header gains backdrop blur + lowered opacity bg after 64px scroll.

## State / Data needs

The website UI kit assumes:
- A `products` collection (id, title, kind, price, hero image, description)
- A `journal` collection (id, title, kind, date, excerpt, hero image)
- Routing between collection list, object detail, journal list

These are local stub data in the JSX — replace with the codebase's data layer.

---

## Assets

All in `source/assets/`. PNG with transparency where appropriate.

| File | Dimensions | Notes |
|---|---|---|
| `bg-neural-network.png` | 1920×1080 | Lossy compression OK if you re-export. Keep deep teal cast. |
| `logo-star.png` | ~764×732 | Silver, transparent BG |
| `logo-star-gold.png` | ~340×320 | Gold, transparent BG |
| `logo-monogram.png` | ~590×478 | NN mark, transparent BG |
| `logo-monogram-script.png` | ~variable | Script variant |
| `brand-key-visual.png` | 1920×1080 | Hero composition (both marks + neural bg) |

If your codebase has an asset pipeline (Vite, Next, etc.), place these in `public/brand/` or equivalent and reference via the framework's asset helper.

---

## Files in this bundle

```
source/
├── README.md                    Brand documentation (long-form)
├── SKILL.md                     One-page brand cheat-sheet
├── colors_and_type.css          Canonical design tokens
├── assets/                      Brand marks + neural bg
├── preview/                     Single-card design system previews
└── ui_kits/website/             Website component library (React/JSX)
```

## Implementation order (suggested)

1. Port `colors_and_type.css` tokens → your token system
2. Add the 4 Google Fonts to your app's font loader
3. Drop assets into your asset pipeline
4. Build atomic components (Button, Input, Tag, Card) matching `preview/*.html`
5. Compose page sections (Header, Hero, etc.) matching `ui_kits/website/*.jsx`
6. Wire to real data

## Questions for the dev?

- The HTML/JSX shows the *intent* — match the visual exactly, but use idiomatic patterns from your codebase.
- If a token or measurement isn't documented here, look in `source/colors_and_type.css` — it's the source of truth.
