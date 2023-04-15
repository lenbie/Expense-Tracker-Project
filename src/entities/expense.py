from datetime import date

class Expense:
    """"

    Class representing an Expense entered into the Expense tracker

    Attributes:
        name (string): The name given to the expense by the user
        amount (float): The monetary amount of the expense
        date: The date of the expense, default being the current system date
        category: The category of the expense, default being undefined

    """

    def __init__(self, name=str, amount=float, date=date.today(), category="undefined"):
        self.name = name
        self.amount = amount
        self.date= date
        self.category = category
