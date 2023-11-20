print("""                             __|__                                             __|__               """)
print("""                            |o   o|                                           |o   o|          """)
print("""                            |  ∆  |     ::: SCHOOL MANAGMENT SYSTEM :::       |  ∆  |                                                   """)
print("""                            |  ∆  |                                           |  ∆  |                """)
print("""                            |_____|                                           |_____|                """)


#CREATING DATABASESprint
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="12345")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists myfile")
mycursor.execute("use myfile")

#creating requires tables
mycursor.execute("create table if not exists student(name varchar(50) not null,class varchar(25),roll_no varchar (25),gender char(1))")
mycursor.execute("create table if not exists staff(name varchar(50) not null,gendr char(1),subject varchar(25) not null,salary varchar(25))")
mydb.commit()

#now for using infinit looping we use while(true) statement
while(True):

    print("""
                            select which process you want to gothrough.......    """)
    print("1-Enter Data for new student")
    print("2-Enter data for new staff")
    print("3-Search student Data")
    print("4-search staff data")
    print("5-Remove student record")
    print("6-Remove staff recod")
    print("7-EXIT")
    ch = int(input("ENTER YOUR CHOICE=== "))
    if ch == 1:
        print("All information prompted are mandatory to be filled")
        name=input("Enter name === ")
        classs=str(input("Enter class === "))
        roll_no=str(input("Enter Roll number=== "))
        gender=str(input("Enter Gender(M/F)=== "))
        mycursor.execute("insert into student values('"+name+"','"+classs+"','"+roll_no+"','"+gender+"')")
        mydb.commit()

        print("student recore has been saved successfully")

    elif ch == 2:
        
         name = str(input("Enter staff member name=== "))
         gender = str(input("Enter Gender(M/f)=== "))
         dep = str(input("Enter department or subject=== "))
         sal = int(input("Enter salary=== "))
         mycursor.execute("insert into staff values('"+name+"','"+gender+"','"+dep+"','"+str(sal)+"')")
         mydb.commit()
    
   
    elif ch == 3:
        roll_no = str(input("Enter student roll_no"))
        mycursor.execute("SELECT * FROM student WHERE roll_no = " + roll_no)
        for i in mycursor:
            name,classs,roll_no,gender=i
       
       
            print(f'name: {name}')
            print(f'Class: {classs}')
            print(f'Roll number: {roll_no}')
            print(f'Gender: {gender}')

#makeing this for getting the detail of staff query

    elif ch == 4:
         name = str(input("Enter staff name: "))
         mycursor.execute("SELECT * FROM staff WHERE name = %s", (name,))

         for i in mycursor:
             name,gender,dep,sal=i
       
       
             print(f'name: {name}')
             print(f'gender: {gender}')
             print(f'dep: {dep}')
             print(f'sal: {sal}')
             
    
    elif ch == 5:
        roll_no = str(input("Enter student roll_no: "))
        mycursor.execute("DELETE FROM student WHERE roll_no = %s", (roll_no,))
        mydb.commit()
    
        print("Student record has been successfully deleted.")
    elif ch == 6:
        name = str(input("Enter staff name: "))
        mycursor.execute("DELETE FROM staff WHERE name = %s", (name,))
        mydb.commit()
    
        print("Staff record has been successfully deleted.")
    else:
        break
