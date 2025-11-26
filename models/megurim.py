from sqlmodel import SQLModel, Field
from typing import Optional

class Megurim(SQLModel, table = True):
    personal_number: int
    megurim: int
    room_number: int