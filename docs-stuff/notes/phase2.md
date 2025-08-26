# Phase 2 – Modelle & Validierung

## Was habe ich gelernt?
- Eingaben und Ausgaben werden mit **Pydantic-Modellen** abgesichert.
- Pflichtfelder, optionale Felder und Constraints sorgen für saubere Daten.
- Constraints = z.B `duration_min: int = Field(gt=0, le=180)`
- Enums helfen, feste Kategorien vorzugeben.
- Mit `HTTPException` lassen sich klare Fehlercodes (404, 409) zurückgeben.
- Automatisierte Tests mit `pytest` und `TestClient` prüfen wichtige Fälle.

## Warum ist das wichtig?
- **Sicherheit**: falsche oder absurde Daten werden automatisch abgefangen.
- **Klarheit**: Frontend und Backend wissen genau, welche Felder erlaubt sind.
- **Dokumentation**: Swagger zeigt direkt die erlaubten Felder und Werte.
- **Wartbarkeit**: Fehlerfälle sind eindeutig mit Statuscodes abgebildet.
- **Qualität**: automatisierte Tests verhindern, dass Fehler unbemerkt bleiben.

## Beispiel
### Request (korrekt)
```json
{
  "date": "2025-08-29",
  "type": "Legs Day",
  "duration_min": 60
} 
```

### Response
```json
{
  "id": 1,
  "date": "2025-08-29",
  "type": "Legs Day",
  "duration_min": 60,
  "notes": null
} 
```

## Fehlerfälle
- 422: ungültige Eingabe (z.B. duration_min = 0)
- 404: Workout nicht gefunden
- 409: Workout mit gleicher Kombination aus date und type existiert schon


