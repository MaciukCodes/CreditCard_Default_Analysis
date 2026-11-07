# %% #* Imports
import sqlite3 as sql
from pathlib import Path
from db_query_utils import sql_table_create, sql_base_query, sql_insert, case_creation
import pandas as pd


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

table_name = 'monthly_reports'

create_table_sql = sql_table_create(table_name, *extras_monthly_reports,  **columns)

# print(create_table_sql)
with sql.connect(db_loc) as db:
    db.execute(create_table_sql)


# %% #* Months select statements

monthly = []
months = [
        'September',
        'August',
        'July',
        'June',
        'May',
        'April'
    ]

# 
for i, j in enumerate(months, 1):

    month = j
    pay = f'PAY_{i}'
    bill = f'BILL_AMT{i}'
    pay_amount = f'PAY_AMT{i}'

    monthly.append({ 'pay':pay, 'bill':bill, 'pay_amount': pay_amount, 'month': month})
    
df = pd.DataFrame(monthly)

# print(df)

q_list = []


for num, row in df.iterrows():
    
    q_list.append(
        (sql_base_query(
            'raw_data',
            'ID',
            f"\'{row['month']}\'",
            row['pay'],
            row['bill'],
            row['pay_amount']
            )
            ))

# print(q_list)


month_union = f"""{' UNION ALL\n '.join(q_list)}"""

# print(month_union)


# %% #* insert and execute

cols = [
    'cardholder_id',
    'month',
    'pay',
    'bill_amount',
    'pay_amount'
    ]

r_monthly = sql_insert( table_name,month_union, *cols)

# print(r_monthly)

with sql.connect(db_loc) as db: 
    db.execute(r_monthly)




# %%
