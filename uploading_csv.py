import csv
import io
from fastAPI.api_generator import app
from fastapi import UploadFile
from utils.sort import Sort
from utils.devide_by_meg import Megurim

@app.post("/assignWithCsv")
def upload_csv_and_sort(file: UploadFile):
    """
    Endpoint that extracts and processes a CSV file from the request.
    Uses Python's csv library to read and parse the CSV data.
    """
    # Validate that the uploaded file is a CSV
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}


    # Read file bytes
    content = file.file.read().decode("utf-8")

    # Parse CSV
    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)
    Sort.sort_by_distance(rows)
    jaluka_lefi_megurim = Megurim.megurim_A_B(rows)
    







    # for line in rows:
    #     print(line)

    # return {
    #     "filename": file.filename,
    #     "content_type": file.content_type,
    #     "total_rows": len(rows),
    #     "columns": header,
    #     "data": rows[0:5],
    #     "message": f"Successfully processed CSV with {len(rows)} rows"
    # }