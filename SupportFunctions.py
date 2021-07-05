import subprocess
import subprocess
import sys
from tkinter import Image, filedialog
from tkinter import messagebox
from tkinter.constants import END, INSERT

from PIL import ImageTk, Image


class SupportFunctions:
    """ class of functions that has the functions of the Application """

    def centerwindow(self, master, width, height):
        """ Function to keep the window in the middle of the screen """

        self.width = width
        self.height = height

        # * Get screen width and height

        self.screenwidth = master.winfo_screenwidth()
        self.screenheight = master.winfo_screenheight()

        # * Calculate position x, y
        x = (self.screenwidth / 2) - (self.width / 2)
        y = (self.screenheight / 2) - (self.height / 2)

        return '%dx%d+%d+%d' % (self.width, self.height, x, y)

    def fullscreen(self, master):
        """ Function for creating a full screen """

        self.master = master

        self.width = self.master.winfo_screenwidth()

        self.height = self.master.winfo_screenheight()

        return "%dx%d" % (self.width, self.height)

    def clearscreen(self, widget, variable):
        """Function to clear the text inside a widget """

        self.widget = widget
        self.variable = variable

        if self.widget == 'TextBox':
            self.variable.delete(1.0, END)
        else:
            self.variable.delete(0, END)

    def fileselection(self, title, variable):

        """ Function Used for selecting files """

        self.title = title
        self.variable = variable

        self.file_selection = filedialog.askopenfilename(initialdir='/PicturesOptional',
                                                         title=self.title,
                                                         filetypes=(('.txt', '*.txt'),))

        try:
            with open(self.file_selection) as file_object:
                content = file_object.read()

            # self.variable.delete(1.0, END)

            self.clearscreen("TextBox", self.variable)

            self.variable.insert(INSERT, content)
        except:
            pass

    def closewindow(self, window):

        "universal function to close window"
        self.window = window

        self.ask = messagebox.askyesno('Close Window', 'Are you sure to Exit?')

        if self.ask == 1:
            self.window.destroy()

    def image_resizer(self, width, height, path):

        "Function for resizing images"

        self.width = width
        self.height = height
        self.path = path

        self.open_image = Image.open(self.path)

        self.resize_image = self.open_image.resize((self.width, self.height), Image.ANTIALIAS)

        self.Image = ImageTk.PhotoImage(self.resize_image)

        return self.Image

    def fileselection_converted(self):
        pass

    def open_close_script(self, pythonfile, title, message, window):

        self.pythonfile = pythonfile
        self.title = title
        self.message = message
        self.window = window

        self.ask = messagebox.askyesno(self.title, self.message, parent=self.window)

        if self.ask == 1:
            subprocess.run(['python', f'{self.pythonfile}'])
            sys.exit(0)
