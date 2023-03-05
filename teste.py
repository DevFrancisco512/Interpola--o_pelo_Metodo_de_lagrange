import matplotlib.pyplot as plt
import numpy as np
import tkinter as tki
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 


def interpolLagrange(x, vetx, vety) -> float:
    yp = 0
    indexy = 0
    for xi in vetx:
        L = 1
        for xj in vetx:
            if xi != xj:
                L *= (x-xj)/(xi-xj)
        yp += vety[indexy]*L
        indexy += 1
        
    return yp

def genGrafico(vetx, vety, Px, Py):
        fig = Figure(figsize = (5, 5), 
                 dpi = 100)
        ax = fig.add_subplot(111) 
        
        minX = min(vetx)
        maxX = max(vetx)
        w = np.arange(minX-minX%10, maxX+maxX%10, 0.01)
        yw = []
        for pos in w:
            yw.append(interpolLagrange(pos, vetx, vety))

        ax.plot(w, yw, 'b-')
        ax.plot(vetx, vety, 'ro')
        ax.plot(Px, Py, 'go')
        ax.set_ylabel('eixo y')
        ax.set_xlabel('eixo x')

        canvas = FigureCanvasTkAgg(fig, master = frame)
        canvas.__str__()
        canvas.draw() 
    
        
        canvas.get_tk_widget().pack() 
    
        
        toolbar = NavigationToolbar2Tk(canvas, frame) 
        toolbar.update()
    
        
        canvas.get_tk_widget().pack()


root = tki.Tk()
frame = tki.Frame(root).pack()
vetx = [1, 2, 4]
vety = [1, 2, 4]
px = 3
py=interpolLagrange(px, vetx, vety)
Button(frame, text='plot', command=lambda:genGrafico(vetx, vety, px, py)).pack()
tki.mainloop()

def retorna():  
    vetx = [1, 2, 3, 4]
    vety = [2, 4, 6, 8]
    return vetx, vety

r1, r2 = retorna()
print(r1)
print(r2)