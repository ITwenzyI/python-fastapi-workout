from fastapi import APIRouter

router = APIRouter(prefix="/hello", tags=["Greetings"])



# Feste Route (/hello) → immer gleiche Antwort.
@router.get("")
def hello():
    return {"message": "Hello World!"}

# Dynamische Route mit Path-Parameter (/hello/{name}) → Antwort hängt vom Wert in der URL ab.
@router.get("/{name}")
def hello_name(name: str):
    return {"message": f"Hello, {name}!"}