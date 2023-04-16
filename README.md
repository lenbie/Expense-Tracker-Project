# README

*This repository contains tasks from the **Ohjelmistotekniikka 2023** course from Helsingin Yliopisto.*

## Expense Tracker Project

## Python version

Note that Python version 3.10.6 was used for creating and testing this project.

## Documentation

The [timekeeping](https://github.com/lenbie/ot-harjoitustyo/blob/master/documentation/timekeeping.md) document contains information on the hours spent on various project tasks.

The [requirements specification](https://github.com/lenbie/ot-harjoitustyo/blob/master/documentation/requirements_specification.md) document contains the initial requirements defined for the project, including purpose, users and functionalities.

The [changelog](https://github.com/lenbie/ot-harjoitustyo/blob/master/documentation/changelog.md) document contains details on what changes were made to the project during each week of the course, starting from week 3.

## Installation

1. Install dependencies through command line using:

```bash
poetry install
```

2. Perform necessary initialization using:

```bash
poetry run invoke initialize
```

3. Start the application using: 

```bash
poetry run invoke start
```

## Command line functions

### Starting the application

Start the application using: 

```bash
poetry run invoke start
```

### Testing

Run tests using:

```bash
poetry run invoke test
```

### Test Coverage Report

Create the html test coverage report using:

```bash
poetry run invoke coverage-report
```

### Pylint tests

Create the pylint test report using:

```bash
poetry run invoke lint
```