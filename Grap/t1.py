from tkinter import *
from click import command
import socket   
import threading


def broadcast(message, _client,clients):
    for client in clients:
        if client != _client:
            client.send(message)

def handle_messages(client,clients,usernames):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            username = usernames[index]
            #broadcast(f"ChatBot: {username} disconnected".encode('utf-8'), client)
            clients.remove(client)
            usernames.remove(username) 
            client.close()
            break

def receive_connections():
        host = '127.0.0.1'
        port = 55555
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        #print(f"Server running on {host}:{port}")
        clients = []
        usernames = []
       

        while True:
            client, address = server.accept()

            client.send("username".encode("utf-8"))
            username = client.recv(1024).decode('utf-8')

            clients.append(client)
            usernames.append(username)

            #print(f"{username} esta conectado con {str(address)}")

            message = f"Botsito: {username} entro al chat : ".encode("utf-8")
            broadcast(message, client)
            client.send("Te conectaste al servidor ".encode("utf-8"))

            thread = threading.Thread(target=handle_messages, args=(client,))
            thread.start()

raiz =Tk()
raiz.title(" Whatsapp chipeado ")
#raiz.resizable(1920,1080)
#raiz.iconbitmap(fernandogod.ico)
raiz.geometry("1920x1080")
raiz.config(bg="gray")

nombre = StringVar()
#nombre1 = StringVar()

imagen = PhotoImage(file ="fernandito.png" )

label2 = Label(raiz , image = imagen)
label2.config(width = "300", height = "250")
label2.pack()
label2.place(x = 50 , y = 0)


label = Label(raiz, text = "Whatssap chipeado",fg = "black",font =("arial",30),bg ="gray")
label.pack()
label.place(x = 50 , y = 250)

def holaMundo(host,port):
    nombre.set(f"Server running on {host}:{port}")
    receive_connections()

BotonInicarServdior = Button(raiz, text = " Iniciar Servidor ",bg = "green",font =("arial",15), command = holaMundo)
BotonInicarServdior.pack()
BotonInicarServdior.place(x = 1250 , y = 500)
BotonInicarServdior.config(width = "30", height = "15")
#=============================miframe
miframe = Frame()
miframe.pack()
miframe.config(bg = "purple")
miframe.config(width = "700", height = "500")
miframe.config(bd = 35)
miframe.config(relief = "sunken")
miframe.config(cursor = "pirate")
miframe.place(x = 50 , y = 300)

textoGrande = Label(miframe , textvariable = nombre)
textoGrande.config(width = "70", height = "35",bg ="gray")
textoGrande.pack()
raiz.mainloop()
