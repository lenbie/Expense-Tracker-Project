class Category:
    """
    Class defining an expense category

    Attributes:
        name: The name of the category, default being undefined
    """

    def __init__(self, name="undefined"):
        """Class constructor

        Args:
            name (str, optional): The category's name Defaults to "undefined".
        """
        self.name = name
