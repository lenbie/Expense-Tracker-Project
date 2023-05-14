# README

*This repository contains tasks from the **Ohjelmistotekniikka 2023** course from Helsingin Yliopisto.*

## Expense Tracker Project

The expense tracker is a useful tool for keeping track of past expenses, and seeing how much has been spent and on what.

## Releases
- [**Final release**](https://github.com/lenbie/ot-harjoitustyo/releases/tag/final_release)
- [**Week 6 release**](https://github.com/lenbie/ot-harjoitustyo/releases/tag/viikko6)
- [**Week 5 release**](https://github.com/lenbie/ot-harjoitustyo/releases/tag/viikko5)

## Python version

Note that Python version 3.10.6 was used for creating and testing this project.

## Documentation

The [timekeeping](https://github.com/lenbie/ot-harjoitustyo/blob/master/documentation/timekeeping.md) document contains information on the hours spent on various project tasks.

The [requirements specification](https://github.com/lenbie/ot-harjoitustyo/blob/master/documentation/requirements_specification.md) document contains the initial requirements defined for the project, including purpose, users and functionalities.

The [changelog](https://github.com/lenbie/ot-harjoitustyo/blob/master/documentation/changelog.md) document contains details on what changes were made to the project during each week of the course, starting from week 3.

The [architecture description](https://github.com/lenbie/ot-harjoitustyo/blob/master/documentation/architecture.md) of the application contains information and diagrams on the application's architecture and structure.

The [user manual](https://github.com/lenbie/ot-harjoitustyo/blob/master/documentation/user_manual.md) contains a detailed guide for how to use the application with screenshots of the UI.

The [testing document](https://github.com/lenbie/ot-harjoitustyo/blob/master/documentation/testing_document.md) provides detail on how the application was tested.

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
