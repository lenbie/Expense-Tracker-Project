from tkinter import ttk, constants, messagebox
from services.login_service import login_service, UsernameNotUniqueError, IncorrectPasswordFormatError


class CreateAccountView:
    def __init__(self, root, handle_expense_tracker, handle_login):
        self._root = root
        self._handle_expense_tracker = handle_expense_tracker
        self._handle_login = handle_login
        self._frame = None
        self._style = None

        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._style = ttk.Style()
        self._style.configure("TFrame", background="#AFE4DE")

        header_label = ttk.Label(
            master=self._frame, text="Create a new account", background="#AFE4DE")

        username_label = ttk.Label(
            master=self._frame, text="Choose a username", background="#AFE4DE")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(
            master=self._frame, text="Choose a password", background="#AFE4DE")
        self._password_entry = ttk.Entry(master=self._frame)
        password_info_label = ttk.Label(
            master=self._frame, text="""Your password must be at least 8 characters long and contain at least 1 number and 1 special character""", background="#AFE4DE")

        create_account_and_continue_button = ttk.Button(
            master=self._frame, text="Create account and continue to expense tracker", command=self._handle_create_account_and_login_button_click)
        return_to_login_button = ttk.Button(
            master=self._frame, text="Return to Login", command=self._handle_login)

        header_label.grid(columnspan=2, sticky=(constants.N), padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_info_label.grid(
            column=1, columnspan=2, sticky=(constants.N), padx=5, pady=5)

        create_account_and_continue_button.grid(
            columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        return_to_login_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=200)

    def configure(self):
        self._frame.pack(fill=constants.X)
        self._root.configure(background="#AFE4DE")

    def destroy(self):
        self._frame.destroy()

    def _handle_create_account_and_login_button_click(self):
        username_value = self._username_entry.get()
        password_value = self._password_entry.get()

        try:
            login_service.create_new_user(username_value, password_value)
            self._handle_expense_tracker()

        except IncorrectPasswordFormatError:
            self._display_error_message("Incorrect password format")

        except UsernameNotUniqueError:
            self._display_error_message(
                "User with this username exists already")

    def _display_error_message(self, message):
        messagebox.showerror("Error", message)
