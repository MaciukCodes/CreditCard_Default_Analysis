# %% #* imports

from pathlib import Path
import sqlite3 as sql
import pandas as pd
from sqlalchemy import create_engine

from database.db_query_utils import sql_base_query

# %% #* paths

ROOT = Path(__file__).parents[2]
# print(ROOT)

alchemy_loc = r'sqlite:///' +  str(ROOT / 'src' / 'database' / 'default_cc_clients.db') 
# db_location = ROOT / 'src' / 'database' / 'default_cc_clients.db'

query = sql_base_query('cardholder','*')


# %% #* query with pandas and sqlalchemy

engine = create_engine(alchemy_loc)

df = pd.read_sql(query, engine)

print(df.head(20))


# %% #* query using sqlite3

# with sql.connect(db_location) as db:
#     q_back = db.execute(query)

# print(q_back.fetchmany(20))


# %%
