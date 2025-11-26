from models.megurim import Megurim
from sqlmodel import Session, select
from dal.conect_engine import engine
# full rooms
# partial rooms
# empty rooms
def space_left(megurim_num):
    rooms = [0,0,0,0,0,0,0,0,0,0]
    response = {"full rooms": "", "partial rooms": "", "empty": ""}
    with Session(engine) as session:
        statement = select(Megurim).where(Megurim.megurim == megurim_num)
        results = session.exec(statement)
        for room in results:
            rooms[room.room_number] += 1

        for room in range(len(rooms)):
            if room == 8:
                response["full rooms"] += f", {str(room)}"
            elif 0 < room < 8:
                response["partial rooms"] += f", {str(room)}"
            else:
                response["empty"] += f", {str(room)}"
    return response