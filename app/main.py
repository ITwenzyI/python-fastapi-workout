from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
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
def get_workouts():
    return workouts