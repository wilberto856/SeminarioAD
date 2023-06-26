

from service.Iroles import IRol
from Connection.connection import get_connection


class IRolImpl(IRol):
    
    def guardarRol(self, data):
        
        nombreRol = data.get('rol')      
        conexion = get_connection()

        try:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO rol (nombreRol) VALUES ("'+nombreRol+'")'
                cursor.execute(sql)
                conexion.commit()
                ultima = cursor.lastrowid
                conexion.close()    
            return ultima
        except:
            raise


    def getRoles(self):
        
        conexion = get_connection()
        lRoles = []

        try:
            with conexion.cursor() as cursor:
                sql = 'SELECT  * FROM Rol'
                cursor.execute(sql)
                roles = cursor.fetchall()
                for row in roles:                   
                    nc = {'id':row[0], 'nombreRol': row[1]}
                    lRoles.append(nc)
                conexion.close()
            return lRoles
        except:
            raise
        
