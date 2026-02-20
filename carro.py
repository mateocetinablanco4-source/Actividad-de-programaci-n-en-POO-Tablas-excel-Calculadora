class Carro:
    def __init__(self, placa,marca,color):
        self.placa=placa
        self.color=color
        self.marca=marca
        
    def get_placa (self):
        return  self.placa
    
    def  set_dato_placa ( self,dato_placa):
        self.placa = dato_placa
        
    def get_color (self):
        return self.color
    
    def set_dato_color (self,dato_color):
        self.color = dato_color
        
    def get_marca (self):
        return self.marca
    
    def get_dato_marca (self, dato_marca):
        self.marca = dato_marca
        
        
    def imprimir_datos (self):
        print(f"placa: {self.placa}")
        print(f"color:{self.color}")
        print(f"marca:{self.marca}")
        
        
        
        
        

        