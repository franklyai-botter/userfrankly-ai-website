# NeuralNautic Website

## What This Is

Die NeuralNautic-Website ist die Marketing- und Beratungsseite von Frank Schütt — KI-Berater für den Mittelstand. Die Seite präsentiert Leistungen, Methode, Use Cases und ermöglicht Kontaktaufnahme. Sie richtet sich an Geschäftsführer und Entscheider im DACH-Mittelstand.

## Core Value

Ein potenzieller Kunde landet auf der Seite, versteht sofort was NeuralNautic macht und nimmt Kontakt auf.

## Codebase Location

Der Code liegt in: `C:\Users\frank\Downloads\neural-nautic-website\`
Tech Stack: Next.js 15, TypeScript, Inline Styles (kein Tailwind), next/image

Design-Assets und Handoff: `C:\Users\frank\Downloads\Neural Nautic Design System\design_handoff_neural_nautic\`

## Requirements

### Validated

- ✓ Grundstruktur aller Seiten (Home, Leistungen, Methode, Use Cases, Wissen, KI Tool Kompass, Über mich, Kontakt) — bestehend
- ✓ Design System implementiert (Farben, Fonts, CSS Variables) — bestehend
- ✓ Footer mit Logo und Neural Network Background — bestehend
- ✓ Neural Network Background auf allen Unterseiten (Header) — Phase 0

### Active

- [ ] Neural Network im Hero der Startseite deutlich sichtbarer (Gradient angepasst)
- [ ] Scroll-Reveal Animationen auf allen Seiten (Elemente faden beim Scrollen rein)
- [ ] Mobile-Optimierung: vollständig responsive auf Smartphone (sehr hohe Priorität)

### Out of Scope

- Backend / CMS — statische Inhalte reichen für jetzt
- Blog-System / dynamische Inhalte — v2
- Dark/Light Mode Toggle — nicht geplant
- i18n / Mehrsprachigkeit — nur Deutsch

## Context

- Design-Handoff liegt vor mit vollständigem Design System (Farben, Fonts, Assets)
- Die Seite existiert bereits und ist technisch funktionsfähig
- Neural Network (`bg-neural-network.png`) ist das zentrale visuelle Element der Marke
- Logo-Stern (`logo-star.png`) und Monogramm (`logo-monogram.png`) als Branding-Elemente
- Primärfarbe: `--glow-cyan` (#3FD4E0), Hintergrund: `--ink-abyss` (#061419)
- Frank ist der einzige Entwickler, Solo-Projekt

## Constraints

- **Tech Stack**: Next.js 15 + TypeScript — keine andere Framework-Änderung
- **Styling**: Inline Styles (kein Tailwind, kein CSS Modules) — konsistent halten
- **Performance**: next/image für alle Bilder, keine schweren Animation-Libraries wenn möglich
- **Mobile**: Mobile-first, da viele Besucher via Smartphone kommen

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Inline Styles statt Tailwind | Design System via CSS Variables, maximale Kontrolle | — Pending |
| Neural Network als Overlay mit Gradient | Sichtbarkeit im Hero: radial-gradient lässt Netzwerk rechts durchscheinen | — Pending |
| Scroll-Reveal ohne schwere Library | Intersection Observer API direkt oder Framer Motion falls nötig | — Pending |

## Evolution

Dieses Dokument entwickelt sich bei Phasenübergängen.

**Nach jeder Phase:**
1. Requirements validiert? → In Validated verschieben
2. Neue Anforderungen? → In Active aufnehmen
3. "What This Is" noch korrekt? → Anpassen falls nötig

---
*Last updated: 2026-05-01 nach Initialisierung*
