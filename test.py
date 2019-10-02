from tkinter import *
import math
import time
import gauge as G

root = Tk()

##### GAUGE TEST #####

val = StringVar()
myg = G.VGauge(40, 200, 0, 100, 50)
myg.bg_color = 'white'
myg.border_color = 'black'
myg.bar_color = 'red'
myg.show(root).pack()
ent = Entry(root, textvariable=val)
ent.pack()
btn = Button(root, text='click me', command=lambda: myg.update(int(val.get())))
btn.pack()

myvu = G.VVuMeter_Mono(0,100,0)
myvu.show(root).pack()



##### ROTATION #####

c = Canvas(root, width=300, height=300, bg='white')
c.pack()
angle = 30
longueur = 150
p1 = (10, 10)
p2 = (p1[0] + (longueur * (math.cos(math.radians(angle)))), p1[1] + (longueur * (math.sin(math.radians(angle)))))
print(p1)
print(p2)
c.create_line((p1, p2), width=10)
line = None
while True:
    # c.delete(line)
    # angle += 10
    # p1 = (10, 10)
    # p2 = (p1[0] + (longueur * (math.cos(math.radians(angle)))), p1[1] + (longueur * (math.sin(math.radians(angle)))))
    # print(p1)
    # print(p2)
    # line = c.create_line((p1, p2), width=10)
    # time.sleep(1)
    root.update()

root.mainloop()
