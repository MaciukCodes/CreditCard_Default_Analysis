# Credit Card Default Analysis README


### Overview

This project takes records on clients credit card statements and normalizes them into a SQL database. It separates the card holders and their info into one table and separates each monthly record into a monthly reports table (separating clients records into months) all within a docker container.


### Goals

I am trying to display my ability to use SQL as well as Docker and perform basic Database transformations in SQL.

### Tools Used

- Python
- - SQLite3
- - Pandas
- - SQLAlchemy
- - Docker
- - Requests


### Why these tools?

I have plenty of opportunities to display my pandas and python skills however since most of the abilities are able to be done with those I don't get many chances to use SQL. While there where times I could make it easier wth Pandas ( Going from a wide to tall table) I kept with SQL.


### How to run

1. Clone the repository
  - - git clone https://github.com/MaciukCodes/CreditCard_Default_Analysis.git
  - - cd CreditCard_Default_Analysis
2.  Build the image from the Dockerfile
- - docker build -t cc_card_analysis .
3. Run the container from the image
- - docker run  cc_card_analysis


### How to Run no docker

1.  Clone the repository.
2. Create and start a virtual environment.
3. run the following in command line interface from the project root inside python: 
- - from  src.main import run_all
- - run_all()

### Future Plans

- Have the database auto correct inputs so all inputs have matching case.
- Add at least one window statement to the monthly report table to show information on the previous month.
