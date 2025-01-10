import matplotlib.pyplot as plt

def plot_creator(data_dict, column_name):
    """
    Plots the specified column for all countries in the data dictionary.

    Args:
        data_dict (dict): A dictionary where keys are country names and values are DataFrames.
        column_name (str): The column to plot against 'Year'.
    """
    for country_name, data in data_dict.items():
        if column_name in data.columns:
            plt.plot(data['Year'], data[column_name], label=country_name)
        else:
            print(f"Warning: '{column_name}' not found in {country_name}'s data.")
    
    plt.title(f'{column_name} vs Years')
    plt.xlabel('Year')
    plt.ylabel(column_name)
    plt.legend(loc='best')
    plt.grid(True)
    plt.tight_layout()
    plt.show()