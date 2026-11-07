# %% #* imports

from pathlib import Path
import sqlite3 as sql
import pandas as pd
from sqlalchemy import create_engine
import os

print(os.getcwd())

print(__file__)
ROOT = Path(__file__).parents[1]
print(ROOT)

from database.db_query_utils import sql_base_query

# %% #* paths



alchemy_loc = r'sqlite:///' +  str(ROOT / 'src' / 'database' / 'default_cc_clients.db') 
db_location = ROOT / 'src' / 'database' / 'default_cc_clients.db'

engine = create_engine(alchemy_loc)

query_card = sql_base_query('cardholder','*')
query_monthly = sql_base_query('monthly_reports','*')
query_raw = sql_base_query('raw_data', '*')

# %% #* raw_data queries

df = pd.read_sql(query_raw, engine)

print(df.keys())
print(df.head())


# %% #* cardholders query sql
df_card = pd.read_sql(query_card, engine)

print(df_card.head(20))

print(df_card[df_card['age'] == df_card['age'].max()])
print(df_card[df_card['credit_limit'] == df_card['credit_limit'].max()])


# %% #* monthly reports sql query

where = 'cardholder_id = 19'

# where = (
#     """
#     cardholder_id IN(
#     SELECT cardholder_id
#     FROM monthly_reports
#     GROUP BY cardholder_id
#     HAVING MIN(pay) == -2
#     )
#     """
#     )


query = sql_base_query(
            'monthly_reports',
            '*',
            where=where
            )

# query = sql_base_query('monthly_reports', 'DISTINCT(pay)')

# query = sql_base_query('monthly_reports', 'cardholder_id', where = where)


# print(query)

df_month = pd.read_sql(query, engine)


print(df_month)




# %% #* query using sqlite3

# query = "DROP TABLE monthly_reports"
# query = "DROP TABLE cardholder"
# query = "DROP TABLE raw_data"


with sql.connect(db_location) as db:
    q_back = db.execute(query)




# %%
