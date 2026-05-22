from clases.producto import Producto
from clases.usuario import Cliente
from clases.carrito import Carrito

#Matias Jeronimo Vallejo Patino - 1008

def menu():
    user_cliente = Cliente("Jero", "jero@colegio.edu.co")
    carrito = Carrito()
    
    inventario = [
        Producto("Mouse Gamer", 85000, 10),
        Producto("Teclado Mecanico", 150000, 5),
        Producto("Audifonos HyperX", 220000, 4)
    ]

    while True:
        print("\n=== MENU TIENDA VIRTUAL ===")
        print(f"Usuario: {user_cliente.nombre} | Rol: {user_cliente.tipo}")
        print("1. Ver catalogo de productos")
        print("2. Agregar producto al carrito")
        print("3. Quitar producto del carrito")
        print("4. Ver total y pagar (Factura)")
        print("5. Salir")
        
        opc = input("Seleccione una opcion (1-5): ")

        if opc == "1":
            print("\n--- CATALOGO DE PRODUCTOS ---")
            for i, prod in enumerate(inventario, 1):
                print(f"{i}. {prod.mostrar_info()}")
            
        elif opc == "2":
            print("\n--- AGREGAR AL CARRITO ---")
            for i, prod in enumerate(inventario, 1):
                print(f"{i}. {prod.nombre} (${prod.get_precio()})")
            
            try:
                idx = int(input("Ingrese el numero del producto: ")) - 1
                if 0 <= idx < len(inventario):
                    carrito.agregar_producto(inventario[idx])
                else:
                    print("Numero invalido.")
            except ValueError:
                print("Escriba un numero valido.")
                
        elif opc == "3":
            print("\n--- QUITAR DEL CARRITO ---")
            if not carrito.items:
                print("El carrito esta vacio.")
            else:
                nombre_quitar = input("Nombre del producto a quitar: ")
                carrito.remover_producto(nombre_quitar)
                
        elif opc == "4":
            carrito.generar_factura()
            if carrito.items:
                print("\nCompra finalizada con exito.")
                break
            
        elif opc == "5":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    menu()