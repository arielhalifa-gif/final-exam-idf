from dal.conect_engine import engine
from models.soldiers import Soldiers
from sqlmodel import Session, select

def sort_soldiers_by_distance():
    with Session(engine) as session:
        statement = select(Soldiers).order_by("Soldiers.distance_from_base DESC")
        results = session.exec(statement)
        return results.all()
    

def search_soldier_by_personal_number(pn: int):
    with Session(engine) as session:
        statement = select(Soldiers).where(Soldiers.personal_number == pn)
        results = session.exec(statement)
        soldiers_by_pn = results.all()
        return soldiers_by_pn