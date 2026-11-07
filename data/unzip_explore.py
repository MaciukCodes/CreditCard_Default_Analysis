#  %% #* Initial imports
import pandas as pd
import zipfile as zip
from pathlib import Path

ROOT = Path(__file__).parents[1]
print(ROOT)

#  %% #* Base URL (and file name....)
#? had trouble extracting from the site and manually downloaded the zip
# url = 'https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip'
file_base = ROOT / 'src' / 'database' / 'raw_downloads' / 'default+of+credit+card+clients.zip'
#// file made later but here for ease of access
xls = 'default of credit card clients.xls'
file_loc = ROOT / 'data' / xls

# %% #* Unzip context managers (and sub zip file names)
#? had to be done in sequence so am commenting out the previous in the sequence to avoid dups.
if not file_loc.exists():
    with zip.ZipFile(file_base) as zip_data:
        zip_data.extractall(path=ROOT / 'data')

