

from service.Iusuarios import IUsuario
from Connection.connection import get_connection


class IUsuarioImpl(IUsuario):
    
    def guardarUsuario(self, data):
        
        nombre = data.get('nombre') 
        apellido = data.get('apellido')  
        password = data.get('password')  
        idRol = data.get('idRol')  
        idSupervisor = data.get('idSupervisor')  
             
        conexion = get_connection()

        try:
            with conexion.cursor() as cursor:
                
                
                if idSupervisor == 0:
                    sql = 'INSERT INTO Usuario (Nombre, Apellido, Password, idRol, idSupervisor) VALUES \
                    ("'+nombre+'","'+apellido+'","'+password+'","'+idRol+'")'
                    
                sql = 'INSERT INTO Usuario (Nombre, Apellido, Password, idRol, idSupervisor) VALUES \
                ("'+nombre+'","'+apellido+'","'+password+'","'+idRol+'","'+idSupervisor+'")'

                
                    
                cursor.execute(sql)
                conexion.commit()
                ultima = cursor.lastrowid
                conexion.close()    
            return ultima
        except:
            raise


    def getUsuario(self):
        
        conexion = get_connection()
        lUsuarios = []

        try:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM Usuario'
                cursor.execute(sql)
                usuarios = cursor.fetchall()
                for row in usuarios:                   
                    nu = {'id':row[0], 'nombre': row[1], 'apellido': row[2], 'password': row[3], 'idRol': row[4], 'idSupervisor': row[5]}
                    lUsuarios.append(nu)
                conexion.close()
            return lUsuarios
        except:
            raise


        
