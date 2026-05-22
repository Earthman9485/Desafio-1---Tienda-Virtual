#Matias Jeronimo Vallejo Patino - 1008

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

class Cliente(Usuario):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.tipo = "Cliente"

class Administrador(Usuario):
    def __init__(self, nombre, correo):
        super().__init__(nombre, correo)
        self.tipo = "Administrador"