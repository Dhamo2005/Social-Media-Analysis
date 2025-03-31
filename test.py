import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("dataset.db")
cursor = conn.cursor()

# Get the list of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:")
for table in tables:
    print(f"- {table[0]}")

# Display the structure of each table
for table in tables:
    print(f"\nStructure of table: {table[0]}")
    cursor.execute(f"PRAGMA table_info({table[0]});")
    columns = cursor.fetchall()
    for column in columns:
        print(f"  {column[1]} ({column[2]})")

# Close the connection
conn.close()