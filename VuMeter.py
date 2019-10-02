from tkinter import *
from gauge import VVuMeter

mode = 'multi'


root = Tk()
myVu = VVuMeter(0,100,0)
myVu.bar_number = 20
myVu.bar_height = 10
myVu.interval = 2
myVu.show(root).pack()
myVu.update(0)
v = StringVar()
ent = Entry(root, textvariable=v)
btn = Button(root, text='click', command=lambda:myVu.update(int(v.get())))

ent.pack()
btn.pack()

root.update()


root.mainloop()
