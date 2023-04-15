from database_connection import connect_to_database
from entities.user import User
from entities.expense import Expense
from entities.category import Category

class ExpenseRepository:
    def __init__(self):
        self._connection = connect_to_database()
    
    def add_expense(self, user = User, expense = Expense):
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
    
    def find_expense(self, user = User, expense = Expense):

        cursor = self._connection.cursor()

        select = ("""
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
                category=?""")
    
        cursor.execute(select, (user.username, expense.name, expense.amount, expense.date, expense.category))
            
        found = cursor.fetchone()

        return found
    
    def delete_expense(self, user = User, expense = Expense):
        cursor = self._connection.cursor()

        delete = ("""
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
                category=?""")
    
        cursor.execute(delete, (user.username, expense.name, expense.amount, expense.date, expense.category))

        self._connection.commit()
    
    def delete_all_expenses(self):
        cursor = self._connection.cursor()

        cursor.execute("""
        delete from expenses;
        """)

        self._connection.commit()
    
    def get_all_expenses_in_table(self):
        cursor = self._connection.cursor()

        cursor.execute("""
        select * from expenses
        """)

        found = cursor.fetchall()

        return found

    def get_all_expenses_by_user(self, user = User):
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
           username=:c""",
                    {"c": user.username}
        )
        found = cursor.fetchall()

        return found
    
    def get_all_expenses_by_category_and_user(self, user = User, category = Category):
        cursor = self._connection.cursor()

        find_all=("""
        select
            name,
            amount,
            date
        from 
            expenses
        where
           username=?
        and
            category=?
        """)

        cursor.execute(find_all, (user.username, category.name))
        found = cursor.fetchall()

        return found
        

#these may acc be for expense service (get total --> find all from user and then add, or from user and category)
#and edit expense is just delete old one and add new expense with changed value

    #def get_total_all_expenses(self):
    
    #def get_total_by_category(self):
    
    #def edit_expense_name(self):
    
    #def edit_expense_amount(self):

    #def edit_expense_category(self):
    
    #def edit_expense_date(self):

