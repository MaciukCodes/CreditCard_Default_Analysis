# %% #* sql_table_create
def sql_create_table( 
        table_name : str,
        *extras,
        **columns
        ):
    """A "quick" way to create tables 
    *** Note must be done within a context handler containing the database to connect to****
    
    :param table name: name of the table to create
    :param extras: after the table and columns are created add any constraints here manually afterwords
    :param columns: key-value pair of column name and data type 
    
    
    :ivar col: transfer the list of tuple to a list of string for each column
    :ivar cols: joins the list of strings together 
    
    :returns: the query in string format to create a table inside a sql db

    """

    if len(extras) > 0:
        extra = ',' + ',\n'.join(extras)
    else:
        extra = ''

    col = []

    for i in columns.items():
        col.append((f'{i[0]} {i[1]}'))

    cols = ', '.join(col)
        


    query = f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
            {cols}
            {extra}
            )
        """
    return query


# %% #* sql_base_query

def sql_base_query( from_table : str , *select, where : str | None = None):

    """ 
    Base sql query with SELECT FROM and an optional WHERE

    :param from_table: the table to query
    :param select: the information you wish to get back from the query
    :param where: optional but takes a string for the WHERE statement minus the where portion

    :ivar q_select: a string of all the values given in the select statement separated by a comma and space.
    
    :returns: a basic query to use in a SQL database
    """
    
    q_select = ', '.join(select)

    if where is None:
        q_where = ''
    else:
        q_where =f'WHERE {where}'


    query = f"""  
            SELECT {q_select}    
            FROM {from_table}
            {q_where}
            """
    return query


# %% #* case_creation

def case_creation(else_str : str | None = None, **kwargs):
    """
    case_creation is used to make a case statement for SQL

    :param else_str: if an entry fails all the case statements what should it be
    :param kwargs: the checks and returns of the case statement in a certain format

        format needed is:

            key(column) : key(expected value to find with appropriate comparison operator): value(the return)

    :ivar checks: a list containing each WHEN clause for the case statement
    :ivar x_checks: a string combining all the WHEN statements together in one string separated by a new line.
                
    :returns: case statement as a string to insert as needed into a sql query           
    """
    checks = []
    
    for o_key, o_value in kwargs.items():
        for i_key, i_value  in o_value.items():
            c = f"WHEN {o_key} {i_key} THEN '{i_value}' "
            checks.append(c)

    x_checks = ' '.join(checks)

    if else_str is None:
        e_other = ""
    else:
        e_other = f"ELSE '{else_str}'"

    query = f"""CASE {x_checks}
                {e_other}
                END"""

    return query


# %% #* sql_insert
def sql_insert(
    table_name : str,
    query : str,
    *columns,
    ):
    
    """
    Inserts values into a table via query of another table.
    
    :param table_name: name of the table to insert into.
    :param query: the query to use when grabbing the records of another table.
    :param columns: columns to be inserted into.

    :ivar cols: the columns parameter joined together in a string.

    :returns: a query to insert into the table provided.
    """

    if columns is None:
        cols = ''
    else:
        cols = ', '.join(columns)


    insert_query = f"""
        INSERT INTO {table_name} ({cols})
            {query}
        """
    return insert_query