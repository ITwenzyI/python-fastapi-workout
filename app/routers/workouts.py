from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import HTTPException


class Workout(BaseModel):
    id: int
    date: str
    title: str
    duration_min: int
    notes: str | None = None # Feld ist nicht Pflicht

class WorkoutCreate(BaseModel): # Ohne ID weil wir die vergeben nicht Client
    date: str
    title: str
    duration_min: int
    notes: str | None = None

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
        q = title_contains.strip().casefold()
        result = [w for w in result if q in w["title"].casefold()]
    return result

@router.post("", response_model=Workout, status_code=201)
def create_workout(payload: WorkoutCreate): # payload ist ein Objekt von WorkoutCreate
    if WORKOUTS:
        new_id = max(w["id"] for w in WORKOUTS) + 1
    else:
        new_id = 1
    new_workout = {"id": new_id, **payload.dict()}
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

