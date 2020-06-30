# covid19_scraping_data
Scraping all data of reported Covid19 cases from a website from March 23 to June 19, 2020 autonomously.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Description](#Description)

## General info
Scraping data of reported Covid19 cases from a https://www.gov.mb.ca/health/newsreleases/index.html autonomously from March 23 to June 19, 2020; and insert all the data into a Postgres database.
	
## Technologies
This project is created with:
* Python version: 3.6.9
* Beautiful Soup Library version: 4
* psycopg version: 2 2.8.5
* Postgres SQL version: 10.12
* word2number version 1.1

## Description
* Python:
    > 1. scraping_data(soup): First, find all the td tag in the main content table, then find all the links that contain Covid-19 Bulletin # format to filter out all the reported cases news.The main contents of each news are simliar to the " Public health officials advise " format, there were some cases that need to use Regex to find the number of cases. 
    > 2. config(filename='database.ini', section='postgresql'): reading the database.ini that contains host, database_name, user and password.
    > 3. connect(): a standard connect method to connect to PostgresSQL
    > 4. insert_new_case(case_data, num_case): a standard method that runs a query to insert a new case to a database.
    > 5. main(): loop through the dates array and insert new cases that reported and updated from the website.
* PostgresSQL:
    > CREATE TABLE covid19_scraping_data_table(
	id serial,
	date VARCHAR (50) NOT NULL,
	cases VARCHAR (50) NOT NULL
);

* Run locally once in order to insert data into a Postgres database.
