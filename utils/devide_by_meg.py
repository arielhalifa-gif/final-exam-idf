class Megurim:
    def megurim_sorting(soldiers: list[list[str]]):
        division = []
        rooms = 10
        beds_for_room = 8
        for room in range(rooms):
            for bed in range(beds_for_room):
                if len(soldiers) > 0:
                    division.append(soldiers.pop(0))
                else:
                    break
        return division
    
    def megurim_A_B(soldiers: list[list[str]]):
        megurim_a = Megurim.megurim_sorting(soldiers)
        megurim_b = Megurim.megurim_sorting(soldiers)
        hamtana = Megurim.megurim_sorting(soldiers)
        return {"megurim A": megurim_a, "megurim B": megurim_b, "waiting list": hamtana}
    
