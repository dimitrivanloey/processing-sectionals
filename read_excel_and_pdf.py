import pandas as pd
from weasyprint import HTML

# Read the Excel file into a Pandas dataframe
df = pd.read_excel('excel_file.xlsx')

# Iterate through each sheet in the Excel file
for sheet_name in df.sheet_names:
    # Select the current sheet
    sheet = df[sheet_name]
    
    # Convert the sheet to an HTML table
    html_table = sheet.to_html()
    
    # Add CSS to the table
    html_table = '<style>table {border-collapse: collapse;} th, td {border: 1px solid black;}</style>' + html_table
    
    # Create a PDF of the table
    HTML(string=html_table).write_pdf(f'{sheet_name}.pdf')
