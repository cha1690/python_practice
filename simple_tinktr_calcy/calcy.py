from tkinter import *

window = Tk()


def mnd_to_rs():
    mnd = float(value.get())/70
    t1.insert(END, mnd)


b1 = Button(window, text="Calculate", command=mnd_to_rs)
b1.grid(row=0, column=0)

value = StringVar()
e1 = Entry(window, textvariable=value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
