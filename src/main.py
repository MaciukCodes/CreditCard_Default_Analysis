if __name__ == 'src.main':
    from src.download_unzip import download_unzip
    from src.create_tables import create_tables
    from src.insert_raw_data import insert_raw_data
    from src.insert_cardholder import insert_cardholder
    from src.insert_monthly import insert_monthly
else:
    from download_unzip import download_unzip
    from create_tables import create_tables
    from insert_raw_data import insert_raw_data
    from insert_cardholder import insert_cardholder
    from insert_monthly import insert_monthly
    

def run_all():
    download_unzip()
    create_tables()
    insert_raw_data()
    insert_cardholder()
    insert_monthly()