
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import ttk
import tkinter as tk
import sqlite3
import datetime
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from datetime import datetime, timedelta



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\GYM-PROGRAM\GymTrack\assets3\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window =tk.Tk()
window.title("Gym App")
window.geometry("1100x700")
window.configure(bg = "#FFFFFF")

def add_gymMember():
    full_name = name_entry.get()

    try:
        num_of_months = int(num_of_months_entry.get())
        contact = int(contact_entry.get())

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
    
    print(full_name)
    print(contact)
    print(num_of_months)
     # Get the current date and time
    current_datetime = datetime.now()

    # Format the current datetime to remove microseconds
    date_registered = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    # Convert the date_registered string to a datetime object
    date_registered_obj = datetime.strptime(date_registered, '%Y-%m-%d %H:%M:%S')

    # Calculate the expiration date by adding the number of months (assuming 30 days per month)
    expiration_date_ex = date_registered_obj + timedelta(days=30 * num_of_months)

    # Format the expiration date
    expiration_date = expiration_date_ex.strftime("%Y-%m-%d %H:%M:%S")
    
    # Convert expiration_date to a datetime object
    expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S")


    # Compare expiration_date with today's date
    is_expired = expiration_date_obj < current_datetime

    if (is_expired):
        is_expired = "TRUE"
        print("True it is expired")
    else: 
        print("False it is not expired")
        is_expired = "FALSE"

    print(f"Date registered: {date_registered}")
    print(f"Expiry date: {expiration_date}")

    if full_name and contact and num_of_months:
        cursor.execute("INSERT INTO gymMembers (full_name, contact, date_registered , num_of_months, expiration_date, is_expired ) VALUES (?, ?, ?, ?, ?,?)", (full_name, contact, date_registered ,num_of_months, expiration_date,is_expired))
        conn.commit()
        load_gymMember()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")


def load_gymMember():
    for record in gymMember_tree.get_children():
        gymMember_tree.delete(record)

    cursor.execute("SELECT * FROM gymMembers")
    gymMember = cursor.fetchall()

    for row in gymMember:
        gymMember_tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


def clear_entries():
    name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    num_of_months_entry.delete(0, tk.END)
    
def gymLog():
    window.destroy()  

    subprocess.run(['python', 'gymLogs.py'])


def logout():
    window.destroy()  

    subprocess.run(['python', 'login.py'])
    


def update_gymMember():
    selected_gymMember = gymMember_tree.selection()
    if selected_gymMember:
        member_id = int(gymMember_tree.item(selected_gymMember, "values")[0])
        full_name = name_entry.get()
        try:
            num_of_months = int(num_of_months_entry.get())
            contact = int(contact_entry.get())

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
        
         # Get the current date and time
        current_datetime = datetime.now()

        # Format the current datetime to remove microseconds
        date_registered = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        
        # Convert the date_registered string to a datetime object
        date_registered_obj = datetime.strptime(date_registered, '%Y-%m-%d %H:%M:%S')

        # Calculate the expiration date by adding the number of months (assuming 30 days per month)
        expiration_date_ex = date_registered_obj + timedelta(days=30 * num_of_months)

        # Format the expiration date
        expiration_date = expiration_date_ex.strftime("%Y-%m-%d %H:%M:%S")
        
        # Convert expiration_date to a datetime object
        expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S")


        # Compare expiration_date with today's date
        is_expired = expiration_date_obj < current_datetime

        if (is_expired):
            is_expired = "TRUE"
            print("True it is expired")
        else: 
            print("False it is not expired")
            is_expired = "FALSE"

        
        print(f"Date registered: {date_registered}")
        print(f"Expiry date: {expiration_date}")
            
        if full_name and contact and num_of_months:
            cursor.execute("UPDATE gymMembers SET full_name=?, contact=?, date_registered=?, num_of_months=?, expiration_date=?, is_expired=? WHERE member_id=?",
               (full_name, contact, date_registered, num_of_months, expiration_date, is_expired, member_id))            
            conn.commit()
            load_gymMember()
            clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")
    else:
        messagebox.showwarning("Warning", "Please select a record to update.")
        
def delete_gymMember():
    selected_gymMember = gymMember_tree.selection()
    if selected_gymMember:
        member_id = int(gymMember_tree.item(selected_gymMember, "values")[0])
        cursor.execute("DELETE FROM gymMembers WHERE member_id=?", (member_id,))
        conn.commit()
        load_gymMember()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Please select a gymMember to delete.")

def search():
    search = entry_find_1.get()
    print("Searching..." + search)
    
    # Clear the treeview
    for item in gymMember_tree.get_children():
        gymMember_tree.delete(item)
    
    # Perform the search query
    cursor.execute("SELECT * FROM gymMembers WHERE full_name LIKE ?", ('%' + search + '%',))
    
    gymMember = cursor.fetchall()
    
    # Insert the results into the treeview
    if gymMember:
        for row in gymMember:
            gymMember_tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        
        # Clear the search entry field
        entry_find_1.delete(0, tk.END)
    else:
        print("No matching records found.")
    
    



