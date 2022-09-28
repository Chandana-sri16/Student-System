# Joseph's module
# created database
# chandana helped in between

import mysql.connector

# connect the mysql to python
database = mysql.connector.connect(host='127.0.0.1', user='root', password='chandana16@r', auth_plugin='mysql_native_password', database='student')
# cursor for executing the python code
cur = database.cursor()

# to save data entered:
def save_data():
    a = input("Enter student name: ")
    b = input("Enter Roll no: ")
    c = input("Enter College name: ")
    d = input("Email ID: ")
    e = input("Course name: ")

    # syntax to insert details in table
    s = 'INSERT INTO std_details values(%s,%s,%s,%s,%s)'
    t = (a, b, c, d, e)

    # to execute command
    cur.execute(s, t)
    # to save
    database.commit()

# to get details from table
def fetch_info():
    n = input("Enter std name to fetch details: ")
    # syntax to get particular student details
    r = f"SELECT * FROM std_details where std_name = '{n}'"

    cur.execute(r)
    details = cur.fetchall()   # returns all the info from table
    # for getting details separately
    for i in details:
        for s in i:
            print(s, end="  ")
        print()

# to edit the entered details
def edit():
    # shows all the students details
    t = 'SELECT * FROM std_details'
    cur.execute(t)
    details = cur.fetchall()
    for i in details:
        for s in i:
            print(s, end="  ")
        print()

    # modifies the details
    n = input("\nEnter std name to edit details: ")
    name = input("Change name - ")
    roll = input("Change roll - ")
    clg = input("Change college -")
    email = input("New email - ")
    course = input("Change course - ")

    u = f"UPDATE std_details set email_id ='{email}',std_name ='{name}',std_roll ='{roll}',clg_name ='{clg}',course ='{course}' where std_name = '{n}' "

    cur.execute(u)
    database.commit()




