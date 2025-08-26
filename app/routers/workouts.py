from fastapi import APIRouter
from fastapi import HTTPException
# from pydantic import BaseModel, Field, field_validator
# from datetime import date
# from enum import Enum
from app.models.workout import WorkoutCreate, Workout, WorkoutType
from app.dependencies.auth import get_current_user_id
from fastapi import Depends

#Prefix -> spart  das hängt den Pfad vorne dran (/workouts)
#Tags -> Dann bekommen alle Endpunkte dieses Routers in den Docs eine Überschrift „workouts“.
#        Das ist nur Doku, hat keinen Einfluss auf den eigentlichen Code oder die URL.
router = APIRouter()

# Beispiel Daten
WORKOUTS = [
    {"id": 1, "date": "2025-08-20", "type": "Push Day", "duration_min": 45, "notes": "leicht gesteigert", "user_id": 1},
    {"id": 2, "date": "2025-08-21", "type": "Pull Day", "duration_min": 60, "notes": "stark gesteigert", "user_id": 1},
    {"id": 3, "date": "2025-08-23", "type": "Legs Day", "duration_min": 70, "user_id": 2},
]

@router.get("/", response_model=list[Workout])
def list_workouts(min_duration: int | None = None, workout_type: WorkoutType | None = None):
    result = list(WORKOUTS)
    if min_duration is not None and workout_type is not None:
        result = [w for w in result if w["type"] == workout_type and w["duration_min"] >= min_duration]
    if min_duration is not None:
        result = [w for w in result if w["duration_min"] >= min_duration]
    if workout_type is not None:
        result = [w for w in result if w["type"] == workout_type]
    if len(result) == 0:
        raise HTTPException(status_code=404, detail="Workout not found")
    return result

@router.get("/depends", status_code=200, response_model=list[Workout])
def list_workouts(user_id: int = Depends(get_current_user_id)):
    result = [w for w in WORKOUTS if w["user_id"] == user_id]
    return result


@router.post("/", response_model=Workout, status_code=201)
def create_workout(payload: WorkoutCreate, user_id: int = Depends(get_current_user_id)): # payload ist ein Objekt von WorkoutCreate
    if WORKOUTS:
        new_id = max(w["id"] for w in WORKOUTS) + 1
    else:
        new_id = 1
    new_workout = {"id": new_id, **payload.model_dump(), "user_id": user_id}
    for w in WORKOUTS:
        if w["type"] == new_workout["type"] and w["date"] == new_workout["date"]:
            raise HTTPException(status_code=409, detail="Workout already exists")
    WORKOUTS.append(new_workout)
    return new_workout

@router.get("/{id}", response_model=Workout, status_code=200)
def get_workout(id: int):
    for w in WORKOUTS:
        if w["id"] == id:
            return w
    raise HTTPException(status_code=404, detail="Workout not found")

