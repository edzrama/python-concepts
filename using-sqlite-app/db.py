import sqlite3

# Return all from db
def show_all():
    connect = sqlite3.connect('customer.db')
    # NOTE:  create cursor
    cursor = connect.cursor()
    cursor.execute("SELECT rowid, * FROM customers")
    items = cursor.fetchall()

    for item in items:
        print(item)

    # NOTE: close connection
    connect.close()


# NOTE: Insert new record to table
def add_one(first, last, email):
    connect = sqlite3.connect('customer.db')
    # NOTE:  create cursor
    cursor = connect.cursor()
    cursor.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    # NOTE: Commit command
    connect.commit()
    # NOTE: Close connection
    connect.close()


# inserting multiple records
def add_multiple_records(customer_list):
    connect = sqlite3.connect('customer.db')
    # NOTE:  create cursor
    cursor = connect.cursor()
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", customer_list)
    print('customer(s) successfully added')
    connect.commit()
    # NOTE: Close connection
    connect.close()


#  NOTE: Delete a record by ID
def delete_one(rowid):
    connect = sqlite3.connect('customer.db')
    # NOTE:  create cursor
    cursor = connect.cursor()
    cursor.execute("DELETE from customers WHERE rowid =(?)", [id])
    connect.commit()
    # NOTE: Close connection
    connect.close()


def email_lookup(email):
    connect = sqlite3.connect('customer.db')
    # NOTE:  create cursor
    cursor = connect.cursor()
    cursor.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,))
    items = cursor.fetchall()

    for item in items:
        print(item)
    # NOTE: Close connection
    connect.close()

