import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="satyam@25")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists myfile")
mycursor.execute("use myfile")

# creating required tables
mycursor.execute("create table if not exists student(name varchar(50) not null,class varchar(25),roll_no varchar (25),gender char(1))")
mycursor.execute("create table if not exists staff(sname varchar(50) not null,gendr char(1),subject varchar(25) not null,salary varchar(25))")
mydb.commit()

# Entry widgets for record management
entry_name = None
entry_class = None
entry_roll = None
entry_gender = None
entry_subject = None
entry_salary = None
entry_Gender = None
entry_sname = None

# Function to handle clearing entry fields
def clear_fields():
    # Clear the entry fields
    entry_name.delete(0, tk.END)
    entry_class.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_subject.delete(0, tk.END)
    entry_salary.delete(0, tk.END)
    entry_Gender.delete(0, tk.END)
    entry_sname.delete(0, tk.END)

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
    mycursor.execute("insert into staff values (%s, %s, %s, %s)", (name, gender, subject, salary))
    mydb.commit()
    messagebox.showinfo("Success", "Staff record has been saved successfully")

# Function to handle the "Search staff data" button
def search_staff_data():
    name = entry_sname.get()
    mycursor.execute("SELECT * FROM staff WHERE sname = %s", (name,))
    result = mycursor.fetchone()
    if result:
        staffname, gender, subject, salary = result
        messagebox.showinfo("Staff Details", f"Name: {name}\nGender: {gender}\nSubject: {subject}\nSalary: {salary}")
    else:
        messagebox.showinfo("Error", "Staff record not found")

# Function to handle the "Remove staff record" button
def remove_staff_record():
    name = entry_sname.get()
    mycursor.execute("DELETE FROM staff WHERE sname = %s", (name,))
    mydb.commit()
    messagebox.showinfo("Success", "Staff record has been successfully deleted.")

# Function to handle the login
def login():
    valid_username = "admin"
    valid_password = "password"

    entered_username = username_var.get()
    entered_password = password_var.get()

    if entered_username == valid_username and entered_password == valid_password:
        messagebox.showinfo("Login Successful", "Welcome, {}".format(entered_username))
        show_record_management_page()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


def logout():
    # Destroy both the login frame and the record management frame
    login_frame.destroy()
    try:
        record_management_frame.destroy()
    except NameError:
        pass  # Ignore if record_management_frame is not defined
    root.destroy()  # Close the entire application

# Function to show the record management page
def show_record_management_page():
    # Destroy the login frame
    login_frame.destroy()
    root.geometry("550x340")

    # Create a new frame for the record management page
    global record_management_frame
    record_management_frame = ttk.Frame(root)
    record_management_frame.grid(row=0, column=0, sticky="nsew")

    tk.Button(record_management_frame, text="Logout", command=logout).grid(row=10, column=2, columnspan=2, pady=10)

    global entry_name, entry_class, entry_roll, entry_gender, entry_subject, entry_salary, entry_Gender, entry_sname

    # Entry widgets for record management
    entry_name = tk.Entry(record_management_frame)
    entry_name.grid(row=0, column=1, padx=10, pady=5)
    entry_class = tk.Entry(record_management_frame)
    entry_class.grid(row=1, column=1, padx=10, pady=5)
    entry_roll = tk.Entry(record_management_frame)
    entry_roll.grid(row=2, column=1, padx=10, pady=5)
    entry_gender = tk.Entry(record_management_frame)
    entry_gender.grid(row=1, column=4, padx=10, pady=5)
    entry_subject = tk.Entry(record_management_frame)
    entry_subject.grid(row=2, column=4, padx=10, pady=5)
    entry_salary = tk.Entry(record_management_frame)
    entry_salary.grid(row=3, column=4, padx=10, pady=5)
    entry_Gender = tk.Entry(record_management_frame)
    entry_Gender.grid(row=3, column=1, padx=10, pady=5)
    entry_sname = tk.Entry(record_management_frame)
    entry_sname.grid(row=0, column=4, padx=10, pady=5)

    # Labels for record management
    tk.Label(record_management_frame, text="Name:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(record_management_frame, text="Class:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(record_management_frame, text="Roll number:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(record_management_frame, text="Gender:").grid(row=1, column=3, padx=10, pady=5)
    tk.Label(record_management_frame, text="Subject:").grid(row=2, column=3, padx=10, pady=5)
    tk.Label(record_management_frame, text="Salary:").grid(row=3, column=3, padx=10, pady=5)
    tk.Label(record_management_frame, text=" Staff Name:").grid(row=0, column=3, padx=10, pady=5)
    tk.Label(record_management_frame, text="gender:").grid(row=3, column=0, padx=10, pady=5)

    # Buttons for record management
    tk.Button(record_management_frame, text="Enter Data for new student", command=enter_student_data).grid(row=6, column=1, columnspan=2, pady=10)
    tk.Button(record_management_frame, text="Search student Data", command=search_student_data).grid(row=7, column=1, columnspan=2, pady=10)
    tk.Button(record_management_frame, text="Remove student record", command=remove_student_record).grid(row=8, column=1, columnspan=2, pady=10)
    tk.Button(record_management_frame, text="Enter Data for new staff", command=enter_staff_data).grid(row=6, column=4, columnspan=2, pady=10)
    tk.Button(record_management_frame, text="Search staff Data", command=search_staff_data).grid(row=7, column=4, columnspan=2, pady=10)
    tk.Button(record_management_frame, text="Remove staff record", command=remove_staff_record).grid(row=8, column=4, columnspan=2, pady=10)
    tk.Button(record_management_frame, text="clear", command=clear_fields).grid(row=9, column=1, columnspan=2, pady=10)
# Create the main window
root = tk.Tk()
root.title("RECORD MANAGEMENT::::")

# Create a frame for the login page
login_frame = ttk.Frame(root)
login_frame.grid(row=0, column=0, sticky="nsew")

# Username and password variables
username_var = tk.StringVar()
password_var = tk.StringVar()

# Entry widgets for username and password
tk.Label(login_frame, text="Username:").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(login_frame, textvariable=username_var)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(login_frame, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(login_frame, show="*", textvariable=password_var)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login button
login_button = ttk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
