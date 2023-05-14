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

    def __init__(self, name, amount, given_date=date.today(), category="undefined"):
        """Class constructor

        Args:
            name (str): The expense name
            amount (float): The expense amount
            given_date (str, optional): The expense date. Defaults to date.today().
            category (str, optional): The expense category. Defaults to "undefined".
        """
        self.name = name
        self.amount = amount
        self.date = given_date
        self.category = category
