def listarMaestro(maestros1):
    print ("maestros")
    con = 1
    for i in maestros1:
        datos = "{0}. id: {1} - nombre: {2} - apellido: {3}"
        print(datos.format(con,i[0],i[1],i[2]))
        con = con + 1
    print("")
def listarbases(bases):
    print ("bases")
    con = 1
    for i in bases:
        datos = "{0}. nombre: {1}"
        print(datos.format(con,i[0]))
        con = con + 1
    print("")    
def pedirMaestros():
    id = int(input("Escriba un nuevo id: "))
    nombre = input(" Nuevo nombre: ")
    apellido = input(" Nuevo apellido: ")
    maestro = (id,nombre,apellido)
    return maestro

def eliminar(maestro):
    listarMaestro(maestro)
    existeid = False
    id = int(input("ID de maestro a eliminar: "))
    for i in maestro:
        if i[0] == id:
            existeid = True
            break
    if not existeid:
        id = " "
    return id
def actualizarMaestros(maestros):
    listarMaestro(maestros)
    existeid = False
    id = int(input("ID de maestro a editar: "))
    for i in maestros:
        if i[0] == id:
            existeid = True
            break
    if existeid:
        nombre = input(" Nuevo nombre: ")
        apellido = input(" Nuevo apellido: ")
        maestros = (id,nombre,apellido)
    else: 
        maestros = None
    return maestros
    
