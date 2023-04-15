from services.login_service import LoginService
from repositories.expense_repository import ExpenseRepository
from entities.user import User
from entities.expense import Expense
from entities.category import Category
from datetime import date

class ExpenseService:
    def __init__(self, expense_repository=ExpenseRepository, logged_in_user = User):
        self.expense_repository = expense_repository
        self.current_user = logged_in_user
    
    def create_new_expense(self, name, amount, date = date.today(), category = "undefined"):
        expense_name = str(name)
        expense_amount = float(amount)
        expense_date = str(date)
        expense_category = str(category)

        new_expense = Expense(expense_name, expense_amount, expense_date, expense_category)

        self.expense_repository.add_expense(self.current_user, new_expense)


        

        

