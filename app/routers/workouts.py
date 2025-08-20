from fastapi import APIRouter

#Prefix -> spart  das hängt den Pfad vorne dran (/workouts)
#Tags -> Dann bekommen alle Endpunkte dieses Routers in den Docs eine Überschrift „workouts“.
#        Das ist nur Doku, hat keinen Einfluss auf den eigentlichen Code oder die URL.
router = APIRouter(prefix="/workouts", tags=["Workouts"])

# Beispiel Daten
WORKOUTS = [
    {"id": 1, "date": "2025-08-20", "title": "Push Day", "duration_min": 45, "notes": "leicht gesteigert"},
    {"id": 2, "date": "2025-08-21", "title": "Pull Day", "duration_min": 60, "notes": "stark gesteigert"},
]

@router.get("")
def list_workouts(min_duration: int | None = None, title_contains: str | None = None):
    result = list(WORKOUTS)
    if min_duration is not None:
        result = [w for w in result if w["duration_min"] >= min_duration]
    if title_contains:
        q = title_contains.strip().casefold()
        result = [w for w in result if q in w["title"].casefold()]
    return result

@router.get("/{id}")
def get_workout(id: int):
    for w in WORKOUTS:
        if w["id"] == id:
            return w
    return {"message": "Workout not found"}
