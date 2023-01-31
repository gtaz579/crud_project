from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:secret@dbinstance:3306/db_sample")

meta_data = MetaData()
