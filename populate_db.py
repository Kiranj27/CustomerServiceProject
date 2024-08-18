import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('customer_service.db')
cursor = conn.cursor()

# Insert sample data into customers table
cursor.execute("INSERT INTO customers (name, email, join_date) VALUES ('Alice', 'alice@example.com', '2024-01-01')")
cursor.execute("INSERT INTO customers (name, email, join_date) VALUES ('Bob', 'bob@example.com', '2024-02-15')")

# Insert sample data into agents table
cursor.execute("INSERT INTO agents (name, department) VALUES ('Agent Smith', 'Technical Support')")
cursor.execute("INSERT INTO agents (name, department) VALUES ('Agent Jones', 'Customer Service')")

# Insert sample data into customer_service_logs table
cursor.execute("INSERT INTO customer_service_logs (customer_id, agent_id, issue_type, issue_resolved, response_time, log_date) VALUES (1, 1, 'Login Issue', 1, 5, '2024-08-01')")
cursor.execute("INSERT INTO customer_service_logs (customer_id, agent_id, issue_type, issue_resolved, response_time, log_date) VALUES (2, 2, 'Billing Issue', 0, 15, '2024-08-02')")

# Commit changes and close the connection
conn.commit()
conn.close()
