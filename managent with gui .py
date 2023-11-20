import tkinter as tk
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists myfile")
mycursor.execute("use myfile")

#creating requires tables
mycursor.execute("create table if not exists student(name varchar(50) not null,class varchar(25),roll_no varchar (25),gender char(1))")
mycursor.execute("create table if not exists staff(sname varchar(50) not null,gendr char(1),subject varchar(25) not null,salary varchar(25))")
mydb.commit()




# Function to handle the "Enter Data for new student" button
def enter_student_data():
    name = entry_name.get()
    classs = entry_class.get()
    roll_no = entry_roll.get()
    gender = entry_gender.get()
    mycursor.execute("insert into student values (%s, %s, %s, %s)", (name, classs, roll_no, gender))
    mydb.commit()
    messagebox.showinfo("Success", "Student record has been saved successfully")

# Function to handle the "Search student Data" button
def search_student_data():
    roll_no = entry_roll.get()
    mycursor.execute("SELECT * FROM student WHERE roll_no = %s", (roll_no,))
    result = mycursor.fetchone()
    if result:
        name, classs, roll_no, gender = result
        messagebox.showinfo("Student Details", f"Name: {name}\nClass: {classs}\nRoll number: {roll_no}\nGender: {gender}")
    else:
        messagebox.showinfo("Error", "Student record not found")

# Function to handle the "Remove student record" button
# Function to handle the "Remove student record" button
def remove_student_record():
    roll_no = entry_roll.get()
    mycursor.execute("DELETE FROM student WHERE roll_no = %s", (roll_no,))
    mydb.commit()
    messagebox.showinfo("Success", "Student record has been successfully deleted.")

# Function to handle the "Enter data for new staff" button
def enter_staff_data():
    name = entry_sname.get()
    gender = entry_gender.get()
    subject = entry_subject.get()
    salary = entry_salary.get()
    mycursor.execute("insert into staff values (%s, %s, %s, %s)", (sname, gender, subject, salary))
    mydb.commit()
    messagebox.showinfo("Success", "Staff record has been saved successfully")

# Function to handle the "Search staff data" button
def search_staff_data():
    name = entry_sname.get()
    mycursor.execute("SELECT * FROM staff WHERE sname = %s", (sname,))
    result = mycursor.fetchone()
    if result:
        staffname, gender, subject, salary = result
        messagebox.showinfo("Staff Details", f"Name: {sname}\nGender: {gender}\nSubject: {subject}\nSalary: {salary}")
    else:
        messagebox.showinfo("Error", "Staff record not found")

# Function to handle the "Remove staff record" button
def remove_staff_record():
    name = entry_sname.get()
    mycursor.execute("DELETE FROM staff WHERE sname = %s", (sname,))
    mydb.commit()
    messagebox.showinfo("Success", "Staff record has been successfully deleted.")




# GUI setup
def clear_fields():
    # Clear the entry fi
    entry_name.delete(0, tk.END)
    entry_class.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_Gender.delete(0, tk.END)
    entry_subject.delete(0, tk.END)
    entry_salary.delete(0, tk.END)
    entry_sname.delete(0, tk.END)
    entry_gender.delete(0, tk.END)


root = tk.Tk()
root.title("Record Management")
root.geometry("520x310")

# Entry widgets
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)
entry_class = tk.Entry(root)
entry_class.grid(row=1, column=1, padx=10, pady=5)
entry_roll = tk.Entry(root)
entry_roll.grid(row=2, column=1, padx=10, pady=5)
entry_gender = tk.Entry(root)
entry_gender.grid(row=1, column=4, padx=10, pady=5)
entry_subject = tk.Entry(root)
entry_subject.grid(row=2, column=4, padx=10, pady=5)
entry_salary = tk.Entry(root)
entry_salary.grid(row=3, column=4, padx=10, pady=5)
entry_Gender = tk.Entry(root)
entry_Gender.grid(row=3, column=1, padx=10, pady=5)
entry_sname = tk.Entry(root)
entry_sname.grid(row=0, column=4, padx=10, pady=5)

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Class:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Roll number:").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Gender:").grid(row=1, column=3, padx=10, pady=5)
tk.Label(root, text="Subject:").grid(row=2, column=3, padx=10, pady=5)
tk.Label(root, text="Salary:").grid(row=3, column=3, padx=10, pady=5)
tk.Label(root, text=" Staff Name:").grid(row=0, column=3, padx=10, pady=5)
tk.Label(root, text="gender:").grid(row=3, column=0, padx=10, pady=5)

# Buttons
tk.Button(root, text="Enter Data for new student", command=enter_student_data).grid(row=6, column=1, columnspan=2, pady=10)
tk.Button(root, text="Search student Data", command=search_student_data).grid(row=7, column=1, columnspan=2, pady=10)
tk.Button(root, text="Remove student record", command=remove_student_record).grid(row=8, column=1, columnspan=2, pady=10)
tk.Button(root, text="Enter Data for new staff", command=enter_staff_data).grid(row=6, column=4, columnspan=2, pady=10)
tk.Button(root, text="Search staff Data", command=search_staff_data).grid(row=7, column=4, columnspan=2, pady=10)
tk.Button(root, text="Remove staff record", command=remove_staff_record).grid(row=8, column=4, columnspan=2, pady=10)
tk.Button(root, text="clear", command=clear_fields).grid(row=9, column=2, columnspan=2, pady=10)




root.mainloop()
