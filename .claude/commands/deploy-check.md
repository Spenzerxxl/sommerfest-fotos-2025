# Pre-Deployment Checkliste

Prüfe ob das Projekt deployment-ready ist.

## Checkliste:

### 1. Build
```bash
npm run build
```
→ Muss fehlerfrei durchlaufen

### 2. Lint
```bash
npm run lint
```
→ Keine Errors (Warnings dokumentieren)

### 3. Tests (falls vorhanden)
```bash
npm test
```
→ Alle Tests grün

### 4. Git Status
```bash
git status
```
→ Keine uncommitteten Änderungen

### 5. Environment Check
- [ ] `.env.local` nicht im Repo
- [ ] Keine hardcodierten Secrets
- [ ] Alle benötigten ENV-Vars dokumentiert

### 6. CLAUDE.md
- [ ] Aktuell und vollständig
- [ ] Don'ts-Sektion geprüft

## Ausgabe:

```
DEPLOYMENT CHECK: [PROJEKTNAME]
================================
Build:        ✅/❌
Lint:         ✅/❌
Tests:        ✅/❌/⚠️ (keine vorhanden)
Git Clean:    ✅/❌
Env Check:    ✅/❌

STATUS: READY / NOT READY

Probleme (falls vorhanden):
- ...
```

**Hinweis:** Deployments macht Frank manuell über Coolify!
