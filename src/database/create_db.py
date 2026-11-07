# %% #* imports
import sqlite3 as sql
from pathlib import Path
import pandas as pd




# %% #* path locations
ROOT = Path(__file__).parents[2]
db_name = 'default_cc_clients'
db_location = ROOT / 'src' / 'database' / (db_name + '.db')
raw_data_table = 'raw_data'
xls_file = ROOT / 'data' / 'default of credit card clients.xls'

# %% #* DataFrame
df_file = pd.read_excel(xls_file, sheet_name='Data', skiprows=1)

df_columns = df_file.keys().str.replace(' ', '_').str.replace('0', '1')
# print(df_columns)

sql_cols = ' INTEGER, '.join(df_columns) + ' INTEGER'

db_values = []
for i, j in df_file.iterrows():
        db_values.append(str(tuple(j)))

str_values = ', '.join(db_values)


# %% #* query strings
query_1 = f"""
            CREATE TABLE IF NOT EXISTS {raw_data_table}
                ({sql_cols})
            """

query_2 = f"""
            INSERT INTO {raw_data_table}
                VALUES {str_values}
            """

query_check = f"""
            SELECT 1
            FROM {raw_data_table}
            LIMIT 1    
            """

# %% #* query executes
with sql.connect(db_location) as db:
    db.execute(query_1)

with sql.connect(db_location) as db:
    result = db.execute(query_check).fetchone() 
    
    if  result is None:
        db.execute(query_2)