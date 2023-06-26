

from service.Ivisitas import Ivisita
from Connection.connection import get_connection


class IVisitasImpl(Ivisita):
    
    def guardarVisita(self, data):
        
        Idcliente = data.get('idcliente') 
        idEstado = data.get('idEstado')  
                      
        conexion = get_connection()
        try:
            with conexion.cursor() as cursor:             
                sql = 'INSERT INTO Visita (idcliente, IdEstado) VALUES ("'+Idcliente+'","'+idEstado+'")'                      
                cursor.execute(sql)
                conexion.commit()
                ultima = cursor.lastrowid
                conexion.close()    
            return ultima
        except:
            raise


    def getVisita(self):
        
        conexion = get_connection()
        lVisitas = []

        try:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM Visitas'
                cursor.execute(sql)
                vistas = cursor.fetchall()
                for row in vistas:                   
                    nv = {'id':row[0], 'cliente': row[1], 'latitudCliente': row[2], 'longitudCliente': row[3], 'estado': row[4], 'tecnico': row[5],'latitudVisitada': row[6],'longitud': row[7], 'descripcion': row[8]}
                    lVisitas.append(nv)
                conexion.close()
            return lVisitas
        except:
            raise
        
    def getDetalleVisita(self, id):
            
        conexion = get_connection()
        dVisita=""

        try:
            with conexion.cursor() as cursor:
                sql = 'SELECT * FROM Visitas WHERE idvisita ='+id+'' 
                cursor.execute(sql)
                dVisita = cursor.fetchall()   
                for row in dVisita:           
                    nv = {'id':row[0], 'cliente': row[1], 'latitudCliente': row[2], 'longitudCliente': row[3], 'estado': row[4], 'tecnico': row[5],'latitudVisitada': row[6],'longitud': row[7], 'descripcion': row[8]}
                    conexion.close()
            return nv      
        except:
            raise


        