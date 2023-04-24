# Architecture of the Application

## Structure

The structure of the application represented as a package diagram:

![Packaging diagram of the application's structure](./images/class_diagram.png)

## Application Logic

### Creating a User 

The user first chooses and enters their desired username and password, and then clicks "Create account and continue to login" if they want to create an account with those credentials. The following sequence diagram describes the process of user creation in application logic.

```mermaid

    sequenceDiagram
        actor User
        User->>UI: enter credentials and click Create account button
        UI->>LoginService: create_new_user(username, password), e.g. ("Alice", "abcd1234!")
        LoginService->>UserRepository: find_user("Alice")
        UserRepository-->>LoginService: None
        LoginService+->>LoginService: validate_password("abcd1234!")
        LoginService-->>LoginService: True
        deactivate LoginService
        LoginService->>Alice: User("Alice", "abcd1234!")
        LoginService->>UserRepository: add_user(Alice)
        UI->>UI: _show_login_view()

```