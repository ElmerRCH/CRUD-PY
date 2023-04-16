from tkinter import *

pantalla = Tk()
barra=Menu(pantalla)
pantalla.config(menu=barra,width="500", height="500")
contenedor = ["tamales","gorditas","enchiladas","platos","cucharas","tenedores"]
Archivom = Menu(barra,tearoff=0)
for i in range(0,3):
 Archivom.add_command(label=contenedor[i])

#Archivom.add_separator()

cosas = Menu(barra)
for i in range(3,6):
 cosas.add_command(label=contenedor[i])

help = Menu(barra)
help.add_command(label="llegar temprano")
help.add_command(label="mada")



barra.add_cascade(label="menu",menu=Archivom)
barra.add_cascade(label="cosas",menu=cosas)
barra.add_cascade(label="help",menu=help)
pantalla.mainloop()