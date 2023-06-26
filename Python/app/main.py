from flask import Flask, jsonify, request
from flask_cors import CORS


from  InterfacesImp.IclientesImpl import IclientesImpl
from  InterfacesImp.IrolesImpl import IRolImpl
from  InterfacesImp.IestadosImpl import IEstadoImpl
from  InterfacesImp.IusuariosImp import IUsuarioImpl
from  InterfacesImp.IvisitasImp import IVisitasImpl

app = Flask(__name__)
CORS(app)

iclientesService = IclientesImpl()
irolesService = IRolImpl()
iestadoService = IEstadoImpl()
iusuarioService = IUsuarioImpl()
iVisitaService = IVisitasImpl()


@app.route("/cliente", methods=['GET', 'POST'])
def Clientes():
    if request.method=='GET':
        clientes = [] 
        clientes = iclientesService.obtenerclientes()
        return jsonify(clientes)
    else:
        data = request.json
        nuevoClientes = iclientesService.guardarCliente(data)  
        return str(nuevoClientes)


@app.route("/rol", methods=['GET', 'POST'])
def Roles():
    if request.method=='GET':
        Rol = [] 
        Rol = irolesService.getRoles()
        return jsonify(Rol)
    else:
        data = request.json
        nuevoRol = irolesService.guardarRol(data)  
        return str(nuevoRol)


@app.route("/estado", methods=['GET', 'POST'])
def Estados():
    if request.method=='GET':
        Estados = [] 
        Estados = iestadoService.getEstados()
        return jsonify(Estados)
    else:
        data = request.json
        nuevoEstado = iestadoService.guardarEstado(data)  
        return str(nuevoEstado)
    

@app.route("/usuario", methods=['GET', 'POST'])
def Usuarios():
    if request.method=='GET':
        Usuarios = [] 
        Usuarios = iusuarioService.getUsuario()
        return jsonify(Usuarios)
    else:
        data = request.json
        nuevoUsuario = iusuarioService.guardarUsuario(data)  
        return str(nuevoUsuario)
    

@app.route("/visitas", methods=['GET', 'POST'])
def Visitas():
    if request.method=='GET':
        Visitas = [] 
        Visitas = iVisitaService.getVisita()
        return jsonify(Visitas)
    else:
        data = request.json
        nuevaVisita = iVisitaService.guardarVisita(data)  
        return str(nuevaVisita)
    
@app.route("/detallevisita/<menu>", methods=['GET', 'POST'])
def detalleVisita(menu):
    if request.method=='GET':
        visita = ""
        visita = iVisitaService.getDetalleVisita(menu)
        return jsonify(visita)
    else:
        data = request.json
        nuevaVisita = iVisitaService.guardarVisita(data)  
        return str(nuevaVisita)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4201, debug=True)