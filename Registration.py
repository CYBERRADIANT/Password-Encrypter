from tkinter import *
from Sql_db import register_user_add
from CustomWidgets import *
from SupportFunctions import *

supportfunction_Registration = SupportFunctions()


def registration_ui():
    """Function for Login screen"""

    #############################################
    # ! Main root window properties

    registrationscreen = Tk()

    width = registrationscreen.winfo_screenwidth()

    height = registrationscreen.winfo_screenheight()

    registrationscreen.geometry(supportfunction_Registration.centerwindow(
        registrationscreen, width, height))

    registrationscreen.overrideredirect(TRUE)

    registrationscreen.resizable(0, 0)
    ##################################################
    # ! Main canvas

    registration_canvas = Canvas(
        registrationscreen, width=width, height=height, highlightthickness=0)

    registration_canvas.pack()

    Bg_image = supportfunction_Registration.image_resizer(
        width, height, r'Pictures\LoginScreen 1.png')

    registration_canvas.create_image(
        width / 2, height / 2, anchor=CENTER, image=Bg_image)

    # ! Sub canvas

    registration_subcanvas = Canvas(
        registration_canvas, width=400, height=height, bg='#121512', highlightthickness=0)
    registration_canvas.create_window(
        width / 2, height / 2, anchor=CENTER, window=registration_subcanvas)

    # ! Registration screen Entry Widget UI

    registration_img_main = PhotoImage(file='Pictures/Icons/add-user-100.png')
    registration_subcanvas.create_image(200, 60, anchor=CENTER, image=registration_img_main)

    # ? Username

    registration_subcanvas.create_text(
        70, 150, anchor=CENTER, text="Username", font=('corbel', 12), fill='#1DB954')

    logo_username = PhotoImage(file='Pictures/Icons/username-add-30.png')
    registration_subcanvas.create_image(
        50, 180, anchor=CENTER, image=logo_username)

    Username = Entry(registration_subcanvas, bg='#121512',
                     relief=FLAT, fg='white', width=25, font=('corbel', 17,))
    registration_subcanvas.create_window(
        220, 180, anchor=CENTER, window=Username)

    registration_subcanvas.create_line(
        69, 198, 371, 198, width=2, fill='#1DB954')

    # ? Password #121512

    registration_subcanvas.create_text(
        70, 250, anchor=CENTER, text="Password", font=('corbel', 12), fill='#1DB954')

    logo_password = PhotoImage(file='Pictures/Icons/password-add-30.png')
    registration_subcanvas.create_image(
        50, 280, anchor=CENTER, image=logo_password)

    Password = Entry(registration_subcanvas, bg='#121512',
                     relief=FLAT, fg='white', width=25, font=('Corbel', 17))
    registration_subcanvas.create_window(
        220, 280, anchor=CENTER, window=Password)

    registration_subcanvas.create_line(
        69, 298, 371, 298, width=2, fill='#1DB954')

    # Reenter Password
    registration_subcanvas.create_text(
        97, 350, anchor=CENTER, text="Confirm Password", font=('corbel', 12), fill='#1DB954')

    logo_re_password = PhotoImage(file='Pictures/Icons/sign-in-form-password-30.png')
    registration_subcanvas.create_image(
        50, 380, anchor=CENTER, image=logo_re_password)

    reenter_Password = Entry(registration_subcanvas, bg='#121512',
                             relief=FLAT, fg='white', width=25, font=('Corbel', 17))
    registration_subcanvas.create_window(
        220, 380, anchor=CENTER, window=reenter_Password)

    registration_subcanvas.create_line(
        69, 398, 371, 398, width=2, fill='#1DB954')

    # gmail
    registration_subcanvas.create_text(
        58, 450, anchor=CENTER, text="Email", font=('corbel', 12), fill='#1DB954')

    gmail_image = PhotoImage(file='Pictures/Icons/gmail-30.png')
    registration_subcanvas.create_image(
        50, 480, anchor=CENTER, image=gmail_image)

    gmail_entry = Entry(registration_subcanvas, bg='#121512',
                        relief=FLAT, fg='white', width=25, font=('Corbel', 17))
    registration_subcanvas.create_window(
        220, 480, anchor=CENTER, window=gmail_entry)

    registration_subcanvas.create_line(
        69, 498, 371, 498, width=2, fill='#1DB954')

    # ? Buttons

    register_button_image = PhotoImage(file='Pictures/Icons/sign-up-96.png')
    register_button_image1 = register_button_image.subsample(3, 3)
    register_button = Button(registration_subcanvas, text="  Submit", relief=FLAT, image=register_button_image1,
                             bg='#121512', compound=LEFT,
                             fg='#1DB954', activebackground='#121512', activeforeground='#1DB954', font=('Corbel', 18),
                             command=lambda: register_user_add(Username, Password, reenter_Password, gmail_entry,
                                                               'Loginscreen.py', 'Registration',
                                                               'Are you sure with the credentials?',
                                                               registrationscreen))

    registration_subcanvas.create_window(
        200, 565, anchor=CENTER, window=register_button)

    img_enigma = PhotoImage(file='Pictures/Icons/registration enigma.png')
    registration_subcanvas.create_image(200, 710, anchor=CENTER, image=img_enigma)

    registration_subcanvas.create_text(110, 670, anchor=CENTER,
                                       text='Powered by', font=('Corbel', 15), fill='white')

    ################################################
    registrationscreen.mainloop()


registration_ui()
