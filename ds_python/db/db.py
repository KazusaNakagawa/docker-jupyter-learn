import os
import pandas as pd

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error
from sqlalchemy.engine import create_engine

load_dotenv()

mysql_root_user = os.getenv("MYSQL_ROOT_USER")
mysql_user = os.getenv("MYSQL_USER")
mysql_root_password = os.getenv("MYSQL_ROOT_PASSWORD")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_database = os.getenv("MYSQL_DATABASE")
db_port = os.getenv("DB_PORT")
database = os.getenv("DATABASE")


def load_env():
    return mysql_root_user, mysql_user, mysql_root_password, mysql_password, mysql_database, db_port, database
