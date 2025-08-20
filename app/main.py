from fastapi import FastAPI
app = FastAPI(title="Workout API v1 - TEST")


@app.get("/")
def read_root():
    print("DEBUG root called")
    return {"status": "ok"}


# Feste Route (/hello) → immer gleiche Antwort.
@app.get("/hello")
def hello():
    return {"message": "Hello World!"}

# Dynamische Route mit Path-Parameter (/hello/{name}) → Antwort hängt vom Wert in der URL ab.
@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hello, {name}!"}

workouts = [{
    "id": 1,
    "date": "2025-08-20",
    "title": "Push Day",
    "duration_min": 45,
    "notes": "leicht gesteigert"
},
{
    "id": 2,
    "date": "2025-08-21",
    "title": "Pull Day",
    "duration_min": 60,
    "notes": "stark gesteigert"
}

]


@app.get("/workouts")
def get_workouts(min_duration: int = None, title_contains: str = None):
    result = list(workouts)

    if min_duration is not None:
        result = [w for w in result if w["duration_min"] >= min_duration]

    if title_contains:
        title_lower = title_contains.lower()
        result = [w for w in result if title_lower in w["title"].lower()]

    return result


@app.get("/workouts/{id}")
def get_workout(id: int):
    for workout in workouts:
        if workout["id"] == id:
            return workout
    return {"message": "Workout not found"}
