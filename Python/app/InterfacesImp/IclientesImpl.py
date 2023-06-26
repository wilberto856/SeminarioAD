

from service.Iclientes import ICliente
from Connection.connection import get_connection
from Entities.clientes import Cliente

class IclientesImpl(ICliente):
    
    def guardarCliente(self, data):
        
        nombre = data.get('nombre')
        direccion = data.get('direccion')
        latitud = data.get('latitud')
        longitud = data.get('longitud')
        email = data.get('email')
        
        conexion = get_connection()

        try:
            with conexion.cursor() as cursor:
                sql = 'INSERT INTO Cliente (nombre, direccion, latitud, longitud, email) VALUES \
                    ("'+nombre+'", "'+direccion+'", "'+latitud+'", "'+longitud+'","'+email+'")'
                cursor.execute(sql)
                conexion.commit()
                ultima = cursor.lastrowid
                conexion.close()
                
            return ultima
        except:
            raise


    def obtenerclientes(self):
        
        conexion = get_connection()
        lClientes = []

        try:
            with conexion.cursor() as cursor:
                sql = 'SELECT  * FROM Cliente'
                cursor.execute(sql)
                clientes = cursor.fetchall()
                for row in clientes:                   
                    nc = {'id':row[0], 'nombre': row[1], 'direccion': row[2], 'latitud': row[3], 'longitud': row[4], 'email': row[5]}
                    lClientes.append(nc)
                conexion.close()
            return lClientes
        except:
            raise
        
    def buscarcliente(self):
        pass
