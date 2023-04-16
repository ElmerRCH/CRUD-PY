import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
          self.conexion = mysql.connector.connect(
                host='localhost', 
                port= 3306,
                user='root',
                password='rootroot',
                db="escuela"
                )
        except Error as x:
            print(" salio error en la conexion pa: ",x)
    def TodasBD(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("show tables")
                resultado = cursor.fetchall()
                return resultado    
            except Error as x:
                print(" salio error en la conexion pa: ",x)
    def mostrarMaestros(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM maestros ORDER BY nombre ASC")
                resultado = cursor.fetchall()
                return resultado    
            except Error as x:
                print(" salio error en la conexion pa: ",x)
    def registrarMaestro(self,maestro):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentencia = "INSERT INTO maestros (id,nombre,apellido) VALUES ('{0}','{1}','{2}')"
                cursor.execute(sentencia.format(maestro[0],maestro[1],maestro[2]))
                self.conexion.commit()
                print("===")
                print( " curso registrado! \n")
            except Error as x:
                print(" salio error en la conexion pa: ",x)
    def eliminarMaestro(self,maestro):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentencia = "SELECT * FROM maestros WHERE id ='{0}'"
                cursor.execute(sentencia.format(maestro))
                self.conexion.commit()
                print("===")
                print( " maestro eliminado con exito! \n")
            except Error as x:
                print(" salio error en la conexion pa: ",x)

    def actualizarMaestro(self,maestro):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentencia = "UPDATE maestros SET nombre = '{0}',apellido = '{1}' WHERE id ='{2}'"
                cursor.execute(sentencia.format(maestro[1],maestro[2],maestro[0]))
                self.conexion.commit()
                print("===")
                print( " maestro actualizado! \n")
            except Error as x:
                print(" salio error en la conexion pa: ",x)