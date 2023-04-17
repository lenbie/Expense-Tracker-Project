from tkinter import ttk, constants

class ExpenseTrackerView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_return_to_login = handle_login
        self._frame = None
        self._style = None
        
        self._initialize()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._style = ttk.Style()
        self._style.configure("TFrame", background = "#AFE4DE")

        header_label = ttk.Label(master = self._frame, text = "Your Expense Tracker", background ="#AFE4DE")

        create_expense_button = ttk.Label(master=self._frame, text = "Create new expense")
        create_expense_label = ttk.Label(master=self._frame, text = "Functionality for e.g. creating and editing expenses is present in application logic but not yet accessible via the UI")

        header_label.grid(columnspan=2, sticky=(constants.N), padx=5, pady=5)

        create_expense_button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        create_expense_label.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

    def configure(self):
        self._frame.pack(fill=constants.X)
        self._root.configure(background="#AFE4DE")
    
    def destroy(self):
        self._frame.destroy()