from fastapi import FastAPI
from app.routers.workouts import router as workouts_router
from app.routers.greetings import router as greetings_router
app = FastAPI(title="Workout API v1")


@app.get("/")
def read_root():
    print("DEBUG root called")
    return {"status": "ok"}

app.include_router(greetings_router)
app.include_router(workouts_router)