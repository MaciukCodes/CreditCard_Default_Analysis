# Credit Card Default Analysis README


### Overview

This project takes records on clients credit card statements and normalizes them into a SQL database. It separates the card holders and their info into one table and separates each monthly record into a monthly reports table (separating clients records into months)


### Goals

I am trying to display my ability to use SQL as well as Docker (to be incorporated later) and perform basic Database transformations in SQL.

### Tools Used

- Python
- - SQLite3
- - Pandas
- - SQLAlchemy


### Why these tools?

I have plenty of opportunities to display my pandas and python skills however since most of the abilities are able to be done with those I don't get many chances to use SQL. While there where times I could make it easier wth Pandas ( Going from a wide to tall table) I kept with SQL.

### How to Run

1.  Clone the repository.
2. Create and start a virtual environment.
3. Download the zip file from: https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip 
4. Make sure the zip file is inside /data/raw_downloads
3. run the following in command line interface from the project root:  ./project_notes/db_create.cmd

### Future Plans

- Have the database auto correct inputs so all inputs have matching case.
- Add at least one window statement to the monthly report table to show information on the previous month.
