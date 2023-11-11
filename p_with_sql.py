from tabulate import tabulate   #import tabulate for convert values in structure format

import mysql.connector #import mysql connector that is connecting with your localhost my sql server

ps = mysql.connector.connect(host = "localhost",user = "root",password = "2002",database = "python_with_sql")
#connecting code must be all value in string format


def insert(name,age,course): #creating function insert data's
    connect_sql = ps.cursor()
    data = "insert into users(S_NAME,AGE,COURSE) values(%s,%s,%s)"
    value = (name,age,course)
    connect_sql.execute(data,value)
    ps.commit()
    print("inserted Successfully")

def update(name,age,course,id): #creating function update data's
    connect_sql = ps.cursor()
    data = "update users set S_NAME = %s,AGE = %s,COURSE = %s where ID =%s"
    value = (name,age,course,id)
    connect_sql.execute(data,value)
    ps.commit()
    print("Data Updated Successfully")

def select(): #creating function for select showing data's
    connect_sql = ps.cursor()
    data = "select ID,S_NAME,AGE,COURSE from users"
    connect_sql.execute(data)
    total = connect_sql.fetchall()
    print(tabulate(total,headers=["ID","S_NAME","AGE","COURSE"]))

def delete(id): #creating function for particular row deleting
    connect_sql = ps.cursor()
    data = "delete from users where id = %s"
    value = (id,)
    connect_sql.execute(data,value)
    ps.commit()
    print("Row Deleted Successfully")

while True:
    print("""
        1.Insert Data
        2.Update Data
        3.Select Data
        4.Delete Data
        5.Quit
    """)

    choose = int(input("Enter Your Choice : "))

#usinh if condition that collecting and update values from users
    if choose == 1:
        name = input("Enter New Name : ")
        age = int(input("Enter New Age : "))
        course = input("Enter New Course : ")
        insert(name,age,course)

    elif choose == 2:
        id = int(input("Choose ID : "))
        name = input("Enter Update Name : ")
        age = int(input("Enter Update Age : "))
        course = input("Enter Update Course : ")
        update(name,age,course,id)

    elif choose == 3:
        select()

    elif choose == 4:
        id = int(input("Enter ID No : "))
        delete(id)

    elif choose == 5:
        quit()

    else:
        print("Invalid Enter Correct Value")


