#Matias Jeronimo Vallejo Patino - 1008

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto):
        if producto.get_stock() > 0:
            producto.reducir_stock(1)
            self.items.append(producto)
            print(f"-> {producto.nombre} agregado al carrito.")
        else:
            print(f"No hay stock disponible de {producto.nombre}.")

    def remover_producto(self, nombre_producto):
        for prod in self.items:
            if prod.nombre.lower() == nombre_producto.lower():
                self.items.remove(prod)
                prod.reducir_stock(-1)
                print(f"-> {prod.nombre} eliminado del carrito.")
                return
        print("Ese producto no esta en el carrito.")

    def calcular_total(self):
        total = 0
        for prod in self.items:
            total += prod.get_precio()
        return total

    def generar_factura(self):
        if not self.items:
            print("El carrito esta vacio.")
            return
        print("\n=== FACTURA DE COMPRA ===")
        for prod in self.items:
            print(f"- {prod.nombre}: ${prod.get_precio()}")
        print("-------------------------")
        print(f"TOTAL: ${self.calcular_total()}")
        print("=========================")