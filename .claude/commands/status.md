# Projekt-Status prüfen

Gib einen schnellen Überblick über den aktuellen Projektzustand.

## Prüfe:

1. **Git Status**
   ```bash
   git status
   git log --oneline -5
   ```

2. **Dependencies**
   ```bash
   cat package.json | grep -A 20 '"dependencies"'
   ```

3. **Build Test**
   ```bash
   npm run build
   ```

4. **Offene TODOs im Code**
   ```bash
   grep -r "TODO\|FIXME\|HACK" --include="*.ts" --include="*.tsx" --include="*.js" . | head -20
   ```

## Ausgabe:

Fasse zusammen:
- Aktueller Branch und letzte Commits
- Build-Status (erfolgreich/fehlerhaft)
- Anzahl offener TODOs
- Eventuelle Probleme oder Warnungen
