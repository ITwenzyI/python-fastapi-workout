from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel, Field, field_validator
from datetime import date


class Workout(BaseModel):
    id: int = Field(gt=0,)
    date: date
    title: str = Field(min_length=1)
    duration_min: int = Field(gt=0, le=180) # gt= greater than 0 le= max. 180
    notes: str | None = Field(default=None, max_length=200) # Feld ist nicht Pflicht

    @field_validator('title')
    def title_validator(cls, v: str) -> str:
        cleaned = v.strip()
        if len(cleaned) == 0:
            raise ValueError('title cannot be empty')
        return cleaned
    @field_validator('notes')
    def notes_validator(cls, v: str | None) -> str | None:
        if v is None:
            return None
        cleaned = v.strip()
        return cleaned if cleaned else None




class WorkoutCreate(BaseModel): # Ohne ID weil wir die vergeben nicht Client
    date: date
    title: str = Field(min_length=1)
    duration_min: int = Field(gt=0, le=180) # gt= greater than 0 le= max. 180
    notes: str | None = Field(default=None, max_length=200) # Feld ist nicht Pflicht

    @field_validator('title')
    def title_validator(cls, v: str) -> str:
        cleaned = v.strip()
        if len(cleaned) == 0:
            raise ValueError('title cannot be empty')
        return cleaned
    @field_validator('notes')
    def notes_validator(cls, v: str | None) -> str | None:
        if v is None:
            return None
        cleaned = v.strip()
        return cleaned if cleaned else None

#Prefix -> spart  das hängt den Pfad vorne dran (/workouts)
#Tags -> Dann bekommen alle Endpunkte dieses Routers in den Docs eine Überschrift „workouts“.
#        Das ist nur Doku, hat keinen Einfluss auf den eigentlichen Code oder die URL.
router = APIRouter(prefix="/workouts", tags=["Workouts"])

# Beispiel Daten
WORKOUTS = [
    {"id": 1, "date": "2025-08-20", "title": "Push Day", "duration_min": 45, "notes": "leicht gesteigert"},
    {"id": 2, "date": "2025-08-21", "title": "Pull Day", "duration_min": 60, "notes": "stark gesteigert"},
    {"id": 3, "date": "2025-08-23", "title": "Leg Day", "duration_min": 70},
]

@router.get("", response_model=list[Workout])
def list_workouts(min_duration: int | None = None, title_contains: str | None = None):
    result = list(WORKOUTS)
    if min_duration is not None:
        result = [w for w in result if w["duration_min"] >= min_duration]
    if title_contains:
        # .casefold() macht alles klein + berücksichtigt Sonderfälle z.B ß -> ss
        # .strip() Entfernt Leerzeichen am Anfang und Ende des Strings
        q = title_contains.strip().casefold()
        result = [w for w in result if q in w["title"].casefold()]
    return result

@router.post("", response_model=Workout, status_code=201)
def create_workout(payload: WorkoutCreate): # payload ist ein Objekt von WorkoutCreate
    if WORKOUTS:
        new_id = max(w["id"] for w in WORKOUTS) + 1
    else:
        new_id = 1
    new_workout = {"id": new_id, **payload.model_dump()}
    WORKOUTS.append(new_workout)
    return new_workout

@router.get("/{id}", response_model=Workout, status_code=200)
def get_workout(id: int):
    for w in WORKOUTS:
        if w["id"] == id:
            return w
        else:
            continue
    raise HTTPException(status_code=404, detail="Workout not found")

