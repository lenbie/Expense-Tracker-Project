# Requirements specification document

## The purpose of the application

My application is a an expense tracker to help users with keeping track of their spending, both how much they spend and on what kinds of things, so they can budget well and spend wisely. Users can edit that information and choose to view it in a list format or graphically visualized. The application may also include the ability to set a budget (total or per category), and as the user inputs their expenses, they will be informed how close they are to exceeding that budget. For a user to use the expense tracker, they need to create an account and sign in with valid credentials. 

## Users

There is a regular user role in the system, which involves being able to make an account with a username and password, and then logging in to only that account with the username and password, and viewing and editing the information associated with that account only. 

A possible extension to this is creating an administrative user role, with the ability to add or remove other users, and view and edit regular user's information.

## Functionalities

###   Basic Functionalities

- [x] When starting the application, a user will first see the login page asking for their credentials - username and password - and the option to create a new account
  - [x] If they choose to create a new account, they can set a unique username, which must consist of at least 5 characters, and password, which must be at least 8 characters long and contain at least one integer number 
  - [x] If they enter invalid credentials, the application will prompt them to enter different credentials or create a new account
  - [x] If they enter valid credentials, they can then access their expense tracker account
- When a user has accessed their expense tracker account, they can
  - [x] create a new expense
    - [x] This requires the following information: Name (string), Amount (float), and optionally Category, Date
      - [x] For category, the user can choose he option of creating a new category, or one of their previously created categories (see below), or if no category is chosen, it will be the default "undefined".
      - For time, the user can input a time in format YYYY.MM.DD. or choose current time
  - [x] create a new category
    - [x] The user can define a new category by naming it.
  -  view expenses
     - [x] The user can choose to view their expenses in a list, or create a graphical representation
     - [x] The list will have a "total" of all expenses at the top, and then show individual expenses in chronological order
        -  The user can also choose to list expenses by a specified category, and they will then be listed in chronological order if they belong to that category
    -  The graphical representation will show a graph of how the expenses have changed over time
       -  The user can choose whether they would like to see how the total expenses have changed over time, or if they would like to see how the expenses of a certain category have changed over time
  - edit their previously created categories
    - The user can view a list of the categories they created in chronological order and edit the category information, or delete categories. Deleting a category with expenses in it will move all those expenses to the predefined category "undefined".
  - edit their previously created expenses
    - When viewing the list of expenses, the user can then choose an "edit" option and then edit the expense information of any of the expenses, and for example change the name or the category they belong to. This enables users to put old expenses into newly created categories.
- [x] When the user wishes to exit the application, they can log out of their account.

###   Further development ideas	

- Time permitting, the functionalities defined above can be expanded in one or more of the following ways:
  - The user can define a budget, a desired spending limit in total or for a certain category. When they add expenses, the application will then be informed how close they are to exceeding that spending limit. This may be in the form of a text information, or a colour displayed (e.g. green for far away, orange for close, and red for reached limit)
  - The user can create expected expenses for a future time, such as expected bills or debts to be paid, which will be marked differently in the list or graph visualization, and factored into the spending limit calculation
  - The user can create shared expenses with other registered users, which will be split amongst them evenly or according to a user-defined split, and then included in each user's own expense calculation. 
  - The shared expense functionality could be combined with the expected expense functionality, if a user owes a debt to another user.
