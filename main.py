from database_loader import get_database_connection, load_data_to_database
from plot_creator import plot_creator

def main():
    # Define database connection details
    db_details = {
        "host": "",
        "user": "",
        "passwd": "",
        "database": ""
    }
    
    # Define country-to-table mapping
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
    db_connection = get_database_connection(**db_details)

    # Load data from the Excel file to the database
    data_file = r"data/RCEP_economic_analysis.xlsx"
    data_dict = load_data_to_database(data_file, countries, db_connection)

    # Plot data (example usage)
    plot_creator(data_dict, 'Account_Balance')

if __name__ == "__main__":
    main()