from tkinter import *
import tkinter as tki
import matplotlib.pyplot as plt
import numpy as np


# Por meio da interpolação de Lagrange a função retorna  yp do xp correspondente
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

class tela():
    def __init__(self) -> None:
        root = Tk()
        root.title('Método de lagrange')
        wsize = root.winfo_screenwidth(), root.winfo_screenheight()
        rsize = 840, 480
        center = int((wsize[0]/2)-(rsize[0]/2)), int((wsize[1]/2)-(rsize[1]/2))
        root.geometry(f'{rsize[0]}x{rsize[1]}+{center[0]}+{center[1]}')

        backgrafic = Frame(root, width=640, height=480)
        backgrafic.grid(column=1, row=1,rowspan=3)
        backgrafic['borderwidth'] = 2
        content = Frame(root, width=180, height=480, bg='grey')
        content.grid(column=0, row=0, rowspan=3)

        vetEntrys = list()
        entryvet1 = StringVar()
        vetEntrys.append(Entry(content,font=('Arial 14'), textvariable=entryvet1))

        entrytvet2 = StringVar()
        vetEntrys.append(Entry(content, font='Arial 14', textvariable=entrytvet2))

        entrytvet3 = StringVar()
        vetEntrys.append(Entry(content, font='Arial 14', textvariable=entrytvet3))

        x = 45
        y = 10
        for entry in vetEntrys:
            entry.place(x=x, y=y, width=130)
            y += 30
        
        btncalcular = Button(root, text='Calcular', font='Arial 16', background='#1B64F3', activebackground='#5B8DEF', fg='white')
        btncalcular.place(x=30, y=400)
        btncalcular.focus_set()
        btncalcular.bind("return", lambda:print('io'))

        mainloop()


    def genGrafico(self, vetx, vety, n, xp, yp):
        minX = min(vetx)
        maxX = max(vetx)
        w = np.arange(minX-minX%10, maxX+maxX%10, 0.01)
        yw = []
        for pos in w:
            yw.append(interpolLagrange(pos, vetx, vety))
        
        ax = plt.axes()
        ax.plot(w, yw, 'b-')
        ax.plot(vetx, vety, 'ro')
        ax.plot(xp, yp, 'go')
        ax.set_ylabel('eixo y')
        ax.set_xlabel('eixo x')
        plt.savefig('images/grafico.png')


if __name__ == '__main__':
    tela()
