from tkinter import *
from mysql.connector import *

layout =Tk()
layout.geometry("1920x1080")
layout.title("Gestor de bases de datos")
menus=Menu(layout)
layout.config(menu=menus,bg="gray")
#------------MENUS----------------
contenedor = ["Listar registro","Registro nuevo","Actualizar registro","Eliminar registro","Listar por fecha"]
operaciones = Menu(menus,tearoff=0)
menus.add_cascade(label="operaciones",menu=operaciones)
for i in range(0,4):
  operaciones.add_command(label=contenedor[i])
consultas = Menu(menus,tearoff=0)
menus.add_cascade(label="consultas",menu=consultas)
for i in range(4,5):
  consultas.add_command(label=contenedor[i])
help = Menu(menus,tearoff=0)
menus.add_cascade(label="ayuda",menu=help)
help.add_command(label="ayuda")

layout.mainloop()