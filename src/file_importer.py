import xlsxwriter
import pandas as pd
import mysql.connector

# Define a dictionary for country names and their respective table names
countries = {
    "Australia": "australia",
    "Brunei": "brunei",
    "Cambodia": "cambodia",
    "China": "china",
    "Indonesia": "indonesia",
    "Japan": "japan",
    "Lao": "lao",
    "Malaysia": "malaysia",
    "Myanmar": "myanmar",
    "New Zeland": "new_zeland",
    "Philipines": "philipines",
    "Singapore": "singapore",
    "Thailand": "thailand",
    "Vietnam": "vietnam"
}

# Connect to the database
mydb = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)

mycursor = mydb.cursor()

# Loop through each country and process data
for country, table_name in countries.items():
    # Read the respective country's sheet
    data = pd.read_excel(r"data/RCEP_economic_analysis.xlsx", sheet_name=country)
    
    # Generate a dynamic SQL INSERT query
    sql_formula = f"INSERT INTO {table_name} VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    
    # Execute the query for all rows in the DataFrame
    for row in data.itertuples(index=False):
        mycursor.execute(sql_formula, row)
    
    countries[country] = data

# Commit all changes to the database
mydb.commit()