from BD.conexion import DAO
import funciones
#============================== se define el metodo menu para generar opciones
def menu():
    continuar = True # mientras continuar sea true while funcionara
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):# opcionCorrecta es false pero [NOT] invierte las cosas bro
            print("====== Menu Principal ======")
            print(" 1 - Listar clientes ")
            print(" 2 - Registrar clientes ")
            print(" 3 - Actualizar clientes ")
            print(" 4 - Eliminar cliente ")
            print(" 5 - Salir ")
            print("=============================")
            opcion = int(input("seleccione una opcion: "))
            if opcion < 1 or opcion >5:# para evitar usar varios elif se limito
                print(" Opcion Incorrecta, intente nuevamente ")
            elif opcion == 5:
                continuar = False # si la opcion es igual a 5 entonces continuar sera false y el menu termina
                print(" Gracias por usar este programa ")
                break # brear rompe ciclos
            else :
                opcionCorrecta = True # se usa para repetir el menu
                ejecutarOpcion(opcion)
def ejecutarOpcion(opcion):
    dao = DAO()
#================================= opcion 1
    if opcion == 1:
        try:
            cliente = dao.mostraClientes()
            if len(cliente)>0:
                funciones.listarClientes(cliente)
            else: 
                print("no se encontro nada")
        except: 
            print("ocurrio un error")
#================================== opcion 2
    elif opcion == 2:
        cliente = funciones.pedirCliente()
        try:
            dao.registrarCliente(cliente)
        except: 
            print("ocurrio un error")
#================================== opcion 3
    elif opcion == 3:
        try:
            cliente = dao.mostrarCliente()
            if len(cliente)>0:
               cliente = funciones.actualizarMaestros(cliente)
               if cliente:
                   dao.actualizarMaestro(cliente)     
            else: 
                print("no se encontro nada")
        except: 
            print("ocurrio un error")
        
#================================== opcion 4
    elif opcion == 4:
        try:
            cliente = dao.mostrarClientes()
            if len(cliente)>0:
                eliminar = funciones.eliminar(cliente)
                if not(eliminar == " "):  
                    dao.eliminarMaestro(eliminar)
                else: 
                        print(" codigo de curso no encontrado ")
            else: 
                print("no se encontro nada")
        except: 
            print("ocurrio un error en eliminar ")   
menu()
