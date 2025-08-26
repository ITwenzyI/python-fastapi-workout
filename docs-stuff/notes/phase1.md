## Wozu Statuscodes?

- Sie sind der erste Hinweis für den Client, was passiert ist.

Beispiel:

- 200 OK → alles geklappt
- 201 Created → neue Ressource angelegt
- 404 Not Found → Ressource gibt es nicht
- 422 Unprocessable Entity → Eingabe ungültig

Ohne Statuscodes müsste der Client immer erst ins JSON schauen → unpraktisch und unsauber.

## Warum wichtig?

APIs sind Kommunikationsschnittstellen.

Andere Programme (Clients, Apps, Browser) reagieren nicht auf Text, sondern auf Statuscodes.

Beispiel: Ein Browser zeigt „404“ groß an, noch bevor er ins JSON schaut.

In automatisierten Tests ist es einfach zu prüfen:

```
assert response.status_code == 201
```

## Typische Gruppen

2xx = Erfolg

3xx = Weiterleitungen

4xx = Clientfehler (z. B. 404, 422)

5xx = Serverfehler (z. B. 500)

------------------

### Warum 201 Created beim POST besser als nur 200 OK

A: Somit weis das Programm das etwas erfolgreich angelegt worden ist und nicht nur 200, was bedeutet hat funktioniert.

--------------

## Was habe ich gelernt

- Statuscodes (200, 201, 404, 422)
- Routes und Router (Aufteilung in Dateien)
- GET und POST
- Path- und Query-Parameter
- Response-Modelle mit Pydantic

## Warum ist das wichtig?

- **Statuscodes**: Clients erkennen sofort am Status, ob eine Anfrage erfolgreich war oder nicht. Müssen sich nicht erst die Json-Antwort anschauen.
- **Routes und Router**: sorgen für Übersicht, Struktur und eine saubere Projektstruktur.
- **GET und POST**: GET für Datenabruf, POST für das Erstellen/Anlegen neuer Daten.
- **Path-Parameter**: für feste Abschnitte in der URL.  
  **Query-Parameter**: für optionale Filter und Argumente.
- **Response-Modelle**: garantieren einheitliche Antworten und verhindern fehlerhafte Rückgaben.

## Beispiel – Notizen API
```python
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

class NoteCreate(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)

class Note(BaseModel):
    id: int
    title: str
    content: str

router = APIRouter(prefix="/notes", tags=["notes"])

NOTES = [
    {"id": 1, "title": "Einkauf", "content": "Milch und Brot kaufen"},
    {"id": 2, "title": "Training", "content": "Push Day am Abend"},
]

@router.get("", response_model=list[Note], status_code=200)
def list_notes():
    return NOTES

@router.get("/{id}", response_model=Note, status_code=200)
def get_note(id: int):
    for n in NOTES:
        if n["id"] == id:
            return n
    raise HTTPException(status_code=404, detail="Note not found")

@router.post("", response_model=Note, status_code=201)
def create_note(payload: NoteCreate):
    new_id = max(n["id"] for n in NOTES) + 1
    new_note = {"id": new_id, **payload.dict()}
    NOTES.append(new_note)
    return new_note
```

## Typische Antworten

- GET /notes → 200 OK, liefert alle Notizen

- GET /notes/1 → 200 OK, liefert eine Notiz

- GET /notes/999 → 404 Not Found

- POST /notes mit gültigen Daten → 201 Created + neue Notiz

- POST /notes mit ungültigen Daten (z. B. leerer Titel) → 422 Unprocessable Entity