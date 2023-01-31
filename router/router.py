from fastapi import APIRouter
from schema.data_schema import DataSchema
from config.db import engine
from model.data import data
from typing import List

service = APIRouter()

@service.get("/")
def status():
    return {"message":"online"}

@service.post("/data")
def adding_data(data_info: DataSchema):
    with engine.connect() as conn:
        new_record = data_info.dict()
        conn.execute(data.insert().values(new_record))
        conn.commit()
        return "Success"
    
@service.get("/data", response_model=List[DataSchema])
def get_data():
    with engine.connect() as conn:
        result = conn.execute(data.select()).fetchall()
        print(result)
        return result

@service.get("/data/{id}", response_model=DataSchema)
def get_data(id: str):
    with engine.connect() as conn:
        result = conn.execute(data.select().where(data.c.id == id)).first()
        return result

@service.put("/data/{id}", response_model=DataSchema)
def update_data(data_update: DataSchema, id: str):
    with engine.connect() as conn:
        conn.execute(data.update().values(name = data_update.name,
                     desc = data_update.desc,).where(data.c.id == id))
        conn.commit()
        result = conn.execute(data.select().where(data.c.id == id)).first()
        return result

@service.delete("/data/{id}")
def delete_data(id: str):
    with engine.connect() as conn:
        conn.execute(data.delete().where(data.c.id == id))
        conn.commit()
        return "Success"

