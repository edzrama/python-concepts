import db
# add record to db
# db.add_one(first='Edward', last='Rama', email='edward.rama@gmail.com')

# Add multiple records
customers = [('Jim', 'Doe', 'jimdoe@gmail.com'),
             ('Jamie', 'Doe', 'jamiedoe@gmail.com')]
# db.add_multiple_records(customer_list=customers)

# delete a record
# db.delete_one(rowid=6)

# display all records
# db.show_all()

db.email_lookup(email='edz.rama@gmail.com')