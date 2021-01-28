from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk


window = Tk()

window.title("Belor")
window.geometry('800x350')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

# menu = Menu(window)


tab_control.add(tab1, text='Main')
tab_control.add(tab2, text='Diagnostics')
tab_control.add(tab3, text='Rear Cam')
# window.config(menu=menu)
lbl = Label(tab1, text="tab1", font=("roboto", 50))
# lbl.pack(padx=20, pady=20)
lbl.grid(column=6, row=0)

style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(tab1, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = 70

bar.grid(column=6, row=2)

tab_control.pack(expand=1, fill='both')

window.mainloop()
