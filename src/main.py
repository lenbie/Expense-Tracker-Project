from entities.user import User
from repositories.user_repository import UserRepository
from database_initialization import initialize_database
from services.expense_service import ExpenseService


print("""
    NOTE: This is a temporary version of main.py
    for starting the program before the necessary UI exists.
""")
      
initialize_database()

print("Would you like")

start_repository=UserRepository()
start_expense_service=ExpenseService(start_repository)

print("""
    The current functionality allows you to create a new user account.
""")
      
print("""
    If you would like to create an account,
    please answer the next questions.
""")
    
username=str(input("Choose a username"))

password=str(input("""
    Choose a password. It must be at least 8 characters long,
    and include at least 1 number and 1 special character"""))

start_expense_service.create_new_user(username, password)
