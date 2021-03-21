import sqlite3

# Query customers db and return all records 

def show_all():
    """show all records in the database"""
    # connect to the db 
    conn = sqlite3.connect(database='customer.db')
    cursor = conn.cursor()
    # create a function to show all content in the db
    
    #Query the DB 
    cursor.execute("SELECT rowid, * FROM customers ")
    items = cursor.fetchall()

    for _ in items:
        print(_)

    #commit connection 
    conn.commit()
    # close connection
    conn.close()

def add_one(first, last, email):
    """add a new record to the database"""
    conn = sqlite3.connect(database='customer.db')
    cursor = conn.cursor()
    # write the query
    #create palceholders for function params
    cursor.execute("INSERT INTO customers VALUES(?,?,?)", (first, last, email))

    #commit changes 
    conn.commit()

    #close connection
    conn.close()

def add_many(list):
    """add many entries to the db"""
    conn = sqlite3.connect(database='customer.db')
    cursor = conn.cursor()
    # write the query
    #create palceholders for function params
    cursor.executemany("INSERT INTO customers VALUES (?,?,?)", list)

    #commit changes 
    conn.commit()
    #close connection
    conn.close()


def del_one(id):
    """delete a record matching the id given from the database"""
    conn = sqlite3.connect(database='customer.db')
    cursor = conn.cursor()
    # write the query
    #create palceholders for function params
    cursor.execute("DELETE FROM customers WHERE rowid = (?)", id)

    #commit changes 
    conn.commit()
    #close connection
    conn.close()


def email_lookup(email):
    """search for email database"""
    conn = sqlite3.connect(database='customer.db')
    cursor = conn.cursor()
    # write the query
    #create palceholders for function params
    cursor.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,))
    items = cursor.fetchall()
    for i in items:
        print(i)
    #commit changes 
    conn.commit()
    #close connection
    conn.close()
