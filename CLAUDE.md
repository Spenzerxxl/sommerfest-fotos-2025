# sommerfest-fotos-2025

> **Zuletzt aktualisiert:** 12.01.2026  
> **Hauptverantwortlich:** Frank Rath

---

## 🎯 Projektziel

**Was:** [Kurzbeschreibung - 1-2 Sätze]

**Warum:** [Business-Grund]

**Für wen:** [Zielgruppe]

---

## 🛠️ Tech Stack

- **Frontend:** [z.B. Next.js 14, React, Tailwind]
- **Backend:** [z.B. Supabase, Node.js]
- **Hosting:** [z.B. Coolify auf RAG-Server]
- **URL:** [Production URL]

---

## 📁 Projektstruktur

```
/app          - Next.js App Router
/components   - React Komponenten
/lib          - Utilities & Helpers
/public       - Statische Assets
```

---

## ✅ Verifikation

Vor jedem Commit prüfen:

```bash
npm run build      # Muss fehlerfrei durchlaufen
npm run lint       # Keine Errors
npm test           # Falls vorhanden
```

**Health-Check:** `curl [URL]/api/health`

---

## ⚠️ Don'ts - Bekannte Fehler

> Hier Fehler dokumentieren die NICHT wiederholt werden sollen

- [ ] [Fehler 1 - Was passiert ist und warum es vermieden werden soll]
- [ ] [Fehler 2 - ...]

---

## 🔐 Wichtige Hinweise

- **Credentials:** Niemals in Code committen → `.env.local`
- **Branches:** `main` = Production, Feature-Branches für Entwicklung
- **Deployments:** Über Coolify (Frank macht manuell)

---

## 📋 Offene Tasks

- [ ] [Task 1]
- [ ] [Task 2]

---

## 📚 Weiterführende Docs

- Übergabeberichte: `C:\Users\Frank\HiDrive\Agentur\KI\[PROJEKT]\`
- RAG-Datenbank: Projektkontext über `/übergabe` abrufbar
