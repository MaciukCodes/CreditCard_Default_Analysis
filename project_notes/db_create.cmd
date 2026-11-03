pip install -r requirements.txt
py ./data/unzip_explore.py  # unzips and can give quick stats
py ./src/database/create_db.py  # creates the database with the raw file
py ./src/database/create_cardholder_table.py  # transforms and moves the columns into a new table
