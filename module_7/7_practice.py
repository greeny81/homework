import tkinter
import os

from tkinter import filedialog
from tkinter import *
from tkinter import messagebox

def file_select():
    file_name = filedialog.askopenfilename(initialdir='/', title='Choose',
                                          filetypes=(('Text files','.txt'),('All files','*')))
    text['text'] = file_name
    if file_name:
        os.startfile(file_name)

def show_msg_info():
    text_menu.config(text='Chose file and system open them')

def show_msg_about():
    text_menu.config(text='This is first eplorer by python \n ver. 1.0')

def exit_program():
    window.quit()


window = Tk()
window.title('Explorer')
window.geometry('350x100')
window.resizable(False, False)
window.configure(bg='white')

mainmenu = Menu(window)
window.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Info", command=show_msg_info,  state="normal")
filemenu.add_command(label="About", command=show_msg_about,  state="normal")
filemenu.add_command(label="Exit", command=exit_program)
mainmenu.add_cascade(label="Menu", menu=filemenu)

text = tkinter.Label(window, text='File', height=2, width=50,  background='silver')
text.grid(column=1, row=1)

button_select = tkinter.Button(window,  height=1, text='Choose file', background='silver', command=file_select)
button_select.grid(column=1, row=2)

text_menu = tkinter.Label(window, text='',   background='yellow', border=1)
text_menu.grid(column=1, row=3)

window.mainloop()