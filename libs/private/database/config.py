import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv()

enginePostgres = create_engine("postgresql+pg8000://{}:{}@{}:{}/{}".format(
    os.getenv('DB_USERNAME'),
    os.getenv('DB_PASSWORD'),
    os.getenv('DB_HOST'),
    os.getenv('DB_PORT'),
    os.getenv('DB_NAME')
))

meta = MetaData(schema=os.getenv('DB_SCHEMA'))

connection = enginePostgres.connect()
