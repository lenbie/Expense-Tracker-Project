# Changelog

### Week 3

- The environment variables and database setup were configured.
- The initial versions of entity classes User, Expense, Category were created.
- The UserRepository class was added, which stores usernames and passwords in a SQLite database. Functionality includes adding a new user, finding a user by username, finding and deleting all users.
- The ExpenseService class was added, which currently allows the creation of a new user, the validation whether their password is strong enough and an existing user's credentials.
- The user is able to use the command line to create a new account.
- Tests for the current functionality UserRepository and ExpenseService were added.

### Week 4
- The user can create an account and/or log in, using the graphical UI
- The user can create a new expense using the graphical UI
- The user can log out of the expense tracker using the graphical UI
- The ExpenseService class was refactored, it is now split into LoginService (renamed from week 3's ExpenseService) and ExpenseService
- The LoginService class was extended to allow a user to log in and out
- The ExpenseRepository class for saving a user's expenses in a SQLite database was created
- The ExpenseService functionality was built to allow a user to create, edit and delete expenses and expense categories. Users can further view expenses as lists and get the total of their entered expenses, either overall or per category.
- Tests covering most of the current functionality of the LoginService, ExpenseService, UserRepository, ExpenseRepository were created

### Week 5
- The user can view all their created expenses chronologically in a table in the graphical UI
- The user can see the total of all their created expenses in the graphical UI
- The user can view all expenses per selected category chronologically in the graphical UI
- The user can edit their expenses (expense name, amount, date, category) in the graphical UI
- The UI classes were refactored, creating more separated windows for the user to see and simplifying the code structure
- The ExpenseRepository class now includes functionality to retrieve data as a Pandas dataframe
- Other minor improvements were made to the ExpenseService class and UI classes
