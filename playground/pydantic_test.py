from pydantic import BaseModel

class Workout(BaseModel):
    name: str
    duration: int


w1 = Workout(name="Pull Day", duration=60)
print(w1)

# Not Good but is possible
w2 = Workout(name="Push Day", duration="60")
print(w2)

# Error duration str -> int XXX
# w3 = Workout(name="Pull Day", duration="Lange")
# print(w3)