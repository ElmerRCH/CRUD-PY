from tkinter import *
from venv import main
layout=Tk()

def imprimir(): 
    cont = []
    if opcion.get()==1:
            cont ="Elmer"
    elif opcion.get()==2:
            cont += " Rene"
            
    elif opcion.get()==3:
            cont += " Camacho"
    elif opcion.get()==4:
            cont += " Higuera"
    eti.config(text=cont)
    
opcion = IntVar()
Radiobutton(layout,text="Primer nombre",variable=opcion,value=1,command=imprimir).pack()
Radiobutton(layout,text="segundo nombre",variable=opcion,value=2,command=imprimir).pack()
Radiobutton(layout,text="apellido",variable=opcion,value=3,command=imprimir).pack()
Radiobutton(layout,text="segundo apellido",variable=opcion,value=4,command=imprimir).pack()



eti=Label(layout,bg="gray")
eti.pack()
eti.config(width = "200", height = "300")
layout.mainloop()