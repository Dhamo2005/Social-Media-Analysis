import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the SQLite database
conn = sqlite3.connect("dataset.db")
query = "SELECT * FROM profile"  # Query the correct table
df = pd.read_sql_query(query, conn)
conn.close()

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Set a consistent style for plots
sns.set(style="whitegrid")

# 1. Followers Count Trend (Line Chart)
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Date', y='Followers Count', marker='o', label='Followers Count', color='blue')
plt.title('Followers Count Trend (January - March)')
plt.xlabel('Date')
plt.ylabel('Followers Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('followers_count_trend.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()

