from cProfile import label
from tkinter import *

from setuptools import Command
janela = Tk()
rotulo =Label(janela, text='Olá, mundo')
rotulo.grid(row=0, column=0)
rotulo["font"] = ("Arial", "18", "bold", "italic")
rotulo["fg"] = "red"
rotulo["bg"] = "yellow"
pergunta = Label(janela, text="Tudo bem?")
pergunta.grid(row=1, column=0)


'''Label(janela, text="Olá, mundo!").grid(row=0, column=0)
Label(janela, text="||| Tudo bem?").grid(row=0, column=1)
'''
boton_1 = Button(janela)
boton_1.grid(row=2, column=2)
boton_1["text"] = "SAIR"
boton_1["width"] = 30
boton_1['fg'] = "blue"
boton_1['bg'] = 'black'
boton_1["command"] = quit
janela.mainloop()
