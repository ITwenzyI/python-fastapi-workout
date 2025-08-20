from fastapi import FastAPI
from app.routers.workouts import router as workouts_router
app = FastAPI(title="Workout API v1")


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


app.include_router(workouts_router)