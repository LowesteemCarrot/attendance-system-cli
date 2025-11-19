import mysql.connector
from attendance.utils.config import load_config

cfg = load_config()

def get_db():
    return mysql.connector.connect(
        host=cfg["host"],
        user=cfg["user"],
        password=cfg["password"],
        database=cfg["database"]
    )
