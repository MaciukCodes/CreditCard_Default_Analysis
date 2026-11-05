# %% #* Imports
import sqlite3 as sql
from pathlib import Path
from db_query_utils import sql_table_create, sql_base_query, sql_insert


# %% #* Paths

ROOT = Path(__file__).parents[2]

# print(ROOT)

db_loc = ROOT / 'src' / 'database' / 'default_cc_clients.db'

# print(db_loc)


# %% #* create table

columns = {
        'statement_id' : 'INTEGER PRIMARY KEY',
        'cardholder_id': 'INTEGER',
        'month': 'TEXT',
        'pay' : 'INTEGER',
        'bill_amount': 'INTEGER',
        'pay_amount': 'INTEGER'
    }
extras_monthly_reports = [
                        """FOREIGN KEY (cardholder_id) REFERENCES cardholder (cardholder_id)""",
                    ]


create_table_sql = sql_table_create('monthly_reports',*extras_monthly_reports,  **columns)

# print(create_table_sql)
with sql.connect(db_loc) as db:
    db.execute(create_table_sql)


# %% #* Months select statments

monthly = []

for i in range(1, 7):
    select_monthly = [
                    'PAY_{}'.format(i),
                    'BILL_AMOUNT_{}'.format(i),
                    'PAY_AMOUNT_{}'.format(i)]
    'month_' + i = sql_base_query('raw_data' )
    

print (month_1)

# %%
