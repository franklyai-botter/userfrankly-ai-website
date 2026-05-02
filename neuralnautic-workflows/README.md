# Neural Nautic — KI Workflows

Statische Website mit vier KI-Workflows für den DACH-Mittelstand.
DSGVO-konform · Hosting in Deutschland · keine Datenweitergabe an Drittländer.

## Aufbau

- `index.html` — Übersicht aller Workflows
- `mail-workflow.html` — E-Mail-Triage mit Human-in-the-Loop
- `local-analysis.html` — Dokumenten-Pipeline mit OCR und Belegankerung
- `rag-model.html` — Retrieval-Augmented Generation
- `rag-risk.html` — Risikoampel und Compliance-Mapping

## Lokaler Test

```bash
python3 -m http.server 8000
```

Dann `http://localhost:8000` im Browser öffnen.

## Deployment

GitHub Pages: Branch `main`, Root-Verzeichnis des `neuralnautic-workflows/`-Ordners.

## Kontakt

frankschuettai@neuralnautic.org
