from tkinter import *
import os
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from matplotlib.figure import Figure
import random
import numpy as np
import time



def Move():
    global motion, dots, bd1, bd2, bd3, bd4, motion
    for num in range(population):
        stepX = random.randint(-10, 10)
        stepY = random.randint(-10, 10)
        if ((dots[num][0] + stepX) < bd2 and (dots[num][0] + stepX) > bd4):
            dots[num][0] += stepX
        else:
            dots[num][0] -= stepX
        if ((dots[num][1] + stepY) < bd3 and (dots[num][1] + stepY) > bd1):
            dots[num][1] += stepY
        else:
            dots[num][1] -= stepY
        can.coords(Dots[num], dots[num][0], dots[num][1], dots[num][0] + 5, dots[num][1] + 5)
    if (True):
        root.after(120, Move)

def Population():
    global population
    global dots
    dots = np.zeros((population, 2))
    for i in range(0, population):
        dots[i] = (random.randint(50, winsize[0]-380), random.randint(110, winsize[1]-50))
        x1, y1 = dots[i]
        Dots.append(can.create_oval(x1, y1, x1+5, y1+5, fill='#aa3333'))


'''def find_nearest_vector(array, value):    # пример заражения самого близкого индивида
    idx = np.array([np.linalg.norm(x+y) for (x,y) in array-value]).argmin()
    return array[idx]

def Desise():
    global illdots, dots, day
    #print(illdots)
    il = []
    for i in illdots:
        dots1
        a = np.where(dots == find_nearest_vector(dots1, dots[i]))[0]
        for j in a:
            if (j != i):
                il.append(j)
                can.itemconfigure(Dots[j], fill='green')
                break
    for k in il:
        illdots.append(k)
    day += 1
    can.itemconfigure(lday, root, text="День: "+ str(day), ba='#111', fg='#ddd', font=['Akrobat Bold', 22])
    if (motion):
        root.after(3000, Desise)'''


def Epidemic():
    global day, lday, illdots, motion, speed, Dots, noill, ill, population, figure, subp
    day = day + 1
    speed = 2**(day)

    text = "День: " + str(day)
    lday['text'] = text
    text = "Скорость распространения:  "+'\n'+ str(speed) + " чел/день"
    lspeed['text'] = text
    text = "Здоровые:  "+ str(noill)
    lnoill['text'] = text
    text = "Заболевшие:  " + str(ill)
    lill['text'] = text

    print("speed: "+str(speed))
    for i in range(0, speed):
        try:
            can.itemconfigure(Dots[i], fill='green')
            #can.itemconfigure(Dots[i], fill='#ff5555')
            np.delete(illdots, i, axis=0)
            if (noill > 0):
                noill -=1
            if (ill < population):
                ill +=1
        except:
            motion = False

    if (motion):
        dayarray.append(day)
        illarray.append(ill)
        subp.cla()
        subp.tick_params(axis='x', colors='white')
        subp.tick_params(axis='y', colors='white')
        subp.set_xlabel('Количество дней', color='#d0d0d0', size=20)
        subp.set_ylabel('Количество заразившихся', color='#d0d0d0', size=20)
        subp.plot(dayarray, illarray, color='green', linewidth=3)
        cass.draw()

    if (motion):
        root.after(3000, Epidemic)
    else:
        print("Популяция полностью заражена!")

day = -1
dayarray = []
illarray = []
ill = 0
population = 1000
noill = population
speed = 0
motion = True
winsize = [1280, 720]
bd1 = 100
bd2 = winsize[0] -370
bd3 = winsize[1] - 40
bd4 = 40
dots = []
Dots = []
zeroP = random.randint(0, 1000)
illdots = []
illdots.append(zeroP)

winsize = [1280, 720]
root = Tk()
root.title("Инфицирование популяции")
root.geometry(str(winsize[0])+'x'+str(winsize[1]))
root.resizable(False, False)
root["bg"]="#fff"

can = Canvas(width=1272, height=714, bg='#111')
lday=Label(root, text="День: "+ str(day+1), ba='#111', fg='#ddd', font=['Akrobat Bold', 22])
lday.place(x=15, y=7)
lpopulation=Label(root,anchor="nw", text="Популяция: "+ str(population), ba='#111', fg='#ddd', font=['Akrobat Bold', 22])
lpopulation.place(x=winsize[0]/3, y=7)
lpopulation2=Label(root, text="Популяция:  "+ str(population), ba='#111', fg='#aaa', font=['Akrobat Bold', 14])
lpopulation2.place(x=winsize[0]-300, y=5)
lnoill=Label(root, text="Здоровые:  "+ str(noill), ba='#111', fg='#aaa', font=['Akrobat Bold', 14])
lnoill.place(x=winsize[0]-300, y=45)
lill=Label(root, text= "Заболевшие:  "+ str(ill), ba='#111', fg='#aaa', font=['Akrobat Bold', 14])
lill.place(x=winsize[0]-300, y=85)

lspeed=Label(root, text="Скорость распространения:  "+'\n'+ str(speed) + " чел/день", ba='#111', fg='#aaa', font=['Akrobat Bold', 14])
lspeed.place(x=winsize[0]-300, y=205)
lgraph=Label(root, text="График заболевания", ba='#111', fg='#aaa', font=['Akrobat Bold', 14])
lgraph.place(x=winsize[0]-300, y=355)

bord1 = can.create_line(20, 80, winsize[0]-350, 80)
bord2 = can.create_line(winsize[0]-350, 80, winsize[0]-350, winsize[1] - 20)
bord3 = can.create_line(winsize[0]-350, winsize[1] - 20, 20, winsize[1] - 20)
bord4 = can.create_line(20, winsize[1] - 20, 20, 80)
can.itemconfigure(bord1, fill='#57a', width = 3)
can.itemconfigure(bord2, fill='#57a', width = 3)
can.itemconfigure(bord3, fill='#57a', width = 3)
can.itemconfigure(bord4, fill='#57a', width = 3)

figure= Figure(figsize=(6,6), dpi=50)
subp = figure.add_subplot(111)
figure.set_facecolor('#101010')
subp.set(facecolor='#ffffff')
subp.set_xlabel('Количество дней', color='#d0d0d0', size=20)
subp.set_ylabel('Количество заразившихся', color='#d0d0d0', size= 20)
cass = FigureCanvasTkAgg(figure, master = root)
cass.draw()
cass.get_tk_widget().place(x=winsize[0]-320, y=395)
can.place(x=2, y=0)


Population()
Move()
illdots = dots
Epidemic()


root.mainloop()
