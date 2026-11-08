# %% #* imports
import sqlite3 as sql
from pathlib import Path
import pandas as pd

if __name__ == "__main__": 
    from db_query_utils import sql_create_table, sql_base_query, case_creation
else:
    from src.db_query_utils import sql_create_table, sql_base_query, case_creation

# %% #* file locations

ROOT = Path(__file__).parents[1]

db_location = ROOT / 'data' / 'database' / 'default_cc_clients.db'
xls_file = ROOT / 'data' / 'default of credit card clients.xls'

# %% #* columns + misc

raw_df_file = pd.read_excel(xls_file, sheet_name='Data', skiprows=1)
raw_df_cols = raw_df_file.keys().str.replace(' ', '_').str.replace('0', '1')
raw_cols = dict(zip(raw_df_cols, ['INTEGER'] * len(raw_df_cols)))

card_cols = {
    'cardholder_id': 'INTEGER PRIMARY KEY',
    'sex': 'TEXT',
    'education': 'TEXT',
    'marital_status': 'TEXT',
    'age': 'INTEGER',
    'credit_limit': 'INTEGER'    
    }

monthly_cols = {
        'statement_id' : 'INTEGER PRIMARY KEY',
        'cardholder_id': 'INTEGER',                 # Foreign key defined in extras
        'month': 'TEXT',
        'pay' : 'INTEGER',
        'bill_amount': 'INTEGER',
        'pay_amount': 'INTEGER'
    }

# %% #* extras (constraints)


card_extras_sex = """
            CHECK (sex IN(
                'Male',
                'Female',
                'Other',
                'Prefer not to say'
                ))
            """

card_extras_education = """
                CHECK(education IN(
                    'Graduate School',
                    'University',
                    'High School',
                    'Other'
                    ))
                """

card_extras_marital = """
                CHECK(marital_status IN(
                    'Married',
                    'Single',
                    'Other'
                    ))
                """

card_extras_age ="""
            CHECK( age between 0 AND 150)
            """

card_extras = [
                    card_extras_sex,
                    card_extras_education,
                    card_extras_marital,
                    card_extras_age
                ]

monthly_extras = [ "FOREIGN KEY (cardholder_id) REFERENCES cardholder (cardholder_id)"]

# %% #* functions

def create_tables():
    create_raw_data_table()
    create_cardholder_table()
    create_monthly_reports_table()


def create_raw_data_table():
    with sql.connect(db_location) as db:
        db.execute( sql_create_table('raw_data', **raw_cols))


def create_cardholder_table():
    with sql.connect(db_location) as db:
            db.execute( sql_create_table('cardholder', *card_extras, **card_cols))

def create_monthly_reports_table():
    with sql.connect(db_location) as db:
        db.execute( sql_create_table('monthly_reports', *monthly_extras, **monthly_cols))
# %%