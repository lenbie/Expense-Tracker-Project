from datetime import date
from repositories.expense_repository import ExpenseRepository
from entities.user import User
from entities.expense import Expense
from entities.category import Category


class ExpenseService:

    """
    This class manages the expense tracking functions of the application.
    Its functions for creating, editing and viewing expense information are
    user-specific for the current logged in user.
    """

    def __init__(self, expense_repository=ExpenseRepository, logged_in_user=User):
        self.expense_repository = expense_repository
        self.current_user = logged_in_user

    def create_new_expense(self, name, amount, given_date=date.today(), category="undefined"):
        expense_name = str(name)
        expense_amount = float(amount)
        expense_date = str(given_date)
        expense_category = str(category)

        new_expense = Expense(expense_name, expense_amount,
                              expense_date, expense_category)

        self.expense_repository.add_expense(self.current_user, new_expense)

    def check_input_validity_expense_amount(self, amount):
        try:
            amount = float(amount)
        except ValueError as exc:
            raise InvalidInputError(
                """Invalid input. Make sure you have entered a nonnegative
                numeric amount and a valid date in YYYY-MM-DD format""") from exc

    def check_input_validity_expense_date(self, given_date):
        try:
            date.fromisoformat(given_date)
        except ValueError as exc:
            raise InvalidInputError(
                """Invalid input. Make sure you have entered a nonnegative
                numeric amount and a valid date in YYYY-MM-DD format""") from exc

    def edit_expense_name(self, new_expense_name, expense=Expense):
        found = self.expense_repository.find_expense(
            self.current_user, expense)
        if found:
            old_expense = Expense(
                found["name"], found["amount"], found["date"], found["category"])
            self.expense_repository.delete_expense(
                self.current_user, old_expense)

            new_expense = Expense(
                str(new_expense_name), found["amount"], found["date"], found["category"])
            self.expense_repository.add_expense(self.current_user, new_expense)
            return True
        return False

    def edit_expense_amount(self, new_expense_amount, expense=Expense):
        found = self.expense_repository.find_expense(
            self.current_user, expense)
        if found:
            old_expense = Expense(
                found["name"], found["amount"], found["date"], found["category"])
            self.expense_repository.delete_expense(
                self.current_user, old_expense)

            new_expense = Expense(found["name"], float(
                new_expense_amount), found["date"], found["category"])
            self.expense_repository.add_expense(self.current_user, new_expense)
            return True
        return False

    def edit_expense_category(self, new_category_name, expense=Expense):
        found = self.expense_repository.find_expense(
            self.current_user, expense)
        if found:
            old_expense = Expense(
                found["name"], found["amount"], found["date"], found["category"])
            self.expense_repository.delete_expense(
                self.current_user, old_expense)

            new_expense = Expense(
                found["name"], found["amount"], found["date"], str(new_category_name))
            self.expense_repository.add_expense(self.current_user, new_expense)
            return True
        return False

    def edit_expense_date(self, new_expense_date, expense=Expense):
        found = self.expense_repository.find_expense(
            self.current_user, expense)
        if found:
            old_expense = Expense(
                found["name"], found["amount"], found["date"], found["category"])
            self.expense_repository.delete_expense(
                self.current_user, old_expense)

            new_expense = Expense(found["name"], found["amount"], str(
                new_expense_date), found["category"])
            self.expense_repository.add_expense(self.current_user, new_expense)
            return True
        return False

    def delete_expense(self, expense=Expense):
        found = self.expense_repository.find_expense(
            self.current_user, expense)

        if found:
            self.expense_repository.delete_expense(self.current_user, expense)
            return True
        return False

    def delete_category(self, category=Category):
        all_expenses = self.expense_repository.get_all_expenses_by_category_and_user(
            self.current_user, category)

        if all_expenses:
            for expense in all_expenses:
                old_expense = Expense(
                    expense["name"], expense["amount"], expense["date"], expense["category"])
                self.expense_repository.delete_expense(
                    self.current_user, old_expense)

                new_expense = Expense(
                    expense["name"], expense["amount"], expense["date"], "undefined")
                self.expense_repository.add_expense(
                    self.current_user, new_expense)
            return True
        return False

    def rename_category(self, new_category_name, category=Category):
        all_expenses = self.expense_repository.get_all_expenses_by_category_and_user(
            self.current_user, category)

        if all_expenses:
            for expense in all_expenses:
                old_expense = Expense(
                    expense["name"], expense["amount"], expense["date"], expense["category"])
                self.expense_repository.delete_expense(
                    self.current_user, old_expense)

                new_expense = Expense(
                    expense["name"], expense["amount"], expense["date"], str(new_category_name))
                self.expense_repository.add_expense(
                    self.current_user, new_expense)
            return True
        return False

    def get_total_all_expenses_by_user(self):
        all_expenses = self.expense_repository.get_all_expenses_by_user(
            self.current_user)
        total = 0
        for expense in all_expenses:
            total += expense["amount"]
        return total

    def get_total_by_category_and_user(self, category=Category):
        all_expenses = self.expense_repository.get_all_expenses_by_category_and_user(
            self.current_user, category)
        total = 0
        for expense in all_expenses:
            total += expense["amount"]
        return total

    def list_all_expenses(self):
        all_expenses = self.expense_repository.get_all_expenses_by_user(
            self.current_user)
        list_of_expenses = []

        for expense in all_expenses:
            listed_expense = Expense(
                expense["name"], expense["amount"], expense["date"], expense["category"])
            list_of_expenses.append(listed_expense)

        return list_of_expenses

    def list_expenses_by_category(self, category=Category):
        all_expenses = self.expense_repository.get_all_expenses_by_category_and_user(
            self.current_user, category)
        list_of_expenses = []

        for expense in all_expenses:
            listed_expense = Expense(
                expense["name"], expense["amount"], expense["date"], expense["category"])
            list_of_expenses.append(listed_expense)

        return list_of_expenses

    def list_all_categories(self):
        all_expenses = self.expense_repository.get_all_expenses_by_user(
            self.current_user)
        if all_expenses:
            list_of_categories = set()

            for expense in all_expenses:
                list_of_categories.add(expense["category"])

            return list_of_categories
        return []


class InvalidInputError(Exception):
    pass
