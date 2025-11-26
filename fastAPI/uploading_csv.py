import csv
import io
from fastAPI.api_generator import app
from fastapi import UploadFile
from utils.sort import Sort
from utils.devide_by_meg import Megurim
from sqlmodel import Session
from dal.conect_engine import engine
from models.soldiers import Soldiers

def read_csv_file(content):
     # Parse CSV
     reader = csv.reader(io.StringIO(content))
     header = next(reader)
     rows = list(reader)
     return rows

@app.post("/assignWithCsv")
def upload_csv(file: UploadFile):
    """
    Endpoint that extracts and processes a CSV file from the request.
    Uses Python's csv library to read and parse the CSV data.
    """
    # Validate that the uploaded file is a CSV
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}


    # Read file bytes
    content = file.file.read().decode("utf-8")
    rows = read_csv_file(content)
    with Session(engine) as session:
         for line in rows:
              soldier = Soldiers(personal_number = line[0],
                                 f_name = line[1],
                                 l_name = line[2],
                                 sex = line[3],
                                 city = line[4],
                                 distance_from_base = line[5]
                                 )
              session.add(soldier)
              session.commit()
     

    Sort.sort_by_distance(rows)
    jaluka_lefi_megurim = Megurim.megurim_A_B(rows)
    soldiers_who_were_actually_deployed = len(jaluka_lefi_megurim["megurim A"]) + len(jaluka_lefi_megurim["megurim B"])
    waiting_list = len(jaluka_lefi_megurim["waiting list"])
    return {
         "number of soldiers deployed": soldiers_who_were_actually_deployed,
         "soldiers left on waiting list": waiting_list
    }







    for line in rows:
        print(line)

    # return {
    #     "filename": file.filename,
    #     "content_type": file.content_type,
    #     "total_rows": len(rows),
    #     "columns": header,
    #     "data": rows[0:5],
    #     "message": f"Successfully processed CSV with {len(rows)} rows"
    # }