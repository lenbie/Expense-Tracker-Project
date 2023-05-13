# Requirements specification document

## The purpose of the application

My application is a an expense tracker to help users with keeping track of their spending, including how much they spend, when, and on what kinds of things, so they can budget well and spend wisely. Users can input and later edit that information, and choose to view it in a list format or graphically visualized. For a user to use the expense tracker, they need to create an account and sign in with valid credentials. 

## Users

There is a regular user role in the system, which involves being able to make an account with a username and password, and then logging in to only that account with the username and password, and viewing and editing the information associated with that account only. 

## Functionalities

###   Current Functionalities (of the final release)

- When starting the application, a user first see the login page asking for their credentials - username and password - and the option to create a new account
  - If they choose to create a new account, they can set a unique username and a password. The password must be at least 8 characters long and contain at least one number and one special character
  - If they enter invalid credentials, the application will prompt them to enter different, valid credentials meeting the above criteria
  - If they enter valid credentials, they will return to the login page, and after entering their credentials, they can access their expense tracker account
- When a user has accessed their expense tracker account, they can
  - Create new expenses
    - This requires the following information: Name (string), Amount (float), and optionally Category, Date
      - For category, the user can choose the option of creating a new category by entering its name into a text field, or one of their previously created categories from a dropdown menu. If no category is chosen, it will be the default "undefined".
      - For time, the user can input a time in format YYYY-MM-DD, or if left blank, the time will default to the time when the user created the expense
  -  View existing expenses
     - When the user chooses to view their expenses, they see a total of all their entered expenses at the top of the screen
     - The user can choose to view their expenses in a table, or as a graph
     - The table displays rows of individual expenses in chronological order
        -  The user can also choose to view a table of expenses belonging to a selected category, and they will then be listed in chronological order if they belong to that category
    - The graphical representation shows a graph of how the expenses have changed over time
       - he user can choose whether they would like to see how all of their expenses have changed over time, or if they would like to see how the expenses of a category of their choosing have changed over time 
  - Edit their previously created categories
    - The user can view a dropdown menu of the categories they created, and then edit the name of a selected cetegory, or delete the category. Deleting a category with expenses in it will move all those expenses to the predefined category "undefined". Renaming a category retains all expenses within that category, but assigns the new category name to all of them.
  - Edit their previously created expenses
    - When viewing the table of expenses, the user can click on an expense to edit, and edit the expense information of any of the expenses, i.e. the name, amount, date or category of that expense.
- The user can navigate between the different functionalities of the expense tracker by clicking buttons that switch between windows, and by utilizing the expense tracker home screen, which they get to after logging in.
- When the user wishes to exit the application, they can log out of their account from the home screen.

###   Further development ideas	

- The current application could be extended in the following ways:
  - The user can define a budget, a desired spending limit in total or for a certain category. When they add expenses, the application will then be informed how close they are to exceeding that spending limit. This may be in the form of a text information, or a colour displayed (e.g. green for far away, orange for close, and red for reached limit)
  - The user can create expected expenses for a future time, such as expected bills or debts to be paid, which will be marked differently in the list or graph visualization, and factored into the spending limit calculation
  - The user can create shared expenses with other registered users, which will be split amongst them evenly or according to a user-defined split, and then included in each user's own expense calculation. 
  - The shared expense functionality could be combined with the expected expense functionality, if a user owes a debt to another user.
  - An administrative user role could be created, with the ability to add or remove other users, and view and edit regular user's information.
