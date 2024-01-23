## Code here
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
pass_google = os.environ.get('PASS_GOOGLE_AUTHENTICATION')

files_path = './bases'
files = os.listdir(files_path)

consolidated_table = pd.DataFrame()

for file_name in files:
    sales_table = pd.read_csv(os.path.join(files_path, file_name))
    sales_table['Data de Venda'] = pd.to_datetime('01/01/1900') + pd.to_timedelta(sales_table['Data de Venda'], unit='d')

    consolidated_table = pd.concat([consolidated_table, sales_table])

consolidated_table = consolidated_table.sort_values(by='Data de Venda')
consolidated_table = consolidated_table.reset_index(drop=True)
consolidated_table.to_excel('Vendas.xlsx', index=False)
