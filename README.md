# RCEP Economic Analysis Project

## Project Overview

This project focuses on analyzing the economic risks associated with each partner involved in the recent **Regional Comprehensive Economic Partnership (RCEP)** trade deal in the Asia-Pacific region. The analysis is conducted using country-specific economic data and involves importing, processing, and visualizing relevant metrics to derive meaningful insights.


## Features

- **Data Loading and Processing**: Automates the process of importing country-specific data from an Excel file and populating a MySQL database for further analysis.
- **Database Management**: Includes functionality to dynamically insert data into pre-defined tables for each RCEP partner country.
- **Data Visualization**: Provides tools to visualize trends in key economic indicators, such as account balances, over time for all partner countries.


## Project Structure

├── database_loader.py      # Handles data import and database operations
├── plot_creator.py         # Manages data visualization
├── main.py                 # Entry point for the project
├── data/                   # Folder containing input data
└── README.md               # Project documentation


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/rcep-analysis.git
   cd rcep-analysis

2.	Install the required Python packages:
   pip install -r requirements.txt

3.	Ensure you have a MySQL database set up and update the db_details in main.py with your credentials.

4.	Place the Excel file RCEP_economic_analysis.xlsx in the data/ directory.


## Usage

1.	Run the main.py file:
2.	The script will:
	•	Load data from the Excel file into the database.
	•	Generate visualizations of economic trends.
3.	To create additional visualizations, update the column_name in main.py to the desired economic metric.


## Example Output

•	Visualizations showcasing trends like Account Balance vs. Years for all RCEP partners.
•	Warnings if certain metrics are not found in the data for specific countries.


## Contribution

Contributions to enhance this project are welcome! Feel free to open issues or submit pull requests.


## License

This project is licensed under the MIT License.