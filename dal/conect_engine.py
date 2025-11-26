from sqlmodel import create_engine, SQLmodel
import sqlite3

engine = create_engine("sqlite3:///shibolim.db")

def create_db_and_tables():
    SQLmodel.metadata.create_all(engine)