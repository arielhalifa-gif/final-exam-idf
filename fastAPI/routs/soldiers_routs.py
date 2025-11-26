from fastAPI.api_generator import app
from sqlmodel import Session, select
from models.soldiers import Soldiers
from dal.conect_engine import engine
from dal.soldier_dal import search_soldier_by_personal_number


@app.get("/search/{personal_number}")
def get_by_pn(personal_number):
    soldier_by_pn = search_soldier_by_personal_number(personal_number)
    if soldier_by_pn.is_deployed:
        answer = f"the soldier pn: {soldier_by_pn.personal_namber} has been deployed"
    else:
        answer = f"the soldier pn: {soldier_by_pn.personal_namber} is in waiting list"
    response = {"is deployed?": soldier_by_pn.is_deployed, "messege": answer}
    return response
    

    
@app.get("/waitingList")
def get_the_waiting_list():
    pass