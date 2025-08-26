from fastapi.testclient import TestClient
from app.main import app
# from app.models.workout import WorkoutCreate, Workout, WorkoutType

client = TestClient(app)

def test_create_workout_ok():
    resp = client.post("/workouts", json={"date": "2025-08-24", "type": "legs", "duration_min": 80})
    assert resp.status_code == 201
    data = resp.json()
    assert data["date"] == "2025-08-24"
    assert data["type"] == "legs"
    assert data["duration_min"] == 80
    assert data["user_id"] == 1

def test_create_workout_validation_error():
    resp = client.post("/workouts", json={"date": "2025-08-24", "type": "legs", "duration_min": 0})
    assert resp.status_code == 422

def test_create_workout_duplicate_error():
    resp1 = client.post("/workouts", json={"date": "2025-08-29", "type": "legs", "duration_min": 30})
    assert resp1.status_code == 201
    resp2 = client.post("/workouts", json={"date": "2025-08-29", "type": "legs", "duration_min": 60})
    assert resp2.status_code == 409

def test_get_workout_not_found():
    resp = client.get("/workouts/999")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Workout not found"