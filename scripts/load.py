from sqlalchemy import create_engine


def load_data(df):

    engine = create_engine(
        'postgresql+psycopg2://airflow:airflow@postgres:5432/airflow'
    )

    df.to_sql(
        'sales_data',
        engine,
        if_exists='replace',
        index=False
    )

    print("Data loaded into PostgreSQL")