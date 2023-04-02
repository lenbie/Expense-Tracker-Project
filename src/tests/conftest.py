from database_initialization import initialize_database

def pytest_configure():
    initialize_database()