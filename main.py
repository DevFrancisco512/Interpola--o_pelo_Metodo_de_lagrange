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
        center = wsize[0]
        root.geometry('820x480')

        backgrafic = tki.Frame(root, width=640, height=480)
        backgrafic.grid(column=1, row=1,rowspan=3)
        content = tki.Frame(root, width=180, height=480, bg='grey')
        content.grid(column=0, row=0, rowspan=3)

        strvet1 = StringVar()
        entrytvet1 = Entry(content,font=('Arial 14'))
        x, y = [45, 10]
        entrytvet1.place(x=45, y=10, width=130)

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
