#################################################################
#connect.py
#Maneja la conexion a la base de datos
##################################################################

from os import environ
from typing import Callable, Any
from dotenv import load_dotenv
import pymysql.cursors
from pymysql import Connection
import logging

load_dotenv()

#Variables de Conexion
DB_USER = environ.get('DB_USER')
DB_PASS =environ.get('DB_PASS')
DB_HOST = environ.get('DB_HOST')
DB_PORT = int(environ.get('DB_PORT'))
DB_NAME = environ.get('DB_NAME')

def dbConnectionDecorator(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args , **kwargs) -> Any:
        try:
            #Conexion a Mysql
            conexion: Connection = pymysql.connect(
                user=DB_USER,
                password=DB_PASS,
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )

            result = func(conexion, *args, **kwargs)
            return result
        except Exception as e:
            logging.error(f"Error en la conexión DB: {e}")
            return None
    return wrapper
