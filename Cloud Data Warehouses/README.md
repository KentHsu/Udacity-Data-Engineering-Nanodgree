# Project: Build A Cloud Data Warehouse

This project builds an **ELT pipeline** that extracts data from **S3**, stages them in **Redshift**, and transforms data into a set of **dimensional tables** for Sparkify analytics team to continue finding insights in what songs their users are listening to.


## Project Structure

```
Cloud Data Warehouse
|____create_tables.py    # database/table creation script 
|____etl.py              # ELT builder
|____sql_queries.py      # SQL query collections
|____dwh.cfg             # AWS configuration file
|____test.ipynb          # testing
```


## ELT Pipeline
### etl.py
ELT pipeline builder

1. `load_staging_tables`
	* Load raw data from S3 buckets to Redshift staging tables
2. `insert_tables`
	* Transform staging table data to dimensional tables for data analysis

### create_tables.py
Creating Staging, Fact and Dimension table schema

1. `drop_tables`
2. `create_tables`

### sql_queries.py
SQL query statement collecitons for `create_tables.py` and `etl.py`

1. `*_table_drop`
2. `*_table_create`
3. `staging_*_copy`
3. `*_table_insert`


## Database Schema
### Staging tables
```
staging_events
    artist VARCHAR,
    auth VARCHAR,
    firstName VARCHAR,
    gender CHAR(1),
    itemInSession INT,
    lastName VARCHAR,
    length FLOAT,
    level VARCHAR,
    location TEXT,
    method VARCHAR,
    page VARCHAR,
    registration VARCHAR,
    sessionId INT,
    song VARCHAR,
    status INT,
    ts BIGINT,
    userAgent TEXT,
    userId INT

staging_songs
    artist_id VARCHAR,
    artist_latitude FLOAT,
    artist_location TEXT,
    artist_longitude FLOAT,
    artist_name VARCHAR,
    duration FLOAT,
    num_songs INT,
    song_id VARCHAR,
    title VARCHAR,
    year INT
```

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
