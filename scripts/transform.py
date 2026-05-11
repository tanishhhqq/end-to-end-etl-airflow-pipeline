import pandas as pd


def transform_data(df):

    # lowercase columns
    df.columns = [
        col.lower().replace(' ', '_')
        for col in df.columns
    ]

    # remove null values
    df = df.dropna()

    # convert sales column
    if 'sales' in df.columns:
        df['sales'] = df['sales'].astype(float)

    # save processed file
    df.to_csv(
        '/opt/airflow/data/processed/processed_superstore.csv',
        index=False
    )

    print("Transformation completed")

    return df