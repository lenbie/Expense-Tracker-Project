# Changelog

### Week 3

- The environment variables and database setup were configured.
- The initial versions of entity classes User, Expense, Category were created.
- The UserRepository class was added, which stores usernames and passwords in a SQLite database. Functionality includes adding a new user, finding a user by username, finding and deleting all users.
- The ExpenseService class was added, which currently allows the creation of a new user, the validation whether their password is strong enough and an existing user's credentials.
- The user is able to use the command line to create a new account.
- Tests for the current functionality UserRepository and ExpenseService were added.



