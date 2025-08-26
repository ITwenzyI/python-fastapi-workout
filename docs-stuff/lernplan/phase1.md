
## Phase 1
### 📅 Plan für Phase 1 (1 Woche)
#### Tag 1: Projekt-Setup
- Virtuelle Umgebung in PyCharm anlegen.
- FastAPI und Uvicorn installieren.
- Git-Repo initialisieren, .gitignore anlegen.
- Erster Commit: feat: init fastapi project.

#### Tag 2: Erste GET-Endpunkte
- Route / → Begrüßungstext.
- Route /hello → einfache JSON-Antwort.
- Route /workouts → vorerst Dummy-Daten.
- Test in /docs.
- Commit: feat: add first GET endpoints.

#### Tag 3: Path- und Query-Parameter
- Path-Parameter: /hello/{name}.
- Query-Parameter: z.B. /hello?lang=de&upper=true.
- Testen, ob die Parameter greifen.
- Commit: feat: add path and query parameters.

#### Tag 4: Unterschiedliche Responses und Statuscodes
- Unterschied: normale JSON-Antwort vs. strukturierte Response mit festgelegten Feldern.
- Statuscodes setzen (200 OK, 201 Created, 404 Not Found).
- Commit: feat: add responses with status codes.

#### Tag 5: Mini-Projekt Workout Tracker
- Daten im Speicher (Liste oder Dict).
- GET /workouts → gibt alle Workouts zurück.
- POST /workouts → neues Workout hinzufügen.
- Erfolgskriterium: POST liefert 201 Created.
- Commit: feat: add workout tracker endpoints.

#### Tag 6: Theorie-Tag
- Warum Statuscodes wichtig sind (für API-Clients, Debugging, Standards).
- Eigene kurze Notizen dazu machen.
- Kein Code, nur Verständnis.
- Commit: docs: add notes about status codes.

#### Tag 7: Zusammenfassung & README
- Kurze README schreiben: Was gelernt, warum wichtig, Beispiel (GET oder POST).
- Commit: docs: add phase 1 summary.