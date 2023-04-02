import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)
try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

EXPENSES_FILE=os.getenv("EXPENSE_FILE") or "expenses.csv"
EXPENSES_FILE_PATH=os.path.join(dirname, "..", "data", EXPENSES_FILE)

DATABASE_FILE = os.getenv("DATABASE_FILE") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILE)
