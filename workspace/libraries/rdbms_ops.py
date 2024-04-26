import sys
sys.path.append(r'C:\Data\2-Workspace\2-Project\common')

from constants import *
from sqlalchemy import create_engine, text

def create_postgresql_engine(database, server=POSTGRESQL_SERVER, port=POSTGRESQL_PORT, user=POSTGRESQL_USER, password=POSTGRESQL_PASSWORD):
    return create_engine(f'postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_SERVER}:{POSTGRESQL_PORT}/{database}')

def create_mysql_engine(database, server=MYSQL_SERVER, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD):
    return create_engine(f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{database}')

def execute_query(engine, sql, return_value=False):
    with engine.connect() as connection:
        cursor = connection.execute(text(sql))
        if return_value==True:
            result = []
            columns = cursor.keys()
            for row in cursor:
                transformed_row = {}
                for i, column in enumerate(columns):
                    transformed_row[column] = row[i]
                result.append(transformed_row)
            return result
