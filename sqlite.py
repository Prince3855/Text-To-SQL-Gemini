import sqlite3

# Connect to database
connection = sqlite3.connect('student.db')

# Create cursor object to insert records and create table
cursor = connection.cursor()

# Create table
create_table_query = """
    CREATE TABLE IF NOT EXISTS 
        student (id INTEGER PRIMARY KEY, name TEXT NOT NULL, class VARCHAR(25), section VARCHAR(25), marks INTEGER)
"""
cursor.execute(create_table_query)

# Insert records

students = [
    (1, 'John Doe', 'Python', 'A', 85),
    (2, 'Jane Smith', 'Data Science', 'B', 69),
    (3, 'Michael Johnson', 'Devops', 'A', 91),
    (4, 'Sarah Williams', 'Data Science', 'B', 34),
    (5, 'Emily Davis', 'Devops', 'A', 95),
    (6, 'Michael Lee', 'Python', 'B', 76)
]

insert_records_query = """
    INSERT INTO student (id, name, class, section, marks) VALUES (?,?,?,?,?)
"""

cursor.executemany(insert_records_query, students)

# Display insrted records

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()