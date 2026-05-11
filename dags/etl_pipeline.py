from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

import sys
sys.path.append('/opt/airflow')

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.validate import validate_data
from scripts.load import load_data


def etl():

    df = extract_data()

    df = transform_data(df)

    validate_data(df)

    load_data(df)


with DAG(

    dag_id='etl_pipeline',

    start_date=datetime(2024, 1, 1),

    schedule='@daily',

    catchup=False,

    tags=['etl']

) as dag:

    run_etl = PythonOperator(

        task_id='run_etl_pipeline',

        python_callable=etl

    )