conn = sqlite3.connect("gym.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS gymMembers (
    member_id INTEGER PRIMARY KEY,
    full_name TEXT,
    contact INTEGER,
    date_registered TEXT,
    num_of_months INTEGER,
    expiration_date TEXT,   
    is_expired TEXT
)''')



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1100,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    550.0,
    41.0,
    image=image_image_1
)


find_image_1 = PhotoImage(
    file=relative_to_assets("find_1.png"))
find_1 = Button(
    image=find_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=search,
    relief="flat"
)
find_1.place(
    x=946.0,
    y=217.0,
    width=70.0,
    height=35.0
)

canvas.create_text(
    678.0,
    192.0,
    anchor="nw",
    text="Search\n",
    fill="#474747",
    font=("Inter Bold", 14 * -1)
)

entry_find_image_1 = PhotoImage(
    file=relative_to_assets("entry_find_1.png"))
entry_bg_1 = canvas.create_image(
    805.0,
    234.5,
    image=entry_find_image_1
)
entry_find_1 = Entry(
    bd=0,
    bg="#E4E4E4",
    fg="#000716",
    highlightthickness=0
)
entry_find_1.place(
    x=678.0,
    y=217.0,
    width=254.0,
    height=33.0
)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    198.0,
    156.5,
    image=entry_image_1
)
name_entry = Entry(
    bd=0,
    bg="#E4E4E4",
    fg="#000716",
    highlightthickness=0
)
name_entry.place(
    x=71.0,
    y=139.0,
    width=254.0,
    height=33.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    490.0,
    156.5,
    image=entry_image_2
)
contact_entry = Entry(
    bd=0,
    bg="#E4E4E4",
    fg="#000716",
    highlightthickness=0
)

contact_entry.place(
    x=363.0,
    y=139.0,
    width=254.0,
    height=33.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    689.5,
    157.5,
    image=entry_image_3
)
num_of_months_entry = Entry(
    bd=0,
    bg="#E4E4E4",
    fg="#000716",
    highlightthickness=0
)
num_of_months_entry.place(
    x=651.0,
    y=140.0,
    width=77.0,
    height=33.0
)


gymMember_tree = ttk.Treeview(window, columns=('Member ID', 'Full Name', 'Contact', 'Date Registered', 'Num of Months', 'Expiration Date', 'Is Expired'), show='headings')

# Define the column headings

gymMember_tree.heading('Member ID', text='Member ID', anchor=tk.CENTER)
gymMember_tree.column('Member ID', anchor=tk.CENTER,width=100)

gymMember_tree.heading('Full Name', text='Full Name', anchor=tk.CENTER)
gymMember_tree.column('Full Name', anchor=tk.CENTER, )

gymMember_tree.heading('Contact', text='Contact', anchor=tk.CENTER)
gymMember_tree.column('Contact', anchor=tk.CENTER,width=100)

gymMember_tree.heading('Date Registered', text='Date Registered', anchor=tk.CENTER)
gymMember_tree.column('Date Registered', anchor=tk.CENTER,width=170)

gymMember_tree.heading('Num of Months', text='Num of Months', anchor=tk.CENTER)
gymMember_tree.column('Num of Months', anchor=tk.CENTER,width=100)

gymMember_tree.heading('Expiration Date', text='Expiration Date', anchor=tk.CENTER)
gymMember_tree.column('Expiration Date', anchor=tk.CENTER,width=170)

gymMember_tree.heading('Is Expired', text='Is Expired', anchor=tk.CENTER)
gymMember_tree.column('Is Expired', anchor=tk.CENTER,width=100)

# Grid the Treeview
gymMember_tree.grid()

canvas.create_window(547.0,440.0,window=gymMember_tree, height=350)

load_gymMember()




canvas.create_text(
    74.0,
    208.0,
    anchor="nw",
    text="Track Gym Members",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
add_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=add_gymMember,
    relief="flat"
)
add_button.place(
    x=762.0,
    y=139.0,
    width=70.0,
    height=35.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
update_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=update_gymMember,
    relief="flat"
)

update_button.place(
    x=854.0,
    y=139.0,
    width=70.0,
    height=35.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
delete_button = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=delete_gymMember,
    relief="flat"
)
delete_button.place(
    x=946.0,
    y=139.0,
    width=70.0,
    height=35.0
)

canvas.create_text(
    71.0,
    114.0,
    anchor="nw",
    text="FullName",
    fill="#474747",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    363.0,
    114.0,
    anchor="nw",
    text="ContactNumber",
    fill="#474747",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    651.0,
    114.0,
    anchor="nw",
    text="Months",
    fill="#474747",
    font=("Inter Bold", 14 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
logout = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=logout,
    relief="flat"
)
logout.place(
    x=966.0,
    y=20.0,
    width=131.0,
    height=46.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
gymLog = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=gymLog,
    relief="flat"
)
gymLog.place(
    x=21.0,
    y=16.0,
    width=138.0,
    height=44.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
gymMembers = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("gymMembers clicked"),
    relief="flat"
)
gymMembers.place(
    x=177.0,
    y=16.0,
    width=196.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
