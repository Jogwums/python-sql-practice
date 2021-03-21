import sqlite3

# conn = sqlite3.connect(':memory:') # save stuff to a db in memory

conn = sqlite3.connect('customer2.db') # create the database

cursor = conn.cursor()


# cursor.execute("""
#     CREATE TABLE customers(
#         first_name TEXT,
#         last_name TEXT,
#         email TEXT
#         )
#         """)


cursor.execute("""
        SELECT rowid, * from customers ORDER BY last_name 
        """)
# sqlite 3 creates a unique rowid much like a unique ID 

# Use python lists to pass multiple variables 
many_customers = [
        ('Will', 'Ian', 'willian@gmail.com'),
        ('Wes', 'Brown', 'wesbrown@yahoo.com'),
        ('Dan', 'Poh', 'danpoh@aol.com'),
            ]

# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

items = cursor.fetchall()
for i in items:
    print(i)

# print("Command Executed Successfully...")
conn.commit()

# close your connection
conn.close()


