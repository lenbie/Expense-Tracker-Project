from datetime import date
from repositories.expense_repository import ExpenseRepository
from entities.user import User
from entities.expense import Expense
from entities.category import Category


class ExpenseService:

    """
    This class manages the expense tracking functions of the application.
    It includes methods for creating, editing and viewing expense information are
    user-specific for the current logged in user.
    """

    def __init__(self, expense_repository=ExpenseRepository, logged_in_user=User):
        """Class constructor

        Args:
            expense_repository (ExpenseRepository object):
                                Object with methods of ExpenseRepository class,
                                handling database operations
            logged_in_user (User object): The current logged-in user whose expenses will be managed.
                                            The user object includes their username and password.
        """
        self.expense_repository = expense_repository
        self.current_user = logged_in_user

    def create_new_expense(self, name, amount, given_date=str(date.today()), category="undefined"):
        """Creates a new expense

        Args:
            name (str): Name of the new expense
            amount (str, int or float): Amount of the new expense
            given_date (optional): Date of the new expense. Defaults to date.today().
            category (str, optional): Category of the new expense. Defaults to "undefined".
        """
        expense_name = str(name)

        self.check_input_validity_expense_amount(amount)
        expense_amount = float(amount)

        if not given_date:
            expense_date = str(date.today())
        else:
            expense_date = str(given_date)
            self.check_input_validity_expense_date(expense_date)

        expense_category = str(category)
        new_expense = Expense(expense_name, expense_amount,
                              expense_date, expense_category)

        self.expense_repository.add_expense(self.current_user, new_expense)

    def check_input_validity_expense_amount(self, amount):
        """Checks whether the amount to be entered into database is nonnegative and numeric 

        Args:
            amount (str, int or float): The amount to be entered into database

        Raises:
            InvalidInputError: An error that occurs when the amount
            and/or date details entered into database are invalid
        """
        try:
            amount = float(amount)
        except ValueError as exc:
            raise InvalidInputError(
                """Invalid input. Make sure you have entered a nonnegative
                numeric amount and a valid date in YYYY-MM-DD format""") from exc

        if amount < 0:
            raise InvalidInputError("""Invalid input. Make sure you have entered a nonnegative
                numeric amount and a valid date in YYYY-MM-DD format""")

    def check_input_validity_expense_date(self, given_date):
        """Checks whether the date to be entered into database is a valid date.

        Args:
            given_date (str, int or float): The date to be entered into database

        Raises:
            InvalidInputError:  An error that occurs when the amount
            and/or date details entered into database are invalid
        """
        try:
            date.fromisoformat(given_date)
        except ValueError as exc:
            raise InvalidInputError(
                """Invalid input. Make sure you have entered a nonnegative
                numeric amount and a valid date in YYYY-MM-DD format""") from exc

    def edit_expense_name(self, new_expense_name, expense=Expense):
        """Changes the name of an existing expense

        Args:
            new_expense_name (str): The new expense name
            expense (Expense object): The expense to be edited

        Returns:
            True, if the expense name has been successfully changed
            False, if the expense to be edited does not exist
        """
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
        """Changes the amount of an existing expense if the new amount is valid

        Args:
            new_expense_amount (str, int or float): The new expense amount
            expense (Expense object): The expense to be edited
        Returns:
            True, if the expense amount has been successfully changed
            False, if the expense to be edited does not exist
        """
        found = self.expense_repository.find_expense(
            self.current_user, expense)
        if found:
            self.check_input_validity_expense_amount(new_expense_amount)

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
        """Changes the category of an existing expense

        Args:
            new_category_name (str): The new expense category name
            expense (Expense object): The expense to be edited
        Returns:
            True, if the expense category has been successfully changed
            False, if the expense to be edited does not exist
        """
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
        """Changes the date of an existing expense if the new date is valid

        Args:
            new_expense_date (str): The new expense date
            expense (Expense object): The expense to be edited
        Returns:
            True, if the expense date has been successfully changed
            False, if the expense to be edited does not exist
        """
        found = self.expense_repository.find_expense(
            self.current_user, expense)
        if found:
            self.check_input_validity_expense_date(new_expense_date)
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
        """Deletes a specified expense

        Args:
            expense (Expense object): The expense to be deleted,
                        including name, amount, date, category

        Returns:
            True, if the expense exists and could be deleted
            False, if the expense to be deleted does not exist
        """
        found = self.expense_repository.find_expense(
            self.current_user, expense)

        if found:
            self.expense_repository.delete_expense(self.current_user, expense)
            return True
        return False

    def delete_category(self, category=Category):
        """Deletes a specified category and adds all expenses
        within that category to the "undefined" category

        Args:
            category (Category object): The category to be deleted

        Returns:
            False, if no expenses within that category exist for the current user
            True, otherwise
        """
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
        """Renames a specified category

        Args:
            new_category_name (str): The new category name
            category (Category object): The category to be renamed

        Returns:
            False, if no expenses within that category exist for the current user
            True, otherwise
        """
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
        """Calculates and returns the total amount of all expenses of the current user.

        Returns:
            The total amount of all expenses of the current user, as an integer.
        """
        all_expenses = self.expense_repository.get_all_expenses_by_user(
            self.current_user)
        total = 0
        for expense in all_expenses:
            total += expense["amount"]
        return total

    def get_total_by_category_and_user(self, category=Category):
        """Calculates and returns the total amount of all expenses wihthin a
        specified category, belonging to the current user.

        Args:
            category (Category object): The category whose expense total is to be calculated

        Returns:
            The total amount of all expenses in that category, as an integer.
        """
        all_expenses = self.expense_repository.get_all_expenses_by_category_and_user(
            self.current_user, category)
        total = 0
        for expense in all_expenses:
            total += expense["amount"]
        return total

    def list_all_expenses(self):
        """Returns a list of all expenses belonging to the current user

        Returns:
            A list of all the current user's expenses
        """
        all_expenses = self.expense_repository.get_all_expenses_by_user(
            self.current_user)
        list_of_expenses = []

        for expense in all_expenses:
            listed_expense = [expense["name"], expense["amount"],
                              expense["date"], expense["category"]]
            list_of_expenses.append(listed_expense)

        return list_of_expenses

    def list_expenses_by_category(self, category=Category):
        """Returns a list of all expenses belonging to a specified category
        and the current user

        Args:
            category (Category object): The category whose expenses are to be listed

        Returns:
            List of expenses within the specified category
        """
        all_expenses = self.expense_repository.get_all_expenses_by_category_and_user(
            self.current_user, category)
        list_of_expenses = []

        for expense in all_expenses:
            listed_expense = [expense["name"], expense["amount"],
                              expense["date"], expense["category"]]
            list_of_expenses.append(listed_expense)

        return list_of_expenses

    def list_all_categories(self):
        """Returns a list of categories belonging to the current user

        Returns:
            List of categories of the current user, or
            an empty list if that user has no created expenses
        """
        all_expenses = self.expense_repository.get_all_expenses_by_user(
            self.current_user)
        if all_expenses:
            set_of_categories = set()
            list_of_categories = []

            for expense in all_expenses:
                set_of_categories.add(expense["category"])

            for category in set_of_categories:
                list_of_categories.append(category)

            list_of_categories.sort()

            return list_of_categories
        return []

    def graph_all_expenses(self):
        """Returns a line graph of all expenses of the current user by their amount over time

        Returns:
            The plot of a pandas dataframe, representing that graph
        """
        dataframe = self.expense_repository.get_all_expenses_as_pandas_dataframe()
        user_dataframe = dataframe[dataframe["username"]
                                   == self.current_user.username]
        expense_graph = user_dataframe.plot(x="date", y="amount",
                            kind="line", xlabel="Expense Date", ylabel="Expense Amount",
                                    legend=False, figsize=(13, 5), style='-o')
        return expense_graph

    def graph_expenses_by_category(self, category=Category):
        """Returns a line graph of the expenses of a specified category
        of the current user by their amount over time

        Args:
            category (Category object): The category whose expenses are to be plotted

        Returns:
            The plot of a pandas dataframe, representing that graph
        """
        dataframe = self.expense_repository.get_all_expenses_as_pandas_dataframe()
        user_dataframe = dataframe[(dataframe["username"] == self.current_user.username) & (
            dataframe["category"] == category.name)]
        expense_graph = user_dataframe.plot(
            x="date", y="amount", kind="line", xlabel="Expense Date",
            ylabel="Expense Amount", legend=False, figsize=(13, 5), style='-o')
        return expense_graph


class InvalidInputError(Exception):
    pass
