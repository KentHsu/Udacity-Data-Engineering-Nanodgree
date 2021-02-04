import datetime

from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from udac_example_dag import default_args


with DAG('create_table_dag', 
         start_date=datetime.datetime.now(),
         default_args=default_args) as dag:
    
    PostgresOperator(
        task_id="create_table",
        dag=dag,
        postgres_conn_id="redshift",
        sql='create_tables.sql'
    )
    