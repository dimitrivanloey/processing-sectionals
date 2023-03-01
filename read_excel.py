import pandas as pd

# specify the Excel file and sheet name
file = 'wet.xlsx'
sheet = 'Sheet1'

# read the Excel file into a dataframe
df = pd.read_excel(file, sheet_name=sheet)

# extract the tables from the dataframe
tables = pd.read_html(df.to_html())

# print the dataframes for each table
for i, table in enumerate(tables):
    print(f'Table {i + 1}:')
    print(table)
