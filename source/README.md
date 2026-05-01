# Neural Nautic — Design System

> *A luminous mesh beneath still water. A brushed-silver star, catching light. Where the intelligence of the deep meets the craft of the atelier.*

**Neural Nautic** is a style brand that sits at the crossroads of two motifs:

- **Neural** — the glowing teal network of nodes and synapses; luminosity, intelligence, connection, the deep interior of a thinking machine.
- **Nautic** — the compass rose, the sextant, the brushed-platinum hardware of a well-made vessel; heritage, navigation, precision instruments.

The result is a cool, luxurious, editorial aesthetic: **deep teal waters, glowing cyan synapses, and sculptural silver/platinum marks** against ivory or abyss. The brand is quiet and confident — more Hermès-at-sea than tech-startup. Not loud. Not neon. A refined, slow gleam.

---

## Source materials

These are the assets originally provided by the user, stored under `assets/`:

| Asset | Role | Source file |
|---|---|---|
| Brushed-silver compass star | Primary brand mark / seal | `assets/logo-star.png` |
| Silver "NN" calligraphic monogram | Wordmark / secondary mark | `assets/logo-monogram.png` |
| Luminous teal neural network | Signature background image | `assets/bg-neural-network.png` |

> **Note from the user (in German):** *"The neural network should serve as the background, and the logos should always be used in conjunction with the style."* This is a hard rule — see **Visual Foundations → Backgrounds**.

No codebase, Figma file, or existing product was attached. This system is derived entirely from the three source images and the brand concept.

---

## Index

```
/
├── README.md                 ← you are here
├── SKILL.md                  ← portable skill definition
├── colors_and_type.css       ← core tokens (import this everywhere)
├── assets/
│   ├── logo-star.png
│   ├── logo-monogram.png
│   └── bg-neural-network.png
├── fonts/                    ← (using Google Fonts CDN; see Type Substitutions)
├── preview/                  ← design-system cards (colors, type, components, etc)
└── ui_kits/
    └── website/              ← marketing-site UI kit
        ├── README.md
        ├── index.html
        └── *.jsx components
```

---

## Content Fundamentals

The voice is **slow, assured, and quietly elegant** — the brand is a curator, not a salesperson. Copy borrows from fine watchmaking catalogs, sailing journals, and natural-history plates. Never hype. Never exclamation marks.

### Voice & tone

| Dimension | Choice | Notes |
|---|---|---|
| Person | **Third person** predominantly; **first-person plural ("we")** in atelier/craft moments. Avoid "you" unless in a CTA. | "The mark is struck in sterling." not "Your mark is struck." |
| Register | Elevated, literary, nautical. Occasional technical precision. | Think Aesop × Patek Philippe × Aesop. |
| Humor | Dry, rare. Mostly absent. | A quiet wink, never a joke. |
| Contractions | Sparingly. "It is" over "it's" in display copy; contractions allowed in UI labels. | Reserved, not stiff. |
| Casing | **Title Case** for titles, labels, buttons. **Sentence case** for paragraphs. **ALL CAPS + wide tracking** for eyebrows, section tags, footers. | Never Title Case inside paragraphs. |
| Punctuation | Em-dashes — generously. Oxford commas, always. Periods in display headlines: optional and tasteful. | Colon is a favorite. |
| Numbers | **Spelled out** below ten in prose; numerals for measurements, coordinates, years. | "nine bearings" / "9.4 kt" |
| Emoji | **Never.** | Substitute the star glyph ✦ or use the compass mark. |
| Exclamation marks | **Never** in marketing. Sparingly in system messages. | |

### Lexicon — preferred words

- **Mark** (not "logo"), **vessel** (not "product"), **atelier** (not "studio"), **bearing** (not "direction"), **lattice** / **mesh** (for network), **luminous**, **brushed**, **forged**, **quiet**, **calibrated**, **tide**, **current**, **abyss**, **meridian**, **waypoint**.

### Lexicon — banished words

- "Amazing", "awesome", "game-changer", "disrupt", "AI-powered", "seamless", "crafted" (overused — prefer *forged* or *struck*), "empower", "unlock", "journey" (unless literal), "solutions", "offerings".

### Example copy

**Hero, correct:**
> *Instruments of quiet intelligence.*
> A small atelier of goods and software, navigated by a luminous mesh.
> — *Explore the collection*

**Hero, wrong:**
> *Unlock AI-powered awesomeness!*
> Join the journey — your next game-changing tool awaits. 🚀

**UI microcopy, correct:** *"Chart a new bearing" · "Saved to the log" · "Cast off" (for submit) · "Return to shore" (for back)*

**Microcopy, wrong:** *"Click here!" · "You're all set 🎉" · "Oops!"*

### Rhythm

