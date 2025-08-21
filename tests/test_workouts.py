from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_workout_ok():
    resp = client.post("/workouts", json={"date": "2025-08-24", "type": "Legs Day", "duration_min": 80})
    assert resp.status_code == 201
    data = resp.json()
    assert data["date"] == "2025-08-24"
    assert data["type"] == "Legs Day"
    assert data["duration_min"] == 80

def test_create_workout_validation_error():
    resp = client.post("/workouts", json={"date": "2025-08-24", "type": "Legs Day", "duration_min": 0})
    assert resp.status_code == 422