from dal.conect_engine import engine
from models.soldiers import Soldiers
from sqlmodel import Session, select

def sort_soldiers_by_distance():
    with Session(engine) as session:
        statement = select(Soldiers).order_by("Soldiers.distance_from_base DESC")
        results = session.exec(statement)
        return results.all()
    

