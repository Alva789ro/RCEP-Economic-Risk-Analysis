import xlsxwriter
import pandas as pd
import mysql.connector

def get_database_connection(host, user, passwd, database):
    """
    Establish a connection to the database.

    Args:
        host (str): Database host.
        user (str): Database user.
        passwd (str): Database password.
        database (str): Database name.

    Returns:
        mysql.connector.connection.MySQLConnection: A connection object to the database.
    """
    return mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        database=database
    )

def load_data_to_database(file_path, countries, db_connection):
    """
    Load data from an Excel file to the database.

    Args:
        file_path (str): Path to the Excel file.
        countries (dict): A dictionary mapping country names to table names.
        db_connection (mysql.connector.connection.MySQLConnection): Database connection object.
    
    Returns:
        dict: A dictionary where keys are country names and values are their respective DataFrames.
    """
    data_dict = {}
    cursor = db_connection.cursor()

    for country, table_name in countries.items():
        # Read data from the Excel file
        data = pd.read_excel(file_path, sheet_name=country)
        # Generate the SQL insert query
        sql_formula = f"INSERT INTO {table_name} VALUES({', '.join(['%s'] * len(data.columns))})"
        
        # Insert data into the database
        for row in data.itertuples(index=False):
            cursor.execute(sql_formula, row)
        
        # Store the DataFrame in the dictionary
        data_dict[country] = data
    
    # Commit the changes
    db_connection.commit()
    return data_dict