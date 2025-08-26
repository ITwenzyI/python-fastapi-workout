from pydantic import BaseModel, Field, field_validator
from enum import Enum
from datetime import date

class WorkoutType(str, Enum):
    PUSH = "push"
    PULL = "pull"
    LEGS = "legs"
    CARDIO = "cardio"

class Workout(BaseModel):
    id: int = Field(gt=0)
    date: date
    type: WorkoutType
    duration_min: int = Field(gt=0, le=180) # gt= greater than 0 le= max. 180
    notes: str | None = Field(default=None, max_length=200) # Feld ist nicht Pflicht
    user_id: int = Field(gt=0)

    @field_validator('notes')
    def notes_validator(cls, v: str | None) -> str | None:
        if v is None:
            return None
        cleaned = v.strip()
        return cleaned if cleaned else None




class WorkoutCreate(BaseModel): # Ohne ID weil wir die vergeben nicht Client
    date: date
    type: WorkoutType
    duration_min: int = Field(gt=0, le=180) # gt= greater than 0 le= max. 180
    notes: str | None = Field(default=None, max_length=200) # Feld ist nicht Pflicht

    @field_validator('notes')
    def notes_validator(cls, v: str | None) -> str | None:
        if v is None:
            return None
        cleaned = v.strip()
        return cleaned if cleaned else None