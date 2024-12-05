## Funciones 
import socket, threading, sys

## conexion server - cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    CLIENT_IP, PORT = "localhost", 8000
    s.connect((CLIENT_IP, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)


## registrar usuario
class Clientes:

    def __init__(self):
        self.db = []
        self.BANNED_NICKS = ["admin", "moderator", "system", "root"]

    def registrar_cliente(self, nombre : str):

        validar_nombre = lambda x: x in self.BANNED_NICKS
        nombre_existe = lambda x: x in self.db

        if validar_nombre(x=nombre.lower()):
            return {"message": f" '{nombre}', No esta permitido"}, 404
        
        if nombre_existe(x=nombre.lower()):
            return {"message": f" '{nombre}', Ya existe"}, 404
        
        new_cliente = {'id': len(self.db) + 1,
                       "cliente": nombre.lower()}

        self.db.append(new_cliente)
        return {"message": f"{nombre} registrado exitosamente"}, 200



    ## envio de mensaje



## recepcion de mensajes


## cierrar la conexion

if __name__ == "__main__":
    clientes = Clientes()
    nombre = str(input("Ingrese tu nombre: "))
    resultado, codigo = clientes.registrar_cliente(nombre)
    print(resultado)
