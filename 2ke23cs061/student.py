import pandas as pd

# Specify the Excel file path
excel_file = "StudentData.xlsx"  # Replace with your file path

# Load the Excel file into a DataFrame
try:
    data = pd.read_excel(excel_file)
    
    # Check if required columns exist
    required_columns = {'ID', 'USN', 'Name'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"Excel file must contain the following columns: {required_columns}")

    # Display the entire content of the Excel file
    print("Excel Sheet Contents:")
    print(data)

    # Access specific data
    print("\nIterating through rows:")
    for index, row in data.iterrows():
        print(f"Row {index + 1}: ID={row['ID']}, USN={row['USN']}, Name={row['Name']}")
        
except FileNotFoundError:
    print("Error: The specified Excel file was not found.")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
