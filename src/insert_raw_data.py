#  %% #* imports
import sqlite3 as sql
from pathlib import Path
import pandas as pd

if __name__ == '__main__':
    from db_query_utils import case_creation, sql_base_query, sql_insert
else:
    from src.db_query_utils import case_creation, sql_base_query, sql_insert


#  %% #* file locations

ROOT = Path(__file__).parents[1]

db_location = ROOT / 'data' / 'database' / 'default_cc_clients.db'
xls_file = ROOT / 'data' / 'default of credit card clients.xls'

# %% #* raw data retrieval

df_file = pd.read_excel(xls_file, sheet_name='Data', skiprows=1)
df_columns = list( df_file.keys().str.replace(' ', '_').str.replace('0', '1'))


db_values = []

for i, j in df_file.iterrows():
        db_values.append(str(tuple(j)))

# values = f"(VALUES ({', '.join(db_values)}))"

values = 'tuna'



insert_query = sql_insert('raw_data', values=values, *df_columns)


print(insert_query[0:555])