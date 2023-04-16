
def listarClientes(cliente):
    print ("Clientes")
    con = 1
    for i in cliente:
        datos = "{0}. id: {1} - nombre: {2} - apellido: {3}"
        print(datos.format(con,i[0],i[1],i[2]))
        con = con + 1
    print("")
def pedirCliente():
    id = int(input("Escriba un nuevo id: "))
    nombre = input(" Nuevo nombre: ")
    apellido = input(" Nuevo apellido: ")
    gmail = input(" Nuevo gmail: ")
    contraseña = input(" Contraseña: ")
    cliente = (id,nombre,apellido,gmail,contraseña)
    return cliente

def eliminar(cliente):
    listarClientes(cliente)
    existeid = False
    id = int(input("ID de cliente a eliminar: "))
    for i in cliente:
        if i[0] == id:
            existeid = True
            break
    if not existeid:
        id = " "
    return id
def actualizarCliente(cliente):
    listarClientes(cliente)
    existeid = False
    id = int(input("ID de cliente a editar: "))
    for i in cliente:
        if i[0] == id:
            existeid = True
            break
    if existeid:
        nombre = input(" Nuevo nombre: ")
        apellido = input(" Nuevo apellido: ")
        gmail = input(" Nuevo gmail: ")
        contraseña = input(" Contraseña: ")
        cliente = (id,nombre,apellido,gmail,contraseña)
    else: 
        cliente = None
    return cliente
    
