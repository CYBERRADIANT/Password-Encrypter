from tkinter import Button, Label
from tkinter.constants import NORMAL
from tkinter.font import BOLD


class HoverButton(Button):

    '''A HoverButton Child class for the parent Button class in the tkinter module.'''

    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)

        # * Setting the variable for the Default Background
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]

        self['width'] = 16
        self['height'] = 1
        # * Binding the events to the functions
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

      # * Functions
    def on_enter(self, event):
        '''Hover effect when the mouse pointer is over the button'''
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']
        

    def on_leave(self, event):
        '''Hover effect when the mouse pointer stops hovering over the button.'''
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground
    

class UpdatingLabel(Label):
    
    ''' A child class of label with a custom feature of updating '''

    def _init_(self, master, time, updating_texts, **kw):
        '''A label which updates itself after a definite amount of time.'''
        Label._init_(self, master=master, **kw)
        self.updating_texts = updating_texts
        self['text'] = self.updating_texts[0]
        self.time = time
        self.called = 0
        self.after(self.time, self.update_label)

    def update_label(self):
        '''A function that updates the label periodically'''
        if self.called != len(self.updating_texts) - 1:
            self.new_text = self.updating_texts[self.called + 1]
            self.configure(text=self.new_text)
            self.called += 1
        else:
            self.configure(text=self.updating_texts[0])
            self.called = 0
        self.after(self.time, self.update_label)
