from usuario import Usuario
from carro import Carro
from paqueadero import parking

print ( " parqueadero ")
cedula = input ("ingrese su cedula :")
nombre = input ("ingrese su nombre :")
rango = input ("ingrese su rango: (admin/cliente):")
Usuario = Usuario (cedula,nombre,rango)

placa = input("ingrese la placa del carro:")
color = input ("ingrese el color del carro:")
marca = input ("ingrese la marca del carro:")
Carro = Carro (placa,color,marca)

parqueo = parking (Usuario, Carro)
parqueo.registar_entrada ("","")

opcion = input ("¿Desea registar la salida ? (si/no):")
if opcion == "si":
    
    parqueo.registrar_salida()
    parqueo.mostrar_info()
    
    
    
    
    

    