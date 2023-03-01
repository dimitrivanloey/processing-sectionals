import pandas as pd
from pandas.io import excel
from datetime import datetime

# Read the excel file
xl = pd.read_excel('hun.xlsx')

# Get the title of the main sheet
sheet_title = xl.sheet_names[0]

# Initialize a list to store the tables data
tables = []

# Loop through all the tables in the excel sheet
for sheet in xl.sheet_names:
    df = xl.parse(sheet)
    
    # Get the table title
    title = df.iloc[0, 0]
    
    # Get the table date
    date_string = df.iloc[1, 0]
    date = datetime.strptime(date_string, '%Y-%m-%d').date()
    
    # Store the table data in a dictionary
    table = {'title': title, 'date': date, 'data': df}
    tables.append(table)

# Generate the HTML page
html = '<html><head><title>' + sheet_title + '</title></head><body>'

for table in tables:
    html += '<h2>' + table['title'] + '</h2>'
    html += '<p>Date: ' + str(table['date']) + '</p>'
    html += table['data'].to_html()

html += '</body></html>'

# Write the HTML to a file
with open('sample.html', 'w') as f:
    f.write(html)