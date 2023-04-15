from repositories.user_repository import UserRepository
from services.expense_service import ExpenseService

print("""
    NOTE: This is a temporary version of main.py
    for starting the program before the necessary UI exists.
""")

start_repository = UserRepository()
start_expense_service = ExpenseService(start_repository)

print("""
    The current functionality allows you to create a new user account.
""")

print("""
    If you would like to create an account,
    please answer the next questions.
""")

USERNAME = str(input("""
    Choose a username: """))

PASSWORD = str(input("""
    Choose a password. It must be at least 8 characters long,
    and include at least 1 number and 1 special character.

    Insert password here: """))

start_expense_service.create_new_user(USERNAME, PASSWORD)

found = start_repository.find_user(USERNAME)

if found is not None and found["username"] is USERNAME:
    print("User account successfully created. Thank you!")
