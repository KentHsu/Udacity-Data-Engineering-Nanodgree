# Project: Spark and Data Lake
This project builds an **ETL pipeline** for a **data lake**. The data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in the app. We loaded data from S3, process the data into analytics tables using **Spark**, and load them back into S3.


## Project Structure

```
Spark and Data Lake
|____etl.py              # ETL builder
|____dl.cfg              # AWS configuration file
|____test.ipynb          # testing
```


## ELT Pipeline
### etl.py
ELT pipeline builder

1. `process_song_data`
	* Load raw data from S3 buckets to Spark stonealone server and process song dataset to insert record into _songs_ and _artists_ dimension table

2. `process_log_data`
	* Load raw data from S3 buckets to Spark stonealone server and Process event(log) dataset to insert record into _time_ and _users_ dimensio table and _songplays_ fact table


## Database Schema

### Fact table
```
songplays
    songplay_id INT IDENTITY(0,1),
    start_time TIMESTAMP,
    user_id INT,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INT,
    location TEXT,
    user_agent TEXT
```

### Dimension tables
```
users
    user_id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    gender CHAR(1),
    level VARCHAR

songs
    song_id VARCHAR,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration FLOAT

artists
    artist_id VARCHAR,
    name VARCHAR,
    location TEXT ,
    latitude FLOAT ,
    longitude FLOAT

time
    start_time TIMESTAMP,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday VARCHAR
```
