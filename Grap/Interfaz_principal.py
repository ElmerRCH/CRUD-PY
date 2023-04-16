from tkinter import *
from mysql.connector import *
from conexion import DAO
import funciones

layout =Tk()
layout.geometry("1920x1080")
layout.title("Bases de datos")
layout.config(bg="gray")
#----------------------------------
Texto_p=Label(layout,text="--------------base de datos--------------")
Texto_p.pack()
Texto_p.config(width = "100", height = "5",bg="green",font="arial 20",justify="center")
Texto_p.place(x =0 ,y =0)


dao = DAO()
bases = dao.TodasBD()
funciones.listarbases(bases)
#-----------------------------------

layout.mainloop()