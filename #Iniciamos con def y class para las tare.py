class Restaurant:
    def __init__(self):
        self.menu = {
            "Hamburguesa": 80,
            "Hot Dog": 60,
            "Pizza": 120,
            "Refresco": 30,
            "Café": 40,
            "Ensalada": 70,
            "Sándwich": 50,
            "Tacos": 90,
            "Pastel": 45
        }
        self.mesas_apartadas = {}
        self.ordenes = []
        self.pagos = []

    def ver_menu(self):
        print("Menú disponible:")
        for item, precio in self.menu.items():
            print(f"{item}: ${precio:.2f}")

    def agregar_nuevo_item(self):
        item = input("Ingrese el nombre del nuevo producto: ").capitalize()
        if item in self.menu:
            print("Este producto ya existe en el menú.")
        else:
            precio = float(input("Ingrese el precio del nuevo producto: "))
            self.menu[item] = precio
            print(f"{item} ha sido añadido al menú con un precio de ${precio:.2f}.")

    def agregar_pedido(self, numero_mesa):
        total_pedido = 0
        while True:
            self.ver_menu()
            item = input("Seleccione un producto (o 'finalizar' para terminar): ").capitalize()
            if item == 'Finalizar':
                break
            if item in self.menu:
                cantidad = int(input(f"¿Cuántos {item} desea? "))
                total_item = self.menu[item] * cantidad
                total_pedido += total_item
                self.ordenes.append({"mesa": numero_mesa, "producto": item, "cantidad": cantidad, "total_item": total_item})
            else:
                print("Producto no disponible.")
        print(f"Total a pagar para la mesa {numero_mesa}: ${total_pedido:.2f}")
        return total_pedido

    def reserva_mesas(self, numero, nombre_cliente):
        if numero not in self.mesas_apartadas:
            self.mesas_apartadas[numero] = nombre_cliente
        else:
            print(f"Lo siento, la mesa {numero} ya está reservada.")

    def ver_mesas_reservadas(self):
        if self.mesas_apartadas:
            print("Mesas reservadas:")
            for numero, cliente in self.mesas_apartadas.items():
                print(f"Mesa {numero}: reservada por {cliente}")
        else:
            print("No hay mesas reservadas.")

    def ver_cola_pedidos(self):
        print("Cola de pedidos:")
        for idx, orden in enumerate(self.ordenes):
            print(f"{idx+1}. Mesa {orden['mesa']}: {orden['producto']} x{orden['cantidad']} (Total: ${orden['total_item']:.2f})")

    def procesar_pago(self, numero_mesa):
        total_pedido = sum(orden['total_item'] for orden in self.ordenes if orden['mesa'] == numero_mesa)
        if total_pedido > 0:
            metodo_pago = input("Seleccione el método de pago ('tarjeta' o 'efectivo'): ").lower()
            if metodo_pago in ["tarjeta", "efectivo"]:
                self.pagos.append({"mesa": numero_mesa, "monto": total_pedido, "metodo": metodo_pago})
                print(f"Pago procesado para la mesa {numero_mesa} por ${total_pedido:.2f} con {metodo_pago}.")
            else:
                print("Método de pago no válido. Intente de nuevo.")
        else:
            print(f"No hay pedidos pendientes para la mesa {numero_mesa}.")

    def menu_principal(self):
        while True:
            print("\n--- Menú del Sistema ---")
            print("1. Ver Menú")
            print("2. Agregar Nuevo Producto al Menú")
            print("3. Reservar Mesa")
            print("4. Ver Mesas Reservadas")
            print("5. Agregar Pedido")
            print("6. Ver Cola de Pedidos")
            print("7. Procesar Pago")
            print("8. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ver_menu()
            elif opcion == "2":
                self.agregar_nuevo_item()
            elif opcion == "3":
                numero = int(input("Ingrese el número de la mesa: "))
                nombre_cliente = input("Ingrese el nombre del cliente: ")
                self.reserva_mesas(numero, nombre_cliente)
            elif opcion == "4":
                self.ver_mesas_reservadas()
            elif opcion == "5":
                numero_mesa = int(input("Ingrese el número de la mesa: "))
                self.agregar_pedido(numero_mesa)
            elif opcion == "6":
                self.ver_cola_pedidos()
            elif opcion == "7":
                numero_mesa = int(input("Ingrese el número de la mesa: "))
                self.procesar_pago(numero_mesa)
            elif opcion == "8":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

# Ejemplo de uso
restaurante = Restaurant()
restaurante.menu_principal()
