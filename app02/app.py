import customers_db 

#view all records in the db
# customers_db.show_all()

#add a record to the db
#customers_db.add_one('Jane', 'Oby', 'janeoby@aol.com')

# delete a record from the db
# note pass the rowid as a string not integer 
# customers_db.del_one('7')

# add many records 

# stuff = [
#     ('Brenda', 'Smith', 'breandaS@aol.com'),
#     ('Josh', 'Banks', 'Jbanks@gmail.com')
# ]

# customers_db.add_many(stuff)

#look up email addresses 
customers_db.email_lookup('Jbanks@gmail.com')

# view the db 
# customers_db.show_all()