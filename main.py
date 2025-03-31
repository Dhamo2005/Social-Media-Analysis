import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("dataset.db")
cursor = conn.cursor()

# Fetch data
cursor.execute("SELECT * FROM social_media_usage")
rows = cursor.fetchall()

# Print data
for row in rows:
    print(row)

# Close connection
conn.close()
