import pandas as pd


def extract_data():

    df = pd.read_csv(
        '/opt/airflow/data/raw/superstore.csv',
        encoding='latin1'
    )

    print("Data extracted successfully")

    return df