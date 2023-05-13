from tkinter import ttk, constants, messagebox
from services.login_service import login_service, InvalidCredentialsError


class LoginView:
    """This class manages the UI view for user login
    """

    def __init__(self, root, handle_create_account, handle_start_expense_tracker):
        """Class constructor, creating the login view

        Args:
            root (Tkinter frame): The Tkinter frame within which the login view resides
            handle_create_account: Callable value, called when the user clicks the "Create new account" button
            handle_start_expense_tracker: Callable value, called when the user logs in with valid credentials
        """
        self._root = root
        self._handle_create_account = handle_create_account
        self._handle_start_expense_tracker = handle_start_expense_tracker
        self._frame = None
        self._style = None

        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_window_size()

        self._style = ttk.Style()
        self._style.configure("TFrame", background="#AFE4DE")

        header_label = ttk.Label(
            master=self._frame, text="Welcome to the Expense Tracker!", background="#AFE4DE")

        username_label = ttk.Label(
            master=self._frame, text="Username", background="#AFE4DE")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(
            master=self._frame, text="Password", background="#AFE4DE")
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._handle_login_button_click)
        create_account_button = ttk.Button(
            master=self._frame, text="Create new account", command=self._handle_create_account)

        header_label.grid(columnspan=2, sticky=(constants.N), padx=5, pady=5)

        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        login_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        create_account_button.grid(columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)

    def _initialize_window_size(self):
        window_width = self._root.winfo_screenwidth()//2
        window_height = self._root.winfo_screenheight()//4
        screen_width = (self._root.winfo_screenwidth() // 2) - \
            (window_width//2)
        screen_height = (self._root.winfo_screenheight() //
                         2) - (window_height//2)

        self._root.geometry(
            f"{int(window_width)}x{int(window_height)}+{int(screen_width)}+{int(screen_height)}")

    def configure(self):
        """Shows the login view
        """
        self._frame.pack(fill=constants.X)
        self._root.configure(background="#AFE4DE")

    def destroy(self):
        """Destroys the login view
        """
        self._frame.destroy()

    def _handle_login_button_click(self):
        username_value = self._username_entry.get()
        password_value = self._password_entry.get()

        if username_value and password_value:
            try:
                login_service.login_user(username_value, password_value)
                self._handle_start_expense_tracker()

            except InvalidCredentialsError:
                self._display_error_message(
                    "Invalid credentials. Please try again")

    def _display_error_message(self, message):
        messagebox.showerror("Error", message)
