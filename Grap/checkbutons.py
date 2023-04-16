from tkinter import *
lista = ["mexico","chiapas","canada","newyork"]
pantalla = Tk()
img=PhotoImage(file="fernandito.png")
label1 = Label(pantalla,image=img).pack()
for i in range (0,4):
 Checkbutton(pantalla,text=lista[i]).pack()#onvalue y off value en vez de value     




pantalla.mainloop()