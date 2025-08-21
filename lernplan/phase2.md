## Phase 2
### 📅 Plan für Phase 2

#### Einführung in Pydantic-Modelle

- Warum Pydantic?

- Erstellen eines ersten Modells für ein Workout (z. B. Name, Dauer).

#### Request-Modelle

- Validierung von Daten, die der Client (z. B. Nutzer oder Frontend) schickt.

- Beispiel: POST /workouts erwartet ein Workout-Modell.

#### Response-Modelle

- Saubere Ausgabe definieren.

- Beispiel: API gibt nur bestimmte Felder zurück, auch wenn intern mehr gespeichert ist.

#### Pflichtfelder vs. optionale Felder

- Standardwerte in Modellen.

- Optional vs. Required.

#### Fehlerbehandlung mit HTTPException

- Was passiert, wenn etwas fehlt oder falsch ist.

- Beispiel: Workout nicht gefunden → HTTP 404.

#### Automatisierte Tests mit TestClient

- Installation und erster Test.

- Test, ob ein POST mit falschen Daten fehlschlägt.

#### Mini-Projekt: Workout Tracker

- Endpunkte: Workouts anlegen, abrufen, Liste anzeigen.

- Eingaben validieren und saubere Antworten zurückgeben.

#### Theorie-Tag

- Warum sind Modelle wichtig?

- Wie helfen sie bei Security, Dokumentation und Testbarkeit?

#### Abschluss & README

- Zusammenfassung in eigenen Worten.

- Mindestens 1 automatisierter Test grün.
