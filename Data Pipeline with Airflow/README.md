# Project: Data Pipeline with Apache Airflow
This project continues working on the music streaming company’s data infrastructure by creating and automating/scheduling a set of **data pipelines**. We configure and schedule data pipelines with **Apache Airflow** to extract raw datasets from **S3** to **Redshift**, transform and load data from staging tables to dimensional tables. We also monitor production pipelines by run data quality checks to track data linage.

## Project Structure

```
Data Pipeline with Apache Airflow
|
|____dags
| |____ create_tables_dag.py   # DAG for creating tables on Redshift
| |____ create_tables.sql      # SQL CREATE queries
| |____ udac_example_dag.py    # Main DAG for this ETL data pipeline
|
|____plugins
| |____ __init__.py
| |
| |____operators
| | |____ __init__.py          # Define operators and helpers
| | |____ stage_redshift.py    # COPY data from S3 to Redshift
| | |____ load_fact.py         # Execute INSERT query into fact table
| | |____ load_dimension.py    # Execute INSERT queries into dimension tables
| | |____ data_quality.py      # Data quality check after pipeline execution
| |
| |____helpers
| | |____ __init__.py
| | |____ sql_queries.py       # SQL queries for building up dimensional tables
```

## How to Run
1. Create a Redshift cluster on your AWS account
2. Turn on Airflow by running Airflow/start.sh
3. Create AWS and Redshift connections on Airflow Web UI
4. Run create_table _dag DAG to create tables on Redshift
5. Run udac_example _dag DAG to trigger ETL data pipeline


## Airflow Data Pipeline

### Airflow DAG overview
![Alt Text](https://github.com/KentHsu/Udacity-DEND/blob/main/Data%20Pipeline%20with%20Airflow/images/udac-example-dag.png)

### Operators

1. `Begin_execution` & `End_execution`

    Dummy operators at data pipeline end points

2. `Stage_events` & `Stage_songs`

    Extract/Transform data from S3 to Redshift to create staging tables

3. `Load_songplays_fact_table` & `Load_*_dim_table`
    
    Load data from staging tables to dimensional tables

4. `data_quality.py` 
    
    Check no empty table after data loading. More tests can be added into this operator to ensure data quality


## Database Schema
![Alt Text](https://github.com/KentHsu/Udacity-DEND/blob/main/Data%20Pipeline%20with%20Airflow/images/Udacity_Data_Schema.png)


