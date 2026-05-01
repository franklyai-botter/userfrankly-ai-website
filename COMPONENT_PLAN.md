# Component Plan

## Empfohlene Struktur für Next.js App Router

```txt
src/
  app/
    page.tsx
    leistungen/
      page.tsx
    use-cases/
      page.tsx
    methode/
      page.tsx
    ki-tool-kompass/
      page.tsx
    wissen/
      page.tsx
    ueber-mich/
      page.tsx
    kontakt/
      page.tsx
    layout.tsx
    globals.css
  components/
    layout/
      Header.tsx
      Footer.tsx
    sections/
      HeroSection.tsx
      ProblemSection.tsx
      SolutionSection.tsx
      ServicesOverview.tsx
      UseCaseOverview.tsx
      MethodTimeline.tsx
      TrustSection.tsx
      CTASection.tsx
      ContactSection.tsx
    ui/
      ServiceCard.tsx
      UseCaseCard.tsx
      MethodStep.tsx
      GlossaryItem.tsx
      SectionHeading.tsx
  data/
    content.ts
    navigation.ts
```

## Komponentenbeschreibung

### Header

- Logo / Wortmarke NeuralNautic
- Navigation
- CTA Button: KI-Potenzialcheck buchen
- Mobile Menu

### Footer

- Kurzbeschreibung
- Navigation
- Rechtliches
- Kontakt
- Standort: Berlin / Brandenburg / Remote in DACH

### HeroSection

Props:

- headline
- subheadline
- primaryCTA
- secondaryCTA
- visual optional

### ServiceCard

Props:

- title
- description
- icon optional
- cta optional

### UseCaseCard

Props:

- title
- description
- category
- icon optional

### MethodTimeline

Zeigt die 5 Phasen:

1. Verstehen
2. Priorisieren
3. Pilotieren
4. Automatisieren
5. Skalieren

### ContactForm

Felder:

- Name
- Unternehmen
- E-Mail
- Telefon
- Anliegen
- Nachricht

Todo:

- Backend-Integration mit Resend, Formspree, Supabase oder API Route
