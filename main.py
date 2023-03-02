from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Por meio da interpolação de Lagrange a função retorna  yp do xp correspondente
def interpolacaoLagrange(x, vetx, vety) -> float:
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

def lerEntradas():
    entradas = None
    cond = True
    while cond:
        try:
            print('Interpolação de Lagrange\n','='*30,'\n')
            entradas = [input(f'x{i}, y{i}:').split(',') for i in range(3)]
            entradas.append(input('Ponto px: '))
            cond = False
        except Exception as e:
            print(e)
            continue
    return entradas

if __name__ == '__main__':
    entrada = lerEntradas()
    vetx = list()
    vety = list()
    for i in range(3):
        vetx.append(float(entrada[i][0]))
        vety.append(float(entrada[i][1]))
    tm = 2
    xp = float(entrada[3])
    yp = interpolacaoLagrange(xp, vetx, vety)

    #Janela tk
    janela = Tk()
    janela.title('Método de Lagrange')
    janela.geometry('800x430')
    janela['bg'] = 'grey'
    figura = plt.Figure(figsize=(8, 4), dpi=100)
    ax = figura.add_subplot(111)

    canva = FigureCanvasTkAgg(figura, janela)
    canva.get_tk_widget().grid(row=0, column=0)


    # Fixar estado aleatório para produção
    np.random.seed(19680801)

    # Plotando gráfico
    w = np.arange(-8, 8, 0.1)
    yw = []
    for pos in w:
        yw.append(interpolacaoLagrange(pos, vetx, vety))
    ax.plot(w, yw, 'b-')
    ax.plot(vetx, vety, 'ro')
    ax.plot(xp, yp, 'go')
    ax.set_ylabel('eixo y')
    ax.set_xlabel('eixo x')

    janela.mainloop()