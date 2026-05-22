#Matias Jeronimo Vallejo Patino - 1008

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def mostrar_info(self):
        return f"{self.nombre} - Precio: ${self.__precio} | Stock: {self.__stock}"

    def reducir_stock(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        return False