import os
import pandas as pd
from jinja2 import Template
from datetime import datetime

# Function to create a new HTML file from the template
def create_html_from_template(template_file, file_name, context):
    with open(template_file, "r") as template:
        content = template.read()
    template = Template(content)
    rendered_html = template.render(**context)
    with open(file_name, "w") as new_file:
        new_file.write(rendered_html)
    print(f"HTML file {file_name} created successfully.")
    return file_name

# Function to process Excel data and create HTML certificates
def process_excel_data(template_file, excel_file, output_html_dir):
    # Read Excel data
    data = pd.read_excel(excel_file)
    
    # Ensure required columns exist
    required_columns = {'ID', 'USN', 'Name'}
    if not required_columns.issubset(data.columns):
        raise ValueError(f"Excel file must contain the following columns: {required_columns}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_html_dir, exist_ok=True)
    
    # Process each row in the Excel sheet
    for index, row in data.iterrows():
        student_id = row['ID']
        usn = row['USN']
        name = row['Name']
        current_date = datetime.today().strftime('%Y-%m-%d')  # Get current date
        
        context = {
            "id": student_id, 
            "usn": usn, 
            "name": name, 
            "current_date": current_date  # Add the current date to the context
        }
        
        # Generate HTML file
        html_file = os.path.join(output_html_dir, f"{usn}_{name}.html")
        create_html_from_template(template_file, html_file, context)

# Main program
if __name__ == "__main__":
    # File paths
    template_file = "template.html"  # Updated template for the certificate
    excel_file = "StudentData.xlsx"  # Excel file with student data
    output_html_dir = "output_htmls"  # Directory to store generated certificates
    
    # Menu-driven system
    print("Choose an option:")
    print("1. Create an HTML file from template")
    print("2. Process an Excel file and generate HTML certificates")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        file_name = input("Enter the name for the new HTML file (without extension): ") + ".html"
        student_id = input("Enter ID: ")
        usn = input("Enter USN: ")
        name = input("Enter Name: ")
        current_date = datetime.today().strftime('%Y-%m-%d')  # Current date for the certificate
        context = {"id": student_id, "usn": usn, "name": name, "current_date": current_date}
        create_html_from_template(template_file, file_name, context)
    elif choice == "2":
        process_excel_data(template_file, excel_file, output_html_dir)
    else:
        print("Invalid choice. Exiting.")
