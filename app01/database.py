import sqlite3

# conn = sqlite3.connect(':memory:') # save stuff to a db in memory

conn = sqlite3.connect('customer.db') # create the database

# create tables in your database 

# create a  cursor: it tells the db what you want to do 
cursor = conn.cursor()

# create a table 
# use a docstring to write SQL 
# sqlite3 is case sensitive so SQL keywords should be capitalizes

# cursor.execute("""
#     CREATE TABLE customers(
#         first_name TEXT,
#         last_name TEXT,
#         email TEXT
#         )
#         """)

# sql lite has 5 datatypes you can choose from 
# NULL nothing 
# INTEGER integers
# REAL real nos
# TEXT strings 
# BLOB images, mp3 file, etc 

# After creating your table
# Note that adding entries to the table is done 
# line by line 


# Next you have to commit the commands to the database 
# conn.commit()

# Insert data into the table 
# create a new cursor
# 
c = conn.cursor()


# c.execute("""
#         INSERT INTO customers
#         VALUES(
#             'Mary', 'King', 'maryking@yahoo.com') 
#         """)

# Use python lists to pass multiple variables 
many_customers = [
        ('Will', 'Ian', 'willian@gmail.com'),
        ('Wes', 'Brown', 'wesbrown@yahoo.com'),
        ('Dan', 'Poh', 'danpoh@aol.com'),
            ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Query the data base

c.execute("SELECT * FROM customers")

# print(c.fetchall())
# print(c.fetchone())
# print(c.fetchone()[2])
# print(c.fetchmany(3))
print('-'*30)

#format your data
# using fetch all 

items = c.fetchall()
# print(items)

print('Name' + "\t\t\tEMAIL")
print("*"*40)
for i in items:
    # print(i)
    # print('-'*30)
    #for the first names 
    # print(i[0])
    # print('-'*30)
    #concatenate
    print(i[0] + " " + i[1] + "\t\t " + i[2])
    print('-'*30)


# print("Command Executed Successfully...")
conn.commit()

# close your connection
conn.close()


