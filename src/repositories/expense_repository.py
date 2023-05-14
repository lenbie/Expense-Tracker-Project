import pandas as pd
from database_connection import connect_to_database
from entities.user import User
from entities.expense import Expense
from entities.category import Category


class ExpenseRepository:
    """ This class is responsible for operations on the expenses database table.
    """

    def __init__(self):
        """Class constructor
        """
        self._connection = connect_to_database()

    def add_expense(self, user: User, expense: Expense):
        """Adds new expense for a user into database

        Args:
            user (User object): The user, whose expense will be added
            expense (Expense object): The Expense object includes information
            on the expense name, amount, date and category to be added to database
        """
        cursor = self._connection.cursor()

        cursor.execute("""
            insert into expenses
                (username,
                name,
                amount,
                date,
                category)
            values (?, ?, ?, ?, ?)""",
                (user.username, expense.name, expense.amount, expense.date, expense.category))

        self._connection.commit()

    def find_expense(self, user: User, expense: Expense):
        """Finds a specified expense in database and returns database row object 

        Args:
            user (User object): The user, whose expense should be found
            expense (Expense object): The Expense object includes information
            on the expense name, amount, date and category to be found from database

        Returns:
            The found expense as a database row object, or None if not found
        """
        cursor = self._connection.cursor()

        select = """
            select
                username,
                name,
                amount,
                date,
                category
            from
                expenses
            where
                username=?
            and
                name=?
            and
                amount=?
            and 
                date=?
            and
                category=?"""

        cursor.execute(select, (user.username, expense.name,
                       expense.amount, expense.date, expense.category))

        found = cursor.fetchone()

        return found

    def delete_expense(self, user: User, expense: Expense):
        """Deletes a specified expense belonging to a specified user

        Args:
            user (User object): The user, whose expense should be deleted
            expense (Expense object): The Expense object includes information
            on the expense name, amount, date and category to be deleted from database
        """
        cursor = self._connection.cursor()

        delete = """
            delete from
                expenses
            where
                username=?
            and
                name=?
            and
                amount=?
            and 
                date=?
            and
                category=?"""

        cursor.execute(delete, (user.username, expense.name,
                       expense.amount, expense.date, expense.category))

        self._connection.commit()

    def delete_all_expenses(self):
        """Deletes all expenses in database table
        """
        cursor = self._connection.cursor()

        cursor.execute("""
        delete from expenses;
        """)

        self._connection.commit()

    def get_all_expenses_in_table(self):
        """Returns all entries in the database expenses table

        Returns:
            List of database rows in the expenses table
        """
        cursor = self._connection.cursor()

        cursor.execute("""
        select * from expenses
        """)

        found = cursor.fetchall()

        return found

    def get_all_expenses_by_user(self, user: User):
        """Returns all expenses belonging to a specified user

        Args:
            user (User object): The user, whose expenses should be found

        Returns:
            List of expenses belonging to the specified user
        """
        cursor = self._connection.cursor()

        cursor.execute("""
        select
            name,
            amount,
            date,
            category
        from 
            expenses
        where
           username=:c
        order by
            date desc""",
                       {"c": user.username}
                       )
        found = cursor.fetchall()

        return found

    def get_all_expenses_by_category_and_user(self, user: User, category: Category):
        """Returns all expenses within a specified category belonging to a certain user

        Args:
            user (User object): The user, whose expenses should be found
            category (Category object): Expenses belonging to this category will be found 

        Returns:
            List of expenses of a certain user belonging to a certain category
        """
        cursor = self._connection.cursor()

        find_all = """
        select
            name,
            amount,
            date, 
            category
        from 
            expenses
        where
           username=?
        and
            category=?
        order by
            date desc
        """

        cursor.execute(find_all, (user.username, category.name))
        found = cursor.fetchall()

        return found

    def get_all_expenses_as_pandas_dataframe(self):
        """Returns a pandas dataframe with all expenses in the database

        Returns:
            Pandas dataframe of all expenses in database expenses table
        """
        dataframe = pd.read_sql_query(
            "SELECT username, name, amount, date, category from expenses", self._connection)
        return dataframe
