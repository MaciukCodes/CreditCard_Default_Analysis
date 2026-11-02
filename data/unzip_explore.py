#  %% #* Initial imports
import pandas as pd
import zipfile as zip
from pathlib import Path

ROOT = Path(__file__).parent.parent

#  %% #* Base URL (and file name....)
#? had trouble extracting from the site and manually downloaded the zip
# url = 'https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip'
file_base = ROOT / 'data' / 'raw_downloads' / 'default+of+credit+card+clients.zip'
#// file made later but here for ease of access
file_loc = ROOT / 'data' / 'default of credit card clients.xls'


# %% #* Unzip context managers (and sub zip file names)
#? had to be done in sequence so am commenting out the previous in the sequence to avoid dups.
if not file_loc.exists():
    with zip.ZipFile(file_base) as zip_data:
        zip_data.extractall(path=ROOT / 'data')



# %% #* Excel dataframe extraction

# excel_file = pd.read_excel(file_loc, sheet_name='Data', skiprows=1)

# %% #* DataFrame exploration

# print(excel_file.keys())
# print(excel_file.head())
# print(excel_file.tail())
# print(excel_file.info())
# print(excel_file.sample())
# %%
