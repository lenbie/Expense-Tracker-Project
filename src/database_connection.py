import sqlite3
from config import EXPENSES_FILE_PATH

connection = sqlite3.connect(EXPENSES_FILE_PATH)
connection.row_factory=sqlite3.Row

def connect_to_database():
    return connection