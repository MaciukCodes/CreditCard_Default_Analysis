#  %% #* imports
import sqlite3 as sql
from pathlib import Path
import pandas as pd

if __name__ == 'src.insert_raw_data':
    from src.db_query_utils import case_creation, sql_base_query, sql_insert
else:
    from db_query_utils import case_creation, sql_base_query, sql_insert
    

#  %% #* file locations

ROOT = Path(__file__).parents[1]

db_location = ROOT / 'data' / 'database' / 'default_cc_clients.db'
xls_file = ROOT / 'data' / 'default of credit card clients.xls'


# %% #* function start
def insert_raw_data():

    # %% #* raw data retrieval

    df_file = pd.read_excel(xls_file, sheet_name='Data', skiprows=1)
    df_columns = list( df_file.keys().str.replace(' ', '_').str.replace('0', '1'))


    db_values = []

    for i, j in df_file.iterrows():
            db_values.append(str(tuple(j)))

    values = f"VALUES {', '.join(db_values)}"

    # for some reason keyword arguments do not work properly in sql_insert
    insert_query = sql_insert('raw_data', values, *df_columns)

    check_query = sql_base_query("raw_data", '1') + "LIMIT 1"


    # %% #* function executable


    with sql.connect(db_location) as db:
        result = db.execute(check_query).fetchone()

        if result is None:
            db.execute(insert_query)
        else:
            print('Table already contains data please use a empty table.')