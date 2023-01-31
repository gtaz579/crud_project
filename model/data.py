from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

data = Table("data", meta_data,
            Column("id", Integer, primary_key=True),
            Column("name", String(50), nullable=False),
            Column("desc", String(100), nullable=False))

meta_data.create_all(engine)