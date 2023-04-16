from tkinter import *

pantalla = Tk()
pantalla.config(bg='black')
pantalla.title("calculadora")
pantalla.geometry('300x400')
#pantalla.resizable(0,12)

frame1= Frame()
frame1.pack()
frame1.config(bg='#5d524d')
#frame1.config(relief = "sunken")
frame1.place(x =52 ,y = 50)
frame1.config(width = "200", height = "300")
operacion = ""
resultado = 0
contador = 0

#================PANTALLA
np = StringVar()

texto = Entry(pantalla,bg = '#7500f2',textvariable=np,width = "31",justify = 'right')
texto.pack()
texto.place(x = 57,y = 100)
#texto.config(width = "26", height = "2")

#================funciones

def pulsaciones(num):
    global operacion
    global resultado
    global contador
    if operacion !="":
        np.set(num)
        operacion = ""
    else:
        np.set(np.get()+num)

def suma(num):
    global operacion
    global resultado
    global contador
    if contador == 0:
        contador = int(num)
        operacion = "suma"
    else:
        resultado = contador + int(num)
        operacion = "suma" 
        contador = 0
        np.set(resultado)
def resta(num): 
    global operacion
    global resultado
    global contador
    if contador == 0:
        contador = int(num)
        operacion = "resta"
    else:
        resultado = contador - int(num)
        operacion = "resta" 
        contador = 0
        np.set(resultado)
def multiplicacion(num):
    global operacion
    global resultado
    global contador
    if contador == 0:
        contador = int(num)
        operacion = "multiplicacion"
    else:
        resultado = contador * int(num)
        operacion = "multiplicacion" 
        contador = 0
        np.set(resultado)
def division(num):
    global operacion
    global resultado
    global contador
    if contador == 0:
        contador = int(num)
        operacion = "division"
    else:
        resultado = contador / int(num)
        operacion = "division" 
        contador = 0
        np.set(resultado)
def resultado1():
    global resultado
    np.set(resultado +int(np.get()))
    resultado = 0
"""
def resultado2():
    global resultado
    np.set(resultado *int(np.get()))
    resultado = 0
def resultado3():
    global resultado
    np.set(resultado -int(np.get()))
    resultado = 0
def resultado4():
    global resultado
    np.set(resultado /int(np.get()))
    resultado = 0
"""
#================BOTONES 7,8,9,X
boton7 = Button(pantalla,text = '7',bg = '#f20033',command =lambda:pulsaciones("7"))
boton7.pack()
boton7.place(x = 55,y = 150)
boton7.config(width = "4", height = "2")

boton8 = Button(pantalla,text = '8',bg = '#f20033',command =lambda:pulsaciones("8"))
boton8.pack()
boton8.place(x = 105,y = 150)
boton8.config(width = "4", height = "2")

boton9 = Button(pantalla,text = '9',bg = '#f20033',command =lambda:pulsaciones("9"))
boton9.pack()
boton9.place(x = 155,y = 150)
boton9.config(width = "4", height = "2")

botonx = Button(pantalla,text = 'x',bg = '#00f29f',command =lambda:multiplicacion(np.get()))
botonx.pack()
botonx.place(x = 205,y = 150)
botonx.config(width = "4", height = "2")
#================BOTONES 4,5,6,-
boton4 = Button(pantalla,text = '4',bg = '#f20033',command =lambda:pulsaciones("4"))
boton4.pack()
boton4.place(x = 55,y = 200)
boton4.config(width = "4", height = "2")

boton5 = Button(pantalla,text = '5',bg = '#f20033',command =lambda:pulsaciones("5"))
boton5.pack()
boton5.place(x = 105,y = 200)
boton5.config(width = "4", height = "2")

boton6 = Button(pantalla,text = '6',bg = '#f20033',command =lambda:pulsaciones("6"))
boton6.pack()
boton6.place(x = 155,y = 200)
boton6.config(width = "4", height = "2")

botonm = Button(pantalla,text = '-',bg = '#00f29f',command=lambda:resta(np.get()))
botonm.pack()
botonm.place(x = 205,y = 200)
botonm.config(width = "4", height = "2")
#================BOTONES 1,2,3,+
boton1 = Button(pantalla,text = '1',bg = '#f20033',command =lambda:pulsaciones("1"))
boton1.pack()
boton1.place(x = 55,y = 250)
boton1.config(width = "4", height = "2")

boton2 = Button(pantalla,text = '2',bg = '#f20033',command =lambda:pulsaciones("2"))
boton2.pack()
boton2.place(x = 105,y = 250)
boton2.config(width = "4", height = "2")

boton3 = Button(pantalla,text = '3',bg = '#f20033',command =lambda:pulsaciones("3"))
boton3.pack()
boton3.place(x = 155,y = 250)
boton3.config(width = "4", height = "2")

botonmas = Button(pantalla,text = '+',bg = '#00f29f',command =lambda:suma(np.get()))
botonmas.pack()
botonmas.place(x = 205,y = 250)
botonmas.config(width = "4", height = "2")
#================BOTONES /,0,.,=
botondiv = Button(pantalla,text = '/',bg = '#00f29f',command=lambda:division(np.get()))
botondiv.pack()
botondiv.place(x = 55,y = 300)
botondiv.config(width = "4", height = "2")

boton0 = Button(pantalla,text = '0',bg = '#f20033',command =lambda:pulsaciones("0"))
boton0.pack()
boton0.place(x = 105,y = 300)
boton0.config(width = "4", height = "2")

botonpu = Button(pantalla,text = '.',bg = '#00f29f',command =lambda:pulsaciones("."))
botonpu.pack()
botonpu.place(x = 155,y = 300)
botonpu.config(width = "4", height = "2")

botoni = Button(pantalla,text = '=',bg = '#00f29f',command =lambda:resultado1())
botoni.pack()
botoni.place(x = 205,y = 300)
botoni.config(width = "4", height = "2")
pantalla.mainloop()
