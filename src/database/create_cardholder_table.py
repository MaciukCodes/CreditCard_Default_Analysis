# %% #* Imports and file names

# import pandas as pd
# from sqlalchemy import create_engine
from pathlib import Path
import sqlite3 as sql



# %% #* custom functions imports

from database.db_query_utils import sql_table_create, sql_base_query, case_creation, sql_insert

# %% #* File paths

ROOT = Path(__file__).parents[2]
# print(ROOT)

db_location = ROOT / 'src' / 'database' / 'default_cc_clients.db'
# print(db_location)

# %% #* sql query create table 

extras_sex = """
            CHECK (sex IN(
                'Male',
                'Female',
                'Other',
                'Prefer not to say'
                ))
            """

extras_education = """
                CHECK(education IN(
                    'Graduate School',
                    'University',
                    'High School',
                    'Other'
                    ))
                """

extras_marital = """
                CHECK(marital_status IN(
                    'Married',
                    'Single',
                    'Other'
                    ))
                """

extras_age ="""
            CHECK( age between 0 AND 150)
            """

extras = ',\n'.join([
                    extras_sex,
                    extras_education,
                    extras_marital,
                    extras_age
                ])

columns = {
    'cardholder_id': 'INTEGER PRIMARY KEY',
    'sex': 'TEXT',
    'education': 'TEXT',
    'marital_status': 'TEXT',
    'age': 'INTEGER'    
    }

create_table = sql_table_create('cardholder', extras, **columns )

# print(create_table)

# %% #* SQL insert query case creation

#  %% #// sex column case statement
sex_else = "Other"

sex_dict = {
        'SEX': {
                '= 1': "Male",
                '= 2': "Female"
                }
            }

sex_column_case = case_creation( else_str=sex_else, **sex_dict)

# print(case_state)

# %% #// education column case statement

educate_else = "Other"

educate_dict = {
                'EDUCATION':{
                    '= 1': 'Graduate School',
                    '= 2': 'University',
                    '= 3': 'High School'
                    }
                }

educate_column_case = case_creation(else_str=educate_else, **educate_dict)

# print(educate_column_case)

#  %% #// marital_status column case statement

marital_else = "Other"

marital_dict = {
                'MARRIAGE':{
                    '= 1': 'Married',
                    '= 2': 'Single'
                    }
                }

marital_column_case = case_creation(else_str=marital_else, **marital_dict)

# print(marital_column_case)


# %% #* SQL insert query

source_table = 'raw_data'

source_columns = [
                'ID',
                sex_column_case,
                educate_column_case,
                marital_column_case,
                'AGE'
]

sql_insert_query = sql_base_query( source_table, *source_columns)

# print(sql_insert_query)

# %% #* SQL insert into table

dest_table = 'cardholder'
dest_columns = [
            'cardholder_id',
            'sex',
            'education',
            'marital_status',
            'age'
            ]

sql_values_insert = sql_insert(dest_table, sql_insert_query, *dest_columns )

# print(sql_values_insert)

# %% #* db connect and execute

with sql.connect(db_location) as db_step1:
    db_step1.execute(create_table)

with sql.connect(db_location) as db_step2:
    db_step2.execute(sql_values_insert)

# %%
