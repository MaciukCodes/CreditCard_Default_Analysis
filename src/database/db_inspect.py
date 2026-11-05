# %% #* imports

from pathlib import Path
import sqlite3 as sql
import pandas as pd
from sqlalchemy import create_engine

from db_query_utils import sql_base_query

# %% #* paths

ROOT = Path(__file__).parents[2]
# print(ROOT)

alchemy_loc = r'sqlite:///' +  str(ROOT / 'src' / 'database' / 'default_cc_clients.db') 
# db_location = ROOT / 'src' / 'database' / 'default_cc_clients.db'

engine = create_engine(alchemy_loc)

query_card = sql_base_query('cardholder','*')
query_monthly = sql_base_query('monthly_reports','*')

# %% #* cardholders query sql
df_card = pd.read_sql(query_card, engine)

print(df_card.head(20))

print(df_card[df_card['age'] == df_card['age'].max()])
print(df_card[df_card['credit_limit'] == df_card['credit_limit'].max()])


# %% #* monthly reports sql query

df_month = pd.read_sql(query_monthly, engine)

print(df_month.head())


# %% #* query using sqlite3

# with sql.connect(db_location) as db:
#     q_back = db.execute(df_card)

# print(q_back.fetchmany(20))


# %%
