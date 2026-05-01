# Claude Code Prompt – NeuralNautic Website

Du bist ein Senior Frontend Engineer und baust eine professionelle B2B-Website für Frank Schütt unter der Marke „NeuralNautic“.

## Kontext

Das Design wurde separat in Claude Design erstellt. Nutze dieses Design als visuelle Grundlage. Dieses Handoff-Paket enthält Inhalte, Seitenstruktur, Positionierung, Komponentenlogik und SEO-Vorgaben.

## Ziel

Erstelle eine moderne, responsive Website für einen KI-Berater.

## Positionierung

Pragmatische KI-Beratung für den Mittelstand.  
Fokus auf:

- KI-Potenzialanalyse
- Controlled Pilot
- KI-Automatisierung
- KI-Governance
- KI-Schulung
- KI Tool Kompass

## Tech Stack

Nutze bevorzugt:

- Next.js
- TypeScript
- Tailwind CSS
- shadcn/ui
- Framer Motion
- Lucide Icons

Falls bereits ein anderer Stack im Repository vorhanden ist, nutze den bestehenden Stack und integriere die Inhalte sauber.

## Designregeln

- Übernehme das separat erstellte Claude-Design so weit wie möglich.
- Baue nicht irgendein neues generisches KI-Design.
- Verwende viel Weißraum.
- Nutze moderne Cards.
- Nutze dezente Animationen.
- Farben: Violett, Türkis, Dunkelblau, Weiß.
- Keine generischen Roboterbilder.
- Keine überladenen Gradients.
- B2B-seriös, aber modern.
- Vertrauenswürdig, klar, mittelstandstauglich.

## Navigation

Erstelle folgende Seiten:

1. Start `/`
2. Leistungen `/leistungen`
3. Use Cases `/use-cases`
4. Methode `/methode`
5. KI Tool Kompass `/ki-tool-kompass`
6. Wissen `/wissen`
7. Über mich `/ueber-mich`
8. Kontakt `/kontakt`

## Komponenten

Erstelle wiederverwendbare Komponenten:

- Header
- Footer
- HeroSection
- CTASection
- ServiceCard
- UseCaseCard
- MethodStep
- TrustSection
- ContactForm
- GlossaryItem
- SectionHeading

## Inhalt

Nutze `content.json` als zentrale Inhaltsquelle, wenn sinnvoll.  
Alternativ können Inhalte direkt in Page-Komponenten oder einer `content.ts` ausgelagert werden.

## Startseite

Die Startseite muss enthalten:

1. Hero mit Hauptversprechen
2. Problem-Sektion
3. Lösung / 4-Schritte-Modell
4. Leistungsübersicht
5. Use-Case-Teaser
6. Vertrauens-Sektion
7. Final CTA

## Kontaktformular

Erstelle ein sauberes Kontaktformular mit Feldern:

- Name
- Unternehmen
- E-Mail
- Telefon optional
- Anliegen
- Nachricht

Das Formular muss noch keine echte Backend-Anbindung haben, aber sauber vorbereitet sein. Verwende TODO-Kommentare für spätere Integration mit Formspree, Resend, Supabase oder eigener API.

## SEO

Implementiere sinnvolle Meta-Titles und Meta-Descriptions pro Seite.  
Nutze die Angaben aus `SEO.md`.

## Qualität

- Responsive auf Mobile, Tablet, Desktop
- Saubere Semantik
- Gute Accessibility
- Konsistente Abstände
- Keine Dummy-Lorem-Ipsum-Texte
- Keine nichtssagenden KI-Marketing-Floskeln
- Alle CTAs führen zunächst auf `/kontakt`

## Arbeitsweise

1. Prüfe zuerst die vorhandene Projektstruktur.
2. Erstelle oder aktualisiere die Seiten.
3. Lege Content zentral ab.
4. Baue wiederverwendbare Komponenten.
5. Verwende das Claude Design als visuelle Referenz.
6. Entferne Platzhalter.
7. Gib am Ende eine Zusammenfassung der erstellten Dateien und offenen TODOs aus.
