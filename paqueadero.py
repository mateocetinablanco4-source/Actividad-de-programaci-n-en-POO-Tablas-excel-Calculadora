class parqueadero:
  def __init__(self,usuario,carro):
    self.usuario = usuario
    self.carro = carro
    self.hora_entrada = ""
    self.hora_salida = ""
    self.estado=""
    
    def registrar_entrada(self):
        self.fecha_entrada=input("ingrese la fecha de entrada (DD=MM=AAAA):")
        self.hora_entrada=input("ingrese la hora de entrada(HH:MM):")
        self.estado="ADENTRO"
        print("entrada registrada correctamente.")
        
        def regitrar_salida(self):
            self.hora_salida=input("ingrese la hora de salia(HH:MM)")
            self.estado="SALIO"
            print("salida registrada correctamente.")
            
            def imprimir_datos(self):
                print("fecha de entrada:",self.fecha_entrada)
                print("hora de entrada:",self.hora_entrada)
                print("hora de salida:",self.hora_salida)
                print("estado:",self.estado)