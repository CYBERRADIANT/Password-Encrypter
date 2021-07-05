import hashlib as hash
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.constants import INSERT, END
from tkinter.filedialog import asksaveasfilename
from tkinter.scrolledtext import ScrolledText
import mysql.connector as sql
from SupportFunctions import SupportFunctions
from datetime import datetime

###################################################
# ! Objects
supportfunctions = SupportFunctions()


##################################################

def fileselection(variable):
    """ Function Used for selecting files """

    global file_selection
    file_selection = filedialog.askopenfilename(initialdir='/PicturesOptional',
                                                title='Select file to Encrypt or decrypt',
                                                filetypes=(('.txt', '*.txt'),))
    try:
        with open(file_selection, 'r') as file_object:
            content = file_object.read()

        variable.delete(1.0, END)
        variable.insert(INSERT, content)
    except:
        print('Ignored Hash')


###################################################
def mainwindow():
    """The main window"""
    PasswordManager = Tk()
    PasswordManager.resizable(0, 0)
    PasswordManager.overrideredirect(True)
    width = PasswordManager.winfo_screenwidth()
    height = PasswordManager.winfo_screenheight()
    PasswordManager.geometry(f'{width}x{height}')
    ###########################################################

    # ! Main canvas

    Password_Encrypter_Canvas = Canvas(
        PasswordManager, bg='#2c2f33', height=(height), width=(width), highlightthickness=0)

    Password_Encrypter_Canvas.pack()

    ##########################################################
    # ! Scrolled text and other widgets

    global Password_input
    Password_input = ScrolledText(Password_Encrypter_Canvas, width=60, height=15, background='#222222',
                                  foreground='white', font=("Segoe UI", 15,), relief=FLAT)

    Password_input.insert(INSERT, 'Give the text here to Encrypt....')

    Password_Encrypter_Canvas.create_window(
        60, 130, anchor=NW, window=Password_input)

    ###########################################################

    # ! BG Image and Icons and buttons

    Bg_Image = supportfunctions.image_resizer(
        width, height, 'Pictures/Mainscreen1.jpg')

    Password_Encrypter_Canvas.create_image(
        width / 2, height / 2, anchor=CENTER, image=Bg_Image)

    logo = PhotoImage(file='Pictures/Icons/icons8-data-encryption-50.png')
    Password_Encrypter_Canvas.create_image(30, 20, anchor=NW, image=logo)

    img_enigma = PhotoImage(file='Pictures/Icons/Mainscreen PIC.png')
    Password_Encrypter_Canvas.create_image(
        1240, 720, anchor=CENTER, image=img_enigma)

    img_poweroff = PhotoImage(file='Pictures/Icons/power-off-button-50.png')
    img_button_poweroff = Button(Password_Encrypter_Canvas, bg='#060e23', image=img_poweroff,
                                 activebackground='#060e23',
                                 relief=FLAT, command=lambda: supportfunctions.closewindow(PasswordManager))
    Password_Encrypter_Canvas.create_window(
        1310, 40, anchor=CENTER, window=img_button_poweroff)

    clear_button_img = PhotoImage(file='Pictures/Icons/clear-symbol-64.png')
    clear_button_img_subsample = clear_button_img.subsample(3, 3)
    clear_button = Button(Password_Encrypter_Canvas, image=clear_button_img_subsample, bg='#222222',
                          activebackground='#222222', relief=FLAT,
                          text='  Clear', fg='white', font=('Corbel', 14), width=150, height=33,
                          activeforeground='white', compound=LEFT,
                          command=lambda: supportfunctions.clearscreen('TextBox', Password_input))

    Password_Encrypter_Canvas.create_window(
        150, 630, anchor=CENTER, window=clear_button)

    selectfile_img = PhotoImage(file='Pictures/Icons/folder-64.png')
    selectfile_img_subsample = selectfile_img.subsample(3, 3)
    selectfile_button = Button(Password_Encrypter_Canvas, text='  Select File', font=('Corbel', 14),
                               image=selectfile_img_subsample, bg='#222222', activebackground='#222222', relief=FLAT,
                               compound=LEFT, fg='white', activeforeground='white', width=150, height=33,
                               command=lambda: fileselection(Password_input))
    Password_Encrypter_Canvas.create_window(
        370, 630, anchor=CENTER, window=selectfile_button)

    logout_img = PhotoImage(file='Pictures/Icons/rounded-left-64.png')
    logout_img_subsample = logout_img.subsample(3, 3)
    logout_button = Button(Password_Encrypter_Canvas, text='  Logout', font=('Corbel', 14), image=logout_img_subsample,
                           bg='#222222', activebackground='#222222', relief=FLAT,
                           compound=LEFT, fg='white', activeforeground='white', width=150, height=33,
                           command=lambda: supportfunctions.open_close_script('Loginscreen.py', 'Logging Out',
                                                                              'Are you sure to Log out?',
                                                                              PasswordManager))
    Password_Encrypter_Canvas.create_window(
        600, 630, anchor=CENTER, window=logout_button)
    
    def clock():
        "Function for clock "

        current_time=datetime.now()
        stringformat=f'{current_time.hour}:{current_time.minute}:{current_time.second}'
        Password_Encrypter_Canvas.itemconfig(clock_time, text=stringformat)
        Password_Encrypter_Canvas.after(1000, clock)

        
    clock_time = Password_Encrypter_Canvas.create_text(1050, 280, anchor=CENTER,  font=('Corbel', 40), fill='white')
    clock()
        

    encrypt_img = PhotoImage(file='Pictures/Icons/lock-64.png')
    encrypt_img_subsample = encrypt_img.subsample(3, 3)
    encrypt_button = Button(Password_Encrypter_Canvas, text='  Encrypt', font=('Corbel', 14),
                            image=encrypt_img_subsample, bg='#222222', activebackground='#222222', relief=FLAT,
                            compound=LEFT, fg='white', activeforeground='white', width=150, height=33,
                            command=lambda: encrypter_ui(PasswordManager, width, height, ))
    Password_Encrypter_Canvas.create_window(
        1050, 380, anchor=CENTER, window=encrypt_button)

    decrypt_img = PhotoImage(file='Pictures/Icons/unlock-64.png')
    decrypt_img_subsample = decrypt_img.subsample(3, 3)
    decrypt_button = Button(Password_Encrypter_Canvas, text='  Decrypt', font=('Corbel', 14),
                            image=decrypt_img_subsample, bg='#222222', activebackground='#222222', relief=FLAT,
                            compound=LEFT, fg='white', activeforeground='white', width=150, height=33,
                            command=lambda: decrypter_ui(PasswordManager, width, height))
    Password_Encrypter_Canvas.create_window(
        1050, 470, anchor=CENTER, window=decrypt_button)

    ############################################################
    # ! Create text

    Password_Encrypter_Canvas.create_text(1100, 680, anchor=CENTER,
                                          text='Powered by', font=('Corbel', 20), fill='white')

    Password_Encrypter_Canvas.create_text(85, 17, anchor=NW, text='Password Encrypter', font=(
        "Corbel", 35,), fill='#1DB954')

    ############################################################
    # ! Looping
    PasswordManager.mainloop()


