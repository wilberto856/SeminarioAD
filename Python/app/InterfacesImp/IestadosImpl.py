

from service.Iestados import IEstado
from Connection.connection import get_connection


class IEstadoImpl(IEstado):
    
    def guardarEstado(self, data):
        
        nombreEstado = data.get('estado')      
        conexion = get_connection()

        try:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO estado (estado) VALUES ("'+nombreEstado+'")'
                cursor.execute(sql)
                conexion.commit()
                ultima = cursor.lastrowid
                conexion.close()    
            return ultima
        except:
            raise


    def getEstados(self):
        
        conexion = get_connection()
        lEstados = []

        try:
            with conexion.cursor() as cursor:
                sql = 'SELECT  * FROM Estado'
                cursor.execute(sql)
                estados = cursor.fetchall()
                for row in estados:                   
                    ne = {'id':row[0], 'estado': row[1]}
                    lEstados.append(ne)
                conexion.close()
            return lEstados
        except:
            raise
        
