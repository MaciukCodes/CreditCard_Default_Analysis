# %% #* Imports and file names

import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
import sqlite3 as sql

# %% #* File paths

ROOT = Path(__file__).parent.parent
db_location = ROOT / 'data' / 'default_cc_clients.db'
 
# %% #* SQL verifications with pandas and alchemy
engine = create_engine(
            f"sqlite:///{db_location}")

df_data = pd.read_sql('SELECT * FROM raw_data', engine)

print(df_data)

# %% #* sqlite3

query_1 = """
    CREATE TABLE clients(
        ID INTEGER,
            
    )
    """

with sql.connect(db_location) as db_step1:
    db_step1.execute(query_1)