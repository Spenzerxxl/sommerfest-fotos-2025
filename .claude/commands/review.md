# Code Review

Führe ein Code Review der aktuellen Änderungen durch.

## Prüfe:

1. **Was wurde geändert?**
   ```bash
   git diff --stat
   git diff
   ```

2. **Code-Qualität checken:**
   - Sind die Änderungen konsistent mit dem bestehenden Code-Style?
   - Gibt es offensichtliche Bugs oder Edge-Cases?
   - Sind Error-Handling und Logging angemessen?
   - Gibt es Security-Bedenken?

3. **CLAUDE.md prüfen:**
   - Verstoßen die Änderungen gegen dokumentierte "Don'ts"?
   - Passt es zur Projektstruktur?

## Ausgabe:

Erstelle ein kurzes Review mit:
- ✅ Was ist gut
- ⚠️ Was könnte verbessert werden
- 🚨 Was muss geändert werden (falls kritisch)

Sei konstruktiv und konkret.
