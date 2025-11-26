from sqlmodel import SQLModel, Field
from typing import Optional

class Soldiers(SQLModel, table = True):
    personal_number: int
    f_name: str
    l_name: str
    sex: str
    city: str
    distance_from_base: int
    is_deployed: bool = False