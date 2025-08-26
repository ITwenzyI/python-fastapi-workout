from fastapi import APIRouter
from fastapi import HTTPException


router = APIRouter()

USERS = [
    {
        "name": "User1",
        "id": 1,
    },
    {
        "name": "User2",
        "id": 2,
    },
    {
        "name": "User3",
        "id": 3,
    }
]

@router.get("/", status_code=200)
def get_all_users():
    return USERS

@router.get("/{id}", status_code=200)
def get_user_by_id(id: int):
    for user in USERS:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")