def md5(text):
    hashtxt = hash.md5()
    hashtxt.update(text)
    return hashtxt.hexdigest()


#########################################################
Lower = {'a': 'SJMAw', 'b': 'zjf4A', 'c': 'ajnkj', 'd': '1mTci', 'e': 'hgIgq', 'f': 'Eoqj5', 'g': 'GsyTj',
         'h': 'BA0BL',
         'i': 'OUj2I', 'j': 'w2nDo', 'k': 'i6GTH', 'l': 'PXBvF', 'm': 'pUQr9',
         'n': 'dvkmo', 'o': 'ZZdHN', 'p': 'Gstgk', 'q': 'Mbg37', 'r': 'EXxOW', 's': 'LwjTm', 't': 'tQM0y',
         'u': 'myZD2',
         'v': 'W4Cho', 'w': 'JQ6ve', 'x': 'ofm23', 'y': 'crMo2', 'z': 'Ts5kU', '\n': '$', ' ': '#', '.': '_',
         '@': 'zHGzG',
         '% ': 'c3Wc6', '?': 'xTQkB', ',': 'f7SRM', ';': 'G3kBk', '/ ': 'hn7PN', '(': 'Q0bG6', '-': 'DQlmM',
         ':': '1qDtY', ')': 'Fn7QC'}

Upper = {'A': 'lxw7q', 'B': 'v3l0r', 'C': '5y6eo', 'D': 'zi0v2', 'E': 'zin56', 'F': 'uf54n', 'G': 'tp933', 'H': 'pjlw0',
         'I': 'ny7uk', 'J': '6oaqq', 'K': 'lvvkl',
         'L': 'wi9im', 'M': 'ac3j9', 'N': 'mk1nx', 'O': '5plgh', 'P': 'k3p2l', 'Q': 'u8rcm', 'R': 'g99dh', 'S': '4ftj0',
         'T': 'muujd', 'U': 'iyynq', 'V': 'iyynq', 'W': 'di6oh', 'X': '3mimy', 'Y': 'f64kg', 'Z': 'ntv0v'}

numbers = {'1': 'aKdzH', '2': 'jFKvg', '3': 'vOvAo', '4': 'QVlSi',
           '5': 'xOZcg', '6': 'Zotnw', '7': 'PQYqm', '8': 'iHjJq', '9': 'RbBvR'}


#  &

def encrypter_ui(master, width, height):
    """Toplevel's components"""

    Encrypter_top_lvl = Toplevel(master)

    Encrypter_top_lvl.geometry(
        supportfunctions.centerwindow(master, 700, 600))

    Encrypter_top_lvl.iconbitmap('icon.ico')

    Encrypter_top_lvl.title('Encrypt window')

    Encrypter_top_lvl.resizable(0, 0)

    # * Canvas
    Toplvl_canvas = Canvas(
        Encrypter_top_lvl, background='#191414', width=700, height=600, relief=FLAT)

    image = supportfunctions.image_resizer(
        width, height, 'Pictures\Small screen .jpg')
    Bg_Image = Toplvl_canvas.create_image(
        width / 2, height / 2, anchor=CENTER, image=image)

    scrolledtext = ScrolledText(Toplvl_canvas, width=70, height=20, background='#1a1a1a',
                                foreground='white', font=("Segoe UI", 11,), relief=FLAT)

    Toplvl_canvas.create_window(
        30, 100, anchor=NW, window=scrolledtext)

    Toplvl_canvas.create_text(
        30, 10, anchor=NW, text='Encrypted Text' + u'  \U0001F512', font=(
            "corbel", 32,), fill='#1DB954')

    save_img = PhotoImage(file='Pictures/Icons/save-close-64.png')
    save_img_subsample = save_img.subsample(2, 2)
    save_in_file = Button(Toplvl_canvas, text='  Save in File', font=('Corbel', 14), image=save_img_subsample,
                          bg='#222222', activebackground='#222222', relief=FLAT,
                          compound=LEFT, fg='white', activeforeground='white', width=150, height=33,
                          command=lambda: save_file())
    Toplvl_canvas.create_window(
        240, 530, anchor=NW, window=save_in_file)

    tmp2 = open('Tempread2.txt', 'r+')
    tmp2.truncate(0)
    tmp2.close()

    tmp = open('Tempread.txt', 'r+')
    tmp.truncate(0)
    tmp.close()

    def gettext():
        tmp = open('Tempread.txt', 'w+')
        getted = Password_input.get(1.0, END)
        tmp.write(getted)
        tmp.close()

    def Encryption():
        gettext()
        tmp = open('Tempread.txt', 'r+')
        lists = tmp.readlines()

        templist = []

        for position, line in enumerate(lists):
            tempstr = ''
            for i in line:
                if i in Lower.keys():
                    tempstr += Lower[i] + '{'
                elif i in Upper.keys():
                    tempstr += Upper[i] + '{'
                elif i in numbers.keys():
                    tempstr += numbers[i] + '{'
                else:
                    tempstr += i + ','

            templist.append(tempstr + '\n')
        tmp2 = open('Tempread2.txt', 'w+')
        tmp2.writelines(templist)
        tmp2.close()

        tmp2 = open('Tempread2.txt', 'r+')
        input = tmp2.read()
        scrolledtext.insert(INSERT, input)

    def save_file():
        """Function to save the encrypted text"""
        desktop = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        ask = asksaveasfilename(filetype=[('Text files', '*.txt')], defaultextension='.txt',
                                initialdir=desktop)

        savetext = scrolledtext.get(1.0, END)
        with open(ask, 'w') as files:
            files.write(savetext)

        connectdb = sql.connect(
            host='localhost',
            user='root',
            passwd='Vishwaa6789',
            database='userdata'
        )
        cursor = connectdb.cursor()
        insert_in_table = 'INSERT INTO hash (name, hash) VALUES (%s, %s)'

        def hashedfile():
            with open(ask, 'rb') as hashedfiles:
                return md5(hashedfiles.read())

        data = (f'{os.environ.get("USERNAME")}', f'{hashedfile()}')
        cursor.execute(insert_in_table, data)
        connectdb.commit()

    Encryption()
    Toplvl_canvas.pack()
    Encrypter_top_lvl.mainloop()


# ! Dictionaries
reverse_lower = {'SJMAw': 'a', 'zjf4A': 'b', 'ajnkj': 'c', '1mTci': 'd', 'hgIgq': 'e', 'Eoqj5': 'f', 'GsyTj': 'g',
                 'BA0BL': 'h', 'OUj2I': 'i', 'w2nDo': 'j', 'i6GTH': 'k', 'PXBvF': 'l', 'pUQr9': 'm',
                 'dvkmo': 'n', 'ZZdHN': 'o', 'Gstgk': 'p', 'Mbg37': 'q', 'EXxOW': 'r', 'LwjTm': 's', 'tQM0y': 't',
                 'myZD2': 'u', 'W4Cho': 'v', 'JQ6ve': 'w', 'ofm23': 'x', 'crMo2': 'y', 'Ts5kU': 'z', '#': ' ',
                 '$': '\n', '_': '.', 'zHGzG': '@', 'c3Wc6': '% ', 'xTQkB': '?', 'f7SRM': ',', 'G3kBk': ';',
                 'hn7PN': '/ ', 'Q0bG6': '(', 'DQlmM': '-', '1qDtY': ':', 'Fn7QC': ')'}

reverse_upper = {'lxw7q': 'A', 'v3l0r': 'B', '5y6eo': 'C', 'zi0v2': 'D', 'zin56': 'E', 'uf54n': 'F', 'tp933': 'G',
                 'pjlw0': 'H', 'ny7uk': 'I', '6oaqq': 'J', 'lvvkl': 'K', 'wi9im': 'L',
                 'ac3j9': 'M', 'mk1nx': 'N', '5plgh': 'O', 'k3p2l': 'P', 'u8rcm': 'Q', 'g99dh': 'R', '4ftj0': 'S',
                 'muujd': 'T', 'iyynq': 'V', 'di6oh': 'W', '3mimy': 'X', 'f64kg': 'Y', 'ntv0v': 'Z'}

reverse_numbers = {'aKdzH': '1', 'jFKvg': '2', 'vOvAo': '3', 'QVlSi': '4',
                   'xOZcg': '5', 'Zotnw': '6', 'PQYqm': '7', 'iHjJq': '8', 'RbBvR': '9'}


###########################################
# !Functions

