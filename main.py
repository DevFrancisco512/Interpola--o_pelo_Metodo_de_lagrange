from tkinter import *
import tkinter as tki
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

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
    def __init__(self, root) -> None:
        self.root = root
        self.root.title('Método de lagrange')
        wsize = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        rsize = 820, 480
        self.root.minsize(rsize[0], rsize[1])
        self.root.maxsize(rsize[0], rsize[1])
        center = int((wsize[0]/2)-(rsize[0]/2)), int((wsize[1]/2)-(rsize[1]/2))
        root.geometry(f'{rsize[0]}x{rsize[1]}+{center[0]}+{center[1]}')
        self.canvas = None

        self.backgrafic = Frame(self.root, width=600, height=480)
        self.backgrafic.grid(column=1, row=1,rowspan=3)
        self.backgrafic['borderwidth'] = 2
        self.content = Frame(self.root, width=220, height=480, bg='grey')
        self.content.grid(column=0, row=0, rowspan=3)

        vetWidgeths = list()
        self.vetPxy1 = [StringVar(), StringVar()]
        vetWidgeths.append([Label(self.content, text='P(x,y)', font='Arial 10', bg='grey'), Entry(self.content, font='Arial 12', textvariable=self.vetPxy1[0]), Entry(self.content,font='Arial 12', textvariable=self.vetPxy1[1])])

        self.vetPxy2 = [StringVar(), StringVar()]
        vetWidgeths.append([Label(self.content, text='P(x,y)', font='Arial 10', bg='grey'), Entry(self.content, font='Arial 12', textvariable=self.vetPxy2[0]), Entry(self.content,font='Arial 12', textvariable=self.vetPxy2[1])])

        self.vetPxy3 = [StringVar(), StringVar()]
        vetWidgeths.append([Label(self.content, text='P(x,y)', font='Arial 10', bg='grey'), Entry(self.content, font='Arial 12', textvariable=self.vetPxy3[0]), Entry(self.content,font='Arial 12', textvariable=self.vetPxy3[1])])

        # Lendo Px para efetuar a interpolação
        self.Px=StringVar()
        vetWidgeths.append([Label(self.content, text='Px:', font='Arial 10', bg='grey'), Entry(self.content, font='Arial 12', textvariable=self.Px)])

        self.Py = StringVar()
        self.Py.set('0.0')
        vetWidgeths.append([Label(self.content, text='Yp = ', font='Arial 12', bg='gray'), Label(self.content, textvariable=self.Py, font='Arial 12', fg='black', bg='gray')])

        y = 10
        for widgs in vetWidgeths:
            x = 0
            for widg in widgs:
                if type(widg) == tki.Label:
                    widg.place(x=x, y=y)
                    x += 50
                elif type(widg) == tki.Entry:
                    widg.place(x=x, y=y, width=75)
                    x += 85
            y += 50
        
        btncalcular = Button(self.content, text='Calcular', font='Arial 12', activebackground='#5B8DEF',command=lambda:self.calcula())
        btncalcular.place(x=10, y=430)

        btnplot = Button(self.content, text='Plotar Gráfico', font='Arial 12', activebackground='#5B8DEF', command= lambda:self.plotGrafico())
        btnplot.place(x=100, y=430)

        vetWidgeths[0][1].focus()

        mainloop()
    
    def quit(self):
       self.root.destroy

    def calcula(self):
        vetx, vety = self.getCoordinates()
        self.Py.set(str(interpolLagrange(float(self.Px.get()), vetx, vety)))

    def getCoordinates(self):
        vetx=[float(cord[0].get()) for cord in [self.vetPxy1, self.vetPxy2, self.vetPxy3]]
        vety=[float(cord[1].get()) for cord in [self.vetPxy1, self.vetPxy2, self.vetPxy3]]
        return vetx, vety
        

    def plotGrafico(self):
        self.calcula()
        if self.canvas != None:
            self.canvas[0].get_tk_widget().destroy()
            self.canvas[1].destroy()
        vetx, vety = self.getCoordinates()
        minX = min(vetx)
        maxX = max(vetx)
        w = np.arange(minX-minX%10, maxX+maxX%10, 0.01)
        yw = []
        for pos in w:
            yw.append(interpolLagrange(pos, vetx, vety))

        #Gera figura que será passada prara o frame
        fig = Figure(figsize=(6, 4.4), dpi = 100)
        ax = fig.add_subplot(111)

        ax.plot(w, yw, 'b-')
        ax.plot(vetx, vety, 'ro')
        ax.plot(float(self.Px.get()), float(self.Py.get()), 'go')
        ax.set_ylabel('eixo y')
        ax.set_xlabel('eixo x')
        ax.grid(True)
        
        # Plota no frame a figura e a taskbar
        canvas = FigureCanvasTkAgg(fig, master = self.backgrafic)
        canvas.draw()
        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, self.backgrafic)
        canvas.get_tk_widget().pack()
        self.canvas = canvas, toolbar

        

if __name__ == '__main__':
    root = Tk()
    tela(root)

