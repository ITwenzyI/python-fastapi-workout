from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.testclient import TestClient

app = FastAPI()

class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    amount: int = Field(gt=0)

@app.post("/items", status_code=201)
def create_item(payload: ItemCreate):
    # normal würde man speichern; wir geben nur zurück
    return {"id": 1, **payload.model_dump()}

client = TestClient(app)

# 2) Erster Happy Path Test
def test_create_item_ok():
    resp = client.post("/items", json={"name": "Banana", "amount": 3})
    assert resp.status_code == 201
    data = resp.json()
    assert data["id"] == 1
    assert data["name"] == "Banana"
    assert data["amount"] == 3

# 3) Erster Validierungs Test
def test_create_item_validation_error():
    resp = client.post("/items", json={"name": "", "amount": 0})
    assert resp.status_code == 422
