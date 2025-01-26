# import sqlite3
# conn = sqlite3.connect('database/college.sqlite3')
# cursor = conn.cursor()
# def create_table():
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS students(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             email TEXT,
#             age INTEGER,
#             address TEXT
#         )
#     """)
#     conn.commit()
#     print('Table created successfully')

# create_table()


# def insert_data(name,email,age,address):
#     cursor.execute("""INSERT INTO students(name,email,age,address) VALUES(?,?,?,?)""",(name,email,age,address))
#     conn.commit()
#     print('Data inserted successfully')


# name = input('Enter your name: ')
# email = input('Enter your email: ')
# age = int(input('Enter your age: '))
# address = input('Enter your address: ')
# insert_data(name,email,age,address)

# teacher table
# users
# products
import sqlite3
conn = sqlite3.connect('database/college.sqlite3')
cursor = conn.cursor()
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            sallary INTEGER,
            address TEXT
        )
    """)
    conn.comit()
    print('Table created successfully')
    create_table()
    def insert_data(name,phone,sallary,address):
        cursor.execute('''INSERT INTO teacher(name, phone sallary,addrass) VALUES(?,?,?,?)''',(name,phone,sallary,address))
        conn.commit()
        print('data inserted successfully')

        name = input('Enter your name:')
        phone = ('Enter your phone:')
        sallary = ('Enter your sallary:')
        address = ('Enter your address:')
        insert_data(name,phone,sallary,address)

