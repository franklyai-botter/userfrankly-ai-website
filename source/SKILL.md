---
name: neural-nautic-design
description: Use this skill to generate well-branded interfaces and assets for Neural Nautic, either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.

If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.

If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.

Key facts to internalize before designing:

- **Brand DNA:** neural + nautic. Deep teal waters, brushed silver/platinum, glowing cyan synapses. Luxurious and quiet, editorial, never loud or tech-bro.
- **The neural-network background image (`assets/bg-neural-network.png`) is a signature element** — use it on dark/brand moments with a vignette. This is a hard rule from the brand owner.
- **The two logos (`assets/logo-star.png`, `assets/logo-monogram.png`) must appear when the style is invoked.**
- **Palette ratio:** ~60% deep-sea ink / ~30% silver-platinum / ~10% cyan accent. Never two competing accents.
- **Typography:** Italiana (display hero), Cormorant Garamond (serif/italic editorial), Inter (UI/body), JetBrains Mono (code).
- **No emoji.** Use `✦` or the star mark instead.
- **Voice:** third person / "we" (atelier), literary, slow, no exclamation marks, em-dashes welcome. Words like *mark, vessel, atelier, bearing, lattice, luminous*. Avoid *amazing, journey, seamless, unlock*.
- **Icons:** Lucide Icons via CDN (1.5px stroke, no fill).
- **Corners:** tight — 6px default, 4px buttons. Never pillowy.
- **Motion:** gliding `cubic-bezier(0.22, 0.61, 0.36, 1)`, never bouncy, never springy.

Always import `colors_and_type.css` at the root of any HTML file you generate, and reference assets from `assets/` directly.
