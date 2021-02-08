# Udacity Data Engineer Nanodegree - Capstone Project

### Project Summary
This project build up a data warehouse by integrating immigration data and demography data together to provide a wider range [single-source-of-truth](https://en.wikipedia.org/wiki/Single_source_of_truth) database.

The project follows the follow steps:

* Step 1: Scope the Project and Gather Data
* Step 2: Explore and Assess the Data
* Step 3: Define the Data Model
* Step 4: Run ETL to Model the Data
* Step 5: Complete Project Write Up

---

### Step 1: Scope the Project and Gather Data

#### Scope
This project will integrate I94 immigration data, world temperature data and US demographic data to setup a data warehouse with fact and dimension tables.

* Data Sets 
    1. [I94 Immigration Data](https://travel.trade.gov/research/reports/i94/historical/2016.html)
    2. [World Temperature Data](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data)
    3. [U.S. City Demographic Data](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/)

* Tools
    * AWS S3: data storage
    * AWS Redshift: data warehouse and data analysis
    * Python for data processing
        * Pandas - exploratory data analysis on small data set
        * PySpark - data processing on large data set

#### Describe and Gather Data 

| Data Set | Format | Description |
| ---      | ---    | ---         |
|[I94 Immigration Data](https://travel.trade.gov/research/reports/i94/historical/2016.html)| SAS | Data contains international visitor arrival statistics by world regions and select countries (including top 20), type of visa, mode of transportation, age groups, states visited (first intended address only), and the top ports of entry (for select countries).|
|[World Temperature Data](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data)| CSV | This dataset is from Kaggle and contains monthly average temperature data at different country in the world wide.|
|[U.S. City Demographic Data](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/)| CSV | This dataset contains information about the demographics of all US cities and census-designated places with a population greater or equal to 65,000.|


---

### Step 2: Explore and Assess the Data

#### Explore the Data 

1. Use pandas for exploratory data analysis to get an overview on these data sets
2. Split data sets to dimensional tables and change column names for better understanding
3. Utilize PySpark on one of the SAS data sets to test ETL data pipeline logic

#### Cleaning Steps

1. Transform arrdate, depdate from SAS time format to pandad.datetime
2. Parse description file to get auxiliary dimension table - country_code, city _code, state _code, mode, visa
3. Tranform city, state to upper case to match city _code and state _code table

Please refer to [Capstone_Project.ipynb](https://github.com/KentHsu/Udacity-DEND/blob/main/Capstone%20Project/Capstone_Project.ipynb).

(This step was completed in Udacity workspace as pre-steps for building up and testing the ETL data pipeline. File paths should be modified if notebook is run locally.)

---

### Step 3: Define the Data Model

#### Conceptual Data Model
Since the purpose of this data warehouse is for OLAP and BI app usage, we will model these data sets with star schema data modeling.

* Star Schema

	![alt text](https://github.com/KentHsu/Udacity-DEND/blob/main/Capstone%20Project/images/conceptual_data_model.png)

#### Data Pipeline Build Up Steps

1. Assume all data sets are stored in S3 buckets as below
	* `[Source_S3_Bucket]/immigration/18-83510-I94-Data-2016/*.sas7bdat`
	* `[Source_S3_Bucket]/I94_SAS_Labels_Descriptions.SAS`
	* `[Source_S3_Bucket]/temperature/GlobalLandTemperaturesByCity.csv`
	* `[Source_S3_Bucket]/demography/us-cities-demographics.csv`
2. Follow by Step 2 – Cleaning step to clean up data sets
3. Transform immigration data to 1 fact table and 2 dimension tables, fact table will be partitioned by state
4. Parsing label description file to get auxiliary tables
5. Transform temperature data to dimension table
6. Split demography data to 2 dimension tables
7. Store these tables back to target S3 bucket

---

### Step 4: Run Pipelines to Model the Data 

#### 4.1 Create the data model

Data processing and data model was created by Spark.

Please refer to [Capstone_Project.ipynb](https://github.com/KentHsu/Udacity-DEND/blob/main/Capstone%20Project/Capstone_Project.ipynb).

#### 4.2 Data Quality Checks

Data quality checks includes

1. No empty table after running ETL data pipeline
2. Data schema of every dimensional table matches data model

Please refer to [Data_Quality_Check.ipynb](https://github.com/KentHsu/Udacity-DEND/blob/main/Spark%20and%20Data%20Lake/Data_Quality_Check.ipynb).

#### 4.3 Data dictionary 

![alt text](https://github.com/KentHsu/Udacity-DEND/blob/main/Capstone%20Project/images/data_dictionary.png)

---

### Step 5: Complete Project Write Up
1. Clearly state the rationale for the choice of tools and technologies for the project.
    * Spark is capable for large dataset processing
    * Airflow do help build up data pipeline effeciently

2. Propose how often the data should be updated and why.
    * The dataset should be update monthly

3. Write a description of how you would approach the problem differently under the following scenarios:
 * The data was increased by 100x.
 * The data populates a dashboard that must be updated on a daily basis by 7am every day.
 * The database needed to be accessed by 100+ people.