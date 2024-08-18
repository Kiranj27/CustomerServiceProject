import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('customer_service.db')

# Load data from the customer_service_logs table
df_logs = pd.read_sql_query("SELECT * FROM customer_service_logs", conn)

# Close the connection
conn.close()

# Display the data
print(df_logs)

# Analyze response times
avg_response_time = df_logs['response_time'].mean()
print(f"Average Response Time: {avg_response_time:.2f} minutes")

# Plot response times
plt.hist(df_logs['response_time'], bins=10)
plt.title('Distribution of Response Times')
plt.xlabel('Response Time (minutes)')
plt.ylabel('Frequency')
plt.show()