Sentences alternate between short declaratives and longer, comma-knit clauses. Paragraphs are lean — three to four sentences. White space is content.

---

## Visual Foundations

### Palette

Three families, used in specific ratios:

- **Deep Sea (primary, ~60%)** — `--ink-deep` through `--ink-abyss`. This is the canvas. Dark cyan-blacks, never flat black.
- **Platinum (secondary, ~30%)** — `--silver-*`. Brushed-metal neutrals for type, fine rules, UI chrome. Never pure white — always a warm silver.
- **Cyan Luminance (accent, ~10%)** — `--glow-cyan` and siblings. Used sparingly, like light through water. Accent borders, single focus rings, single link color.
- **Ivory (alt canvas)** — `--ivory`, `--ivory-soft`. For the rare light-mode moment (editorial pages, print, packaging).

**Ratio rule:** a composition should feel ~60/30/10 dark/silver/cyan. Never two accent colors competing.

### Typography

| Role | Family | Why |
|---|---|---|
| Display | **Italiana** | Tall, narrow, high-contrast didone — echoes the elongated silver spikes of the star mark |
| Editorial / serif headings | **Cormorant Garamond** (regular + italic) | The italic stands in for the "NN" script monogram's voice — it is how the brand "speaks in cursive" |
| UI / body / labels | **Inter** | Quiet, neutral, well-kerned — lets the display types carry emotion |
| Mono | **JetBrains Mono** | For coordinates, specs, code |

> **⚠ Font substitution flag:** No custom font files were supplied. All four faces are loaded from Google Fonts via CDN in `colors_and_type.css`. **If you have licensed faces** (e.g. a custom engraved display, a bespoke script for the NN monogram, or Commercial Type / Klim equivalents), please provide the files and we will swap them in under `fonts/`.

Type personality: **italic Cormorant** carries the "script" voice for callouts and pull-quotes; **Italiana** is reserved for hero moments only; **Inter** does all the structural work.

### Spacing & rhythm

Generous. Pages breathe. Section padding on marketing pages is `--sp-9` (96px) to `--sp-10` (128px) vertical; card padding is `--sp-6` (32px). Text columns max out at ~58ch for editorial, ~72ch for UI.

### Backgrounds

**The neural-network image is the signature backdrop.** Rules:

1. Use `assets/bg-neural-network.png` as the page background whenever setting a dark "brand" moment (hero sections, title slides, signed marks).
2. Always combine with a **radial darkening vignette** (`radial-gradient(ellipse at center, transparent 40%, rgba(6,20,25,0.75) 100%)`) to pull focus to content.
3. Optional **subtle parallax** on scroll, at ~20% speed — suggests depth of water.
4. Avoid placing the neural net behind dense text without a dark protection layer (`rgba(10,32,40,0.7)`).
5. For light editorial pages, the canvas is `--ivory`; the neural net is absent but the **silver star** remains as a fine watermark.

Gradients beyond the vignette are rare. No purple-to-pink gradients. No bluish-purple hero gradients.

### Corners & borders

Tight and precise. `--r-md` (6px) is the default card radius. `--r-sm` (4px) for buttons. Pills (`--r-pill`) only for tags and small capsules. **No pillowy rounded cards.** Borders are hairline (`1px` at 10–18% opacity silver), like engraved lines.

### Shadows & elevation

Two systems working together:

- **Ambient shadow** — soft, deep, dark. `--shadow-md` / `--shadow-lg`.
- **Glow** — cyan bloom for interactive / focus / active states. `--glow-accent`. Used on one element at a time.
- **Inner rim** (`--inner-rim`) — adds the brushed-metal facet to buttons and chips.

### Hover & press

- **Hover (dark surfaces):** surface lightens to `--ink-shoal`; accent elements shift to `--glow-aqua` and gain a faint `--glow-accent` bloom. Duration `--dur-fast` (180ms), easing `--ease-out`.
- **Hover (text links):** color shifts, a hairline underline fades in (border-bottom 1px).
- **Press:** `transform: scale(0.98)`; glow dims by 30%. Duration 120ms.
- **Focus (keyboard):** 2px `--accent` ring at 2px offset, plus `--glow-accent`.

### Motion

- **Default easing:** `--ease-sail` — the gliding curve. Never bouncy. Never elastic.
- **Durations:** 180ms for micro, 320ms for panels, 600ms for page transitions, 1100ms for hero reveals.
- **Preferred patterns:** fade + fine upward translate (6–12px), mask-reveal for display type, a slow parallax on the neural bg. No spring animations.
- **Never:** confetti, wiggle, scale bounce, rotate-360 loaders. Instead: a slow rotating compass needle or a pulsing single node.

### Transparency & blur

Sparingly. Used for:
- Floating nav bars over hero (`backdrop-filter: blur(24px)` + `rgba(10,32,40,0.6)`).
- Modal scrim (`rgba(6,20,25,0.72)`).
- Never on primary content surfaces.