def decrypter_ui(master, width, height):
    """ Function defines the UI """
    master = master

    Decrypter_top_lvl = Toplevel(master)

    Decrypter_top_lvl.geometry(
        supportfunctions.centerwindow(master, 700, 600))

    Decrypter_top_lvl.iconbitmap('icon.ico')

    Decrypter_top_lvl.title('Decrypt window')

    Decrypter_top_lvl.resizable(0, 0)

    # * Canvas
    Toplvl_canvas = Canvas(
        Decrypter_top_lvl, background='#191414', width=700, height=600, relief=FLAT)

    image = supportfunctions.image_resizer(
        width, height, 'Pictures\Small screen .jpg')

    Bg_Image = Toplvl_canvas.create_image(
        width / 2, height / 2, anchor=CENTER, image=image)

    scrolledtext = ScrolledText(Toplvl_canvas, width=70, height=20, background='#222222',
                                foreground='white', font=("Segoe UI", 11,), relief=FLAT)

    Toplvl_canvas.create_window(
        30, 100, anchor=NW, window=scrolledtext)

    Toplvl_canvas.create_text(
        30, 10, anchor=NW, text='Decrypted Text' + u"  \U0001F513", font=(
            "corbel", 32,), fill='#1DB954')

    save_img = PhotoImage(file='Pictures/Icons/save-close-64.png')
    save_img_subsample = save_img.subsample(2, 2)
    save_in_file = Button(Toplvl_canvas, text='  Save in File', font=('Corbel', 14), image=save_img_subsample,
                          bg='#222222', activebackground='#222222', relief=FLAT,
                          compound=LEFT, fg='white', activeforeground='white', width=150, height=33,
                          command=lambda: save_file())
    Toplvl_canvas.create_window(240, 530, anchor=NW, window=save_in_file)

    tmp2 = open('tempread2.txt', 'r+')
    tmp2.truncate(0)
    tmp2.close()

    tmp = open('Tempread.txt', 'r+')
    tmp.truncate(0)
    tmp.close()

    def gettext():
        tmp = open('Tempread.txt', 'w+')
        getted = Password_input.get(1.0, END)
        tmp.write(getted)
        tmp.close()

    def Decryption():
        """Function for decrypting"""
        gettext()

        connectdb = sql.connect(
            host='localhost',
            user='root',
            passwd='Vishwaa6789',
            database='userdata')

        hashinlist = []
        cursor = connectdb.cursor()
        cursor.execute('SELECT hash FROM hash')
        results = cursor.fetchall()

        for result in results:
            for appending in result:
                hashinlist.append(appending)
        try:
            with open(file_selection, 'rb') as checkfile:
                hashcheck = md5(checkfile.read())

        except:
            messagebox.showerror('Error', 'Select a FIle to encrypt')
        if hashcheck in hashinlist:
            tmp = open('Tempread.txt', 'r+')
            lists = tmp.readlines()
            templist = []

            for position, line in enumerate(lists):

                tempstr = ''
                for i in line.split('{'):
                    if i in reverse_lower.keys():
                        tempstr += reverse_lower[i]
                    elif i in reverse_upper.keys():
                        tempstr += reverse_upper[i]
                    elif i in reverse_numbers.keys():
                        tempstr += reverse_numbers[i]
                    else:
                        tempstr += i
                templist.append(tempstr)

            tmp2 = open('Tempread2.txt', 'w+')
            tmp2.writelines(templist)
            tmp2.close()

            tmp2 = open('Tempread2.txt', 'r+')
            input = tmp2.read()
            scrolledtext.insert(INSERT, input)
        else:
            messagebox.showerror(
                'Error', 'cipher has been modified or not authentic ')

    def save_file():
        desktop = os.path.join(os.path.join(
            os.environ['USERPROFILE']), 'Desktop')
        ask = asksaveasfilename(filetype=[('Text files', '*.txt')], defaultextension='.txt',
                                initialdir=desktop)

        savetext = scrolledtext.get(1.0, END)
        with open(ask, 'w') as files:
            files.write(savetext)

    Decryption()
    Toplvl_canvas.pack()
    Decrypter_top_lvl.mainloop()


mainwindow()
