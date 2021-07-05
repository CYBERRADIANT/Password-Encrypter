import subprocess
import sys
from tkinter import messagebox
import re

import mysql.connector as sql

connectdb = sql.connect(
    host='localhost',
    user='root',
    passwd='Vishwaa6789',
    database='userdata'
)

cursor = connectdb.cursor()


def register_user_add(name, password, reenter, gmail, pythonfile, title, message, window):
    """For adding the user in db and open the mainwindow"""

    name_get = name.get()
    password_get = password.get()
    gmail_get = gmail.get()
    reenter_get = reenter.get()
    cursor.execute('SELECT name FROM userinfo')
    results = cursor.fetchall()
    namesinlist = []
    regex = r'\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b'

    if len(name_get) and len(password_get) and len(gmail_get) and len(reenter_get) == 0:
        messagebox.showerror('Error', 'You cannot leave any blank spaces')
    elif password_get != reenter_get:
        messagebox.showerror('Error', "Passwords does not mactch")
    elif len(password_get) < 8:
        messagebox.showerror('Error', 'Enter a Strong Password')
    elif not re.match(regex, gmail_get):
        messagebox.showerror('Error', "Enter a Valid Email")
    else:
        for result in results:
            for appending in result:
                namesinlist.append(appending)

        if name_get in namesinlist:
            messagebox.showerror("Error", "Username already Taken")

        else:
            ask = messagebox.askyesno(title, message, parent=window)
            if ask == 1:
                insert_in_table = 'INSERT INTO userinfo (name , password, gmail) VALUES (%s, %s, %s)'
                data = (f'{name_get}', f'{password_get}', f'{gmail_get}')
                cursor.execute(insert_in_table, data)
                connectdb.commit()
                subprocess.run(['python', f'{pythonfile}'])
                sys.exit(0)
            else:
                pass


def login_user_add(name, password, pythonfile, title, message, window):
    """For check and login"""

    def open_close_script():
        """for opening the mainwindow"""
        ask = messagebox.askyesno(title, message, parent=window)
        if ask == 1:
            subprocess.run(['python', f'{pythonfile}'])
            sys.exit(0)

    name_get = name.get()
    password_get = password.get()
    namesinlist = []
    cursor.execute('SELECT name FROM userinfo')
    results = cursor.fetchall()

    for result in results:
        for appending in result:
            namesinlist.append(appending)

    if name_get in namesinlist:
        cursor.execute("select * from userinfo where name = '%s'" % name_get)
        rud = cursor.fetchall()
        listforchecking = []
        for step1 in rud:
            for step2 in step1:
                listforchecking.append(step2)
        if password_get == listforchecking[1]:
            open_close_script()
        else:
            messagebox.showerror('Error', 'Wrong Password')
    else:
        messagebox.showerror('Error', "Username not found, Create an account!")
