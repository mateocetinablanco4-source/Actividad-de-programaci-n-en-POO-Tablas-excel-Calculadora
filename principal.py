from usuario import Usuario
from carro import Carro
from paqueadero import parqueadero

print (" PARQUEADERO ")
 
cedula = input ("ingrese su numero de cedula: ")
nombre = input ("ingrese nombre :")
rango = input ("ingrese su rango :(admin/cliente):")
Usuario = Usuario (cedula,nombre,rango)

placa = input ("ingrese la placa del carro:")
color = input ("ingrese el color del carro:")
marca = input ("ingrese marca del carro: ")
carro = Carro (placa,color,marca)

parqueadero = parqueadero (Usuario, carro)
parqueadero.registrar_entrada ("","")


opcion = input ("¿desea registrar la salida? (si/no): ")
if opcion == "si":
    parqueadero.registrar_salida()
    parqueadero.mostrar_informacion
    
    