import os
import mysql.connector
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print (BASE_DIR)
load_dotenv(BASE_DIR + '/etc/.env')

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

print (f"{DB_HOST} {DB_PASSWORD}")

command_list = None

database_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(database_path, 'schema.sql')) as file:
    command_list = file.read().split(';')



def sql_execute(sql_list: list, host: str, user: str, password: str):
    with mysql.connector.connect(host=host,user=user,password=password) as conn:
        print('Connected to the Database successfully')
        cursor = conn.cursor()
        for sql_code in sql_list:
            cursor.execute(sql_code + ';')
            print('sql code exicuted')
    print('database setup finished!')
if __name__ == '__main__':
    sql_execute(command_list,
                DB_HOST,
                DB_USER,
                DB_PASSWORD)