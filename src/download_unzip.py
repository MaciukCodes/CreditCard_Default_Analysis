# %% #* imports
from zipfile import ZipFile
from pathlib import Path
import requests
from io import BytesIO

# %% #* file locations
ROOT = Path(__file__).parents[1]

url = 'https://archive.ics.uci.edu/static/public/350/default+of+credit+card+clients.zip'
xls = 'default of credit card clients.xls'
file_loc = ROOT / 'data' / xls

# %% #* function

def download_unzip():
    response = requests.get(url)
    response.raise_for_status()

    if not file_loc.exists():
        (ROOT / 'data').mkdir(exist_ok=True)

        with ZipFile(BytesIO(response.content)) as zip_data:
            zip_data.extractall(path=ROOT / 'data')