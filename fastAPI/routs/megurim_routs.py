from fastAPI.api_generator import app
from dal.megurim_dal import space_left

@app.get("/space/{megurim}")
def get_space_by_meg(megurim):
    # returning a json dict with the answer
    response = space_left(megurim)
    return response