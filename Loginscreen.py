from tkinter import *
from tkinter.constants import CENTER
from CustomWidgets import *
from Sql_db import login_user_add
from SupportFunctions import *

supportfunction_Loginscreen = SupportFunctions()


def loginscreen_ui():
    """Function for Login screen"""

    #############################################
    # ! Main root window properties

    loginscreen = Tk()

    width = loginscreen.winfo_screenwidth()

    height = loginscreen.winfo_screenheight()

    loginscreen.geometry(supportfunction_Loginscreen.centerwindow(
        loginscreen, width, height))

    loginscreen.overrideredirect(TRUE)

    loginscreen.resizable(0, 0)
    ##################################################
    # ! Main canvas

    loginscreen_canvas = Canvas(
        loginscreen, width=width, height=height, highlightthickness=0)

    loginscreen_canvas.pack()

    Bg_image = supportfunction_Loginscreen.image_resizer(
        width, height, 'Pictures\LoginScreen 1.png')

    loginscreen_canvas.create_image(
        width / 2, height / 2, anchor=CENTER, image=Bg_image)

    # ! Sub canvas

    loginscreen_subcanvas = Canvas(
        loginscreen_canvas, width=400, height=height, bg='#121512', highlightthickness=0)
    loginscreen_canvas.create_window(
        width / 2, height / 2, anchor=CENTER, window=loginscreen_subcanvas)

    loginscreen_shutdown_img = PhotoImage(file='Pictures/Icons/power-off-button-30.png')
    loginscreen_shutdown_button = Button(loginscreen_subcanvas, image=loginscreen_shutdown_img, bg='#121512',
                                         activebackground='#121512', relief=FLAT,
                                         command=lambda: supportfunction_Loginscreen.closewindow(loginscreen))
    loginscreen_subcanvas.create_window(200, 600, anchor=CENTER, window=loginscreen_shutdown_button)

    # ! Login screen Entry Widget UI

    logo = PhotoImage(file='Pictures/Icons/icons8-data-encryption-50.png')
    loginscreen_subcanvas.create_image(200, 90, anchor=CENTER, image=logo)

    logo_name = PhotoImage(file='Pictures/Icons/Loginscreen PIC.png')
    loginscreen_subcanvas.create_image(
        200, 160, anchor=CENTER, image=logo_name)

    # ? Username

    loginscreen_subcanvas.create_text(
        70, 270, anchor=CENTER, text="Username", font=('corbel', 12), fill='#1DB954')

    logo_username = PhotoImage(file='Pictures/Icons/username-30.png')
    loginscreen_subcanvas.create_image(
        50, 300, anchor=CENTER, image=logo_username)

    Username = Entry(loginscreen_subcanvas, bg='#121512',
                     relief=FLAT, fg='white', width=25, font=('corbel', 17,))
    loginscreen_subcanvas.create_window(
        220, 300, anchor=CENTER, window=Username)

    loginscreen_subcanvas.create_line(
        69, 319, 371, 319, width=2, fill='#1DB954')

    # ? Password

    loginscreen_subcanvas.create_text(
        70, 370, anchor=CENTER, text="Password", font=('corbel', 12), fill='#1DB954')

    logo_password = PhotoImage(file='Pictures/Icons/password-30.png')
    loginscreen_subcanvas.create_image(
        50, 400, anchor=CENTER, image=logo_password)

    Password = Entry(loginscreen_subcanvas, bg='#121512',
                     relief=FLAT, fg='white', width=25, font=('Corbel', 17))
    loginscreen_subcanvas.create_window(
        220, 400, anchor=CENTER, window=Password)

    loginscreen_subcanvas.create_line(
        69, 418, 371, 418, width=2, fill='#1DB954')

    # ? Buttons

    login_button_image = PhotoImage(file='Pictures/Icons/login-96.png')
    login_button_image1 = login_button_image.subsample(3, 3)
    login_button = Button(loginscreen_subcanvas, text="  Login", relief=FLAT, image=login_button_image1, bg='#121512',
                          compound=LEFT,
                          fg='#1DB954', activebackground='#121512', activeforeground='#1DB954', font=('Corbel', 20),
                          command=lambda: login_user_add(Username, Password, 'MainWindow.py', "Login",
                                                         'Are you sure to Login ?', loginscreen_canvas))

    loginscreen_subcanvas.create_window(
        200, 500, anchor=CENTER, window=login_button)

    loginscreen_subcanvas.create_text(
        200, 670, anchor=CENTER, text='Don\'t have an account ?', fill='white', font=('Corbel', 13))

    loginscreen_register_button = Button(loginscreen_subcanvas, text='Create account', relief=FLAT, bg='#121512',
                                         fg='#1DB954', activebackground='#121512', activeforeground='#1DB954',
                                         font=('Corbel', 11),
                                         command=lambda: supportfunction_Loginscreen.open_close_script(
                                             'Registration.py', 'Redirection', 'Do You want to register?',
                                             loginscreen_canvas))
    loginscreen_subcanvas.create_window(200, 700, anchor=CENTER, window=loginscreen_register_button)
    ################################################
    loginscreen.mainloop()


loginscreen_ui()
