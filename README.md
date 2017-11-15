# Log-Analysis-Project
 
## Table of Contents
* About
* Requirements
* Run the Programme

## About
  The Log-Analysis-Project is about retriving news data from a news database and reporting answers to the following three questions:
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of reqests lead to errors?
  
## Requirements
  1. Python3 ( [Download here](https://www.python.org/downloads/))
  2. Virtual Box ( [Download here](https://www.virtualbox.org/wiki/Downloads))
  3. Vagrant ( [Download here](https://www.vagrantup.com/downloads.html))
  4. Terminal or Git bash ( [Download here](https://git-scm.com/downloads))
  5. PostgreSQL ( [Download here](https://www.postgresql.org/download/))
  
## Run the Programme
  1. Download the FSND-Virtual-Machine folder and newsdata.sql provided in the Project instructions.
  2. Launch Virtual box with vagrant up and vagrant ssh command in the terminal.
  3. Cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
  4. Create the newslog.py file.
  5. Use the command python newslog.py to report the result.
  
