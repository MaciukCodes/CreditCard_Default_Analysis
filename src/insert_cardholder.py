# %% #* Imports

from pathlib import Path
import sqlite3 as sql

if __name__ == "src.insert_cardholder":
    from src.db_query_utils import sql_base_query, case_creation, sql_insert
else:
    from db_query_utils import sql_base_query, case_creation, sql_insert
    

# %% #* File paths

ROOT = Path(__file__).parents[1]

db_location = ROOT / 'data' / 'database' / 'default_cc_clients.db'


# %% #* function start

def insert_cardholder():

    # %% #* Case strings and dictionaries



    sex_else = "Other"

    sex_dict = {
            'SEX': {
                    '= 1': "Male",
                    '= 2': "Female"
                    }
                }

    educate_else = "Other"

    educate_dict = {
                    'EDUCATION':{
                        '= 1': 'Graduate School',
                        '= 2': 'University',
                        '= 3': 'High School'
                        }
                    }

    marital_else = "Other"

    marital_dict = {
                    'MARRIAGE':{
                        '= 1': 'Married',
                        '= 2': 'Single'
                        }
                    }


    # %% #* Case creation

    sex_column_case = case_creation( else_str=sex_else, **sex_dict)

    educate_column_case = case_creation(else_str=educate_else, **educate_dict)

    marital_column_case = case_creation(else_str=marital_else, **marital_dict)


    # %% #* select statement

    source_columns = [
                    'ID',
                    sex_column_case,
                    educate_column_case,
                    marital_column_case,
                    'AGE',
                    'LIMIT_BAL'
    ]

    data = sql_base_query('raw_data', *source_columns)


    # %% #* insert statement

    dest_cols = [
            'cardholder_id',
            'sex',
            'education',
            'marital_status',
            'age',
            'credit_limit'
        ]

    insert_query = sql_insert('cardholder', data, *dest_cols)

    #? my understanding of sqlite and python is that: its better to create a new then alter an existing one in this version
    check_query = sql_base_query('cardholder', '1') + 'LIMIT 1'


    # %% #* function executable

    with sql.connect(db_location) as db:

        result = db.execute(check_query).fetchone()
        if result is None:
            db.execute(insert_query)
        else:
            print('Table already contains data please use a empty table.')