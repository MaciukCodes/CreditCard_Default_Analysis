# %% #* imports

import sqlite3 as sql
from pathlib import Path
import pandas as pd

if __name__ == 'src.insert_monthly':
    from src.db_query_utils import sql_base_query, case_creation, sql_insert
else:
    from db_query_utils import sql_base_query, case_creation, sql_insert
    
# %% #* locations

ROOT = Path(__file__).parents[1]

db_location = ROOT / 'data' / 'database' / 'default_cc_clients.db'


# %% #* function start

def insert_monthly():

    #* months select query innards

    monthly = []

    months = [
            'September',
            'August',
            'July',
            'June',
            'May',
            'April'
        ]

    #? only the month needs to be the month everything else uses the enumerated number may be a way to combine this and next function
    #? but at this time they seem to be better done as 2 separate operations

    for num, month in enumerate(months, 1):

        month = month
        pay = f'PAY_{num}'
        bill = f'BILL_AMT{num}'
        pay_amount = f'PAY_AMT{num}'

        monthly.append({ 'pay': pay, 'bill': bill, 'pay_amount': pay_amount, 'month': month})

    df = pd.DataFrame(monthly)


    # %% #* months select statement combined

    q_list = []

    for num, row in df.iterrows():

        q_list.append(
                sql_base_query(
                    'raw_data',
                    'ID',
                    f"\"{row['month']}\"",
                    row['pay'],
                    row['bill'],
                    row['pay_amount']
                    )
                )

    wide_to_tall = f'{'UNION ALL\n'.join(q_list)}'


    # %% #* sql executable

    cols =[
        'cardholder_id',
        'month',
        'pay',
        'bill_amount',
        'pay_amount'
        ]

    monthly_insert = sql_insert('monthly_reports', wide_to_tall, *cols)

    check_query = sql_base_query('monthly_reports', '1') + 'LIMIT 1'


    # %% #* function executable

    with sql.connect(db_location) as db:

        results = db.execute(check_query).fetchone()

        if results is None:
            db.execute(monthly_insert)
        else:
            print('Table already contains data please use a empty table.')