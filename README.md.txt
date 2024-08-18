					# Customer Service Data Analysis and Reporting

This project analyzes customer service interactions to identify trends, improve response times, and enhance customer satisfaction. It uses Python and SQLite for data storage, analysis, and visualization.

## Prerequisites

- Python 3.x
- SQLite
- Required Python libraries:
  - pandas
  - sqlalchemy
  - matplotlib
  - seaborn

You can install the necessary Python libraries using:
```bash
pip install pandas sqlalchemy matplotlib seaborn
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <https://github.com/Kiranj27/CustomerServiceProject.git>
   cd <CustomerServiceProject>
   ```

2. Create the SQLite database and tables:
   ```bash
   sqlite3 customer_service.db
   ```

   Run the following SQL commands in the SQLite shell:
   ```sql
   CREATE TABLE customers (
       customer_id INTEGER PRIMARY KEY,
       name TEXT,
       email TEXT,
       join_date DATE
   );

   CREATE TABLE agents (
       agent_id INTEGER PRIMARY KEY,
       name TEXT,
       department TEXT
   );

   CREATE TABLE customer_service_logs (
       log_id INTEGER PRIMARY KEY,
       customer_id INTEGER,
       agent_id INTEGER,
       issue_type TEXT,
       issue_resolved BOOLEAN,
       response_time INTEGER,
       log_date DATE,
       FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
       FOREIGN KEY(agent_id) REFERENCES agents(agent_id)
   );
   ```

## Populating the Database with Sample Data

Run the `populate_db.py` script to insert sample customer, agent, and service log data into the SQLite database:
```bash
python populate_db.py
```

## Analyzing the Data

The `analyze_data.py` script connects to the database, retrieves the data, and performs basic analysis such as calculating average response times and plotting response time distributions.

Run the analysis script:
```bash
python analyze_data.py
```

## Project Structure

The repository contains the following files:
- `customer_service.db`: SQLite database file.
- `populate_db.py`: Python script to insert sample data into the database.
- `analyze_data.py`: Python script to analyze and visualize the customer service data.
- `README.md`: Project documentation.
```