### Imagery

- Photography is **cool, under-exposed, slightly cyan**. Film grain encouraged. Think Hiroshi Sugimoto seascapes, Peter Zumthor architectural interiors, a nautical chart photographed at dusk.
- **Never:** warm-saturated stock photos, cheery product-on-white.
- Black-and-white acceptable when it enhances editorial gravity.

### Cards

- Background `--bg-3` on dark canvases, `--ivory-soft` on light.
- Border: `1px solid var(--border-2)`.
- Radius: `--r-md` (6px).
- Shadow: `--shadow-md` + optionally `--inner-rim`.
- Padding: `--sp-6` (32px) default.
- Hover: lifts 2px (`translateY(-2px)`), border upgrades to `--border-3`.

### Layout rules

- **12-column grid** on marketing, `--sp-5` (24px) gutters.
- Sticky top nav **60–72px** with backdrop blur after scroll.
- Footer: deep `--ink-abyss`, full-bleed neural-net at 20% opacity beneath a dark wash.
- Fixed elements: a small silver star anchor (bottom-right) appears site-wide as a "watermark" on dark canvases.

---

## Iconography

**Primary approach: line icons, 1.5px stroke, platinum color, 24×24 viewBox.** Icons are treated as fine engravings, not emoji.

| Source | Use | Notes |
|---|---|---|
| **Lucide Icons** (CDN) | General UI iconography | Stroke-based, 1.5px default, matches the engraved feel. Loaded from `https://unpkg.com/lucide@latest` in UI Kit pages. |
| **Phosphor Thin / Light** (fallback) | When a hairline feel is needed | Available if Lucide weight feels too heavy. |
| **Bespoke SVG marks** | Compass rose, star, monogram — the brand marks | Derived from / reference the provided silver renders; store under `assets/` as PNG until an icon vector is produced. |
| Emoji | **Never.** | |
| Unicode glyphs | Allowed for typographic accents: `✦` (four-pointed star), `◆`, `·` (middle dot as separator), `—` (em dash). Used sparingly. | |

**Substitution flag:** Lucide is used as the CDN icon set by default. If Neural Nautic wishes to commission a bespoke icon family, all Lucide references should be replaced and this document updated.

### Usage rules

- Icon color inherits `currentColor`; primary tone is `--fg-2` (silver-bright) with `--accent` reserved for active/selected states.
- Never color-fill icons — always line/stroke.
- Never nest an icon inside a colored circle background. Let them sit directly in the layout.
- Pair icons with a label below or beside — icons alone are rarely enough.

### Brand marks — usage

1. **The star** (`assets/logo-star.png`) — primary seal. Use it alone on splash/title moments. Always on a dark or ivory canvas with generous margin (minimum 4× the star's diameter of clear space).
2. **The NN monogram** (`assets/logo-monogram.png`) — wordmark. Use in signatures, footers, packaging, stationery. Pair with the star above it for a "formal lockup".
3. **Combination lockup** — star on the left, NN monogram on the right, both vertically centered with a ~28px gap, sharing a single horizontal baseline. The word "NEURAL NAUTIC" in Inter ALL CAPS at `--tracking-widest` sits beneath the pair. This is the form used in the brand key visual (`assets/brand-key-visual.png`) and in `preview/brand-lockup.html` — reserve it for title slides, splash moments, and brand pages.

Always use the logos — per the brand's founding directive — **in concert with the neural-network backdrop** (on dark canvases) or on ivory with a faint watermark of the mesh.

---

## Known gaps / substitutions (for the user)

- **Fonts** — using Google Fonts fallbacks (Italiana, Cormorant Garamond, Inter, JetBrains Mono). Provide licensed faces if available.
- **Logos are JPGs, not vectors.** An SVG version of the star and monogram would allow crisper use at small sizes and recoloring. Please supply if available.
- **No existing product or codebase** was shared; the website UI kit is a *proposed* interpretation of what a Neural Nautic marketing site could look like. Please review and iterate.
- **No photography** was supplied beyond the three source images; the UI kit uses placeholder slots where editorial imagery would go.

---

## Index of files

- **`colors_and_type.css`** — all tokens. Import in any HTML via `<link rel="stylesheet" href="/colors_and_type.css">`.
- **`SKILL.md`** — portable skill definition for use in Claude Code or as an invocable skill.
- **`preview/*.html`** — individual design-system cards registered to the Design System tab. Each isolates one concept (a palette, a type specimen, a button cluster).
- **`ui_kits/website/`** — high-fidelity recreation of a Neural Nautic marketing site, with modular JSX components and a click-through `index.html`.
- **`assets/`** — real brand imagery: logos, the neural-network background.
