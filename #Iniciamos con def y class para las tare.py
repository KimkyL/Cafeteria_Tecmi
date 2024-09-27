from datetime import datetime  # Importa la clase datetime del módulo datetime para manejar fechas.

class Restaurant:
    def __init__(self):
        # Inicializa el menú del restaurante con algunos productos y sus precios.
        self.menu = {
            "Hamburguesa": 80,
            "Hot Dog": 60,
            "Pizza": 120,
            "Refresco": 30,
            "Cafe": 40,
            "Ensalada": 70,
            "Sandwich": 50,
            "Tacos": 90,
            "Pastel": 45
        }
        # Inicializa las mesas reservadas, órdenes, pagos y promociones.
        self.mesas_apartadas = {}
        self.ordenes = []
        self.pagos = []
        self.promociones = []
    
    def ver_menu(self):
        # Muestra el menú disponible con sus precios.
        print("Menu disponible:")
        for item, precio in self.menu.items():
            print(f"{item}: ${precio:.2f}")

    def agregar_nuevo_item(self):
        # Permite al usuario agregar un nuevo producto al menú.
        item = input("Ingrese el nombre del nuevo producto: ").capitalize()
        if item in self.menu:
            print("Este producto ya existe en el menu.")
        else:
            precio = float(input("Ingrese el precio del nuevo producto: "))
            self.menu[item] = precio
            print(f"{item} ha sido anadido al menu con un precio de ${precio:.2f}.")

    def agregar_promocion(self):
        # Permite al usuario agregar una nueva promoción al sistema.
        nombre = input("Ingrese el nombre de la promocion: ").capitalize()
        tipo_promocion = input("Seleccione el tipo de promocion ('descuento', '2x1', 'regalo'): ").lower()
        
        # Obtiene el descuento si el tipo de promoción es descuento.
        if tipo_promocion == "descuento":
            descuento = float(input("Ingrese el descuento en porcentaje (ej. 10 para 10%): "))
        else:
            descuento = 0

        producto_regalo = None
        # Si la promoción es de regalo, solicita el producto correspondiente.
        if tipo_promocion == "regalo":
            producto_regalo = input("Ingrese el nombre del producto de regalo: ").capitalize()

        producto_2x1 = None
        # Si la promoción es 2x1, solicita el producto correspondiente.
        if tipo_promocion == "2x1":
            producto_2x1 = input("Ingrese el producto al que se le aplicara 2x1: ").capitalize()

        metodo_pago = input("¿Es una promocion valida solo al pagar con tarjeta? (s/n): ").lower() == 's'
        
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")

        try:
            # Intenta convertir la fecha de vencimiento a un objeto de fecha.
            fecha_venc = datetime.strptime(fecha_vencimiento, '%Y-%m-%d').date()
            self.promociones.append({
                "nombre": nombre,
                "tipo": tipo_promocion,
                "descuento": descuento,
                "producto_regalo": producto_regalo,
                "producto_2x1": producto_2x1,
                "solo_tarjeta": metodo_pago,
                "vencimiento": fecha_venc
            })
            print(f"Promocion {nombre} anadida, valida hasta {fecha_venc}.")
        except ValueError:
            print("Fecha invalida, intente de nuevo.")

    def ver_promociones(self):
        # Muestra las promociones activas en el sistema.
        if self.promociones:
            print("Promociones activas:")
            for promo in self.promociones:
                print(f"{promo['nombre']} - Tipo: {promo['tipo']}, valido hasta {promo['vencimiento']}.")
        else:
            print("No hay promociones activas.")

    def aplicar_promocion(self, total, metodo_pago):
        # Aplica las promociones disponibles al total de la orden.
        promocion_aplicada = False
        for promo in self.promociones:
            if promo['vencimiento'] >= datetime.now().date():  # Verifica que la promoción esté vigente.
                if promo['solo_tarjeta'] and metodo_pago != 'tarjeta':
                    continue  # Si es solo para tarjeta y el pago no es con tarjeta, se salta.

                # Aplica el descuento si es una promoción de descuento.
                if promo['tipo'] == 'descuento':
                    aplicar = input(f"¿Desea aplicar la promocion '{promo['nombre']}' con {promo['descuento']}% de descuento? (s/n): ").lower()
                    if aplicar == 's':
                        descuento = total * (promo['descuento'] / 100)
                        total -= descuento
                        promocion_aplicada = True
                        print(f"Se ha aplicado un descuento de ${descuento:.2f}.")
                        break
                # Aplica el 2x1 si corresponde.
                elif promo['tipo'] == '2x1':
                    if promo['producto_2x1'] in [orden['producto'] for orden in self.ordenes]:
                        aplicar = input(f"¿Desea aplicar la promocion 2x1 en {promo['producto_2x1']}? (s/n): ").lower()
                        if aplicar == 's':
                            total -= self.menu[promo['producto_2x1']]
                            promocion_aplicada = True
                            print(f"Se ha aplicado el 2x1 en {promo['producto_2x1']}.")
                            break
                # Ofrece un producto gratis si es una promoción de regalo.
                elif promo['tipo'] == 'regalo':
                    aplicar = input(f"¿Desea aplicar la promocion '{promo['nombre']}' y recibir un {promo['producto_regalo']} gratis? (s/n): ").lower()
                    if aplicar == 's':
                        print(f"¡Has recibido un {promo['producto_regalo']} gratis!")
                        promocion_aplicada = True
                        break
        if not promocion_aplicada:
            print("No se aplico ninguna promocion.")
        return total  # Retorna el total después de aplicar promociones.

    def Sumar_los_Pedidos(self, numero_mesa):
        # Permite al usuario seleccionar productos y cantidades para agregar a su pedido.
        total_pedido = 0
        while True:
            self.ver_menu()  # Muestra el menú.
            item = input("Seleccione un producto (o 'finalizar' para terminar): ").capitalize()
            if item == 'Finalizar':
                break
            elif item in self.menu:
                cantidad = int(input(f"¿Cuántos {item} desea? "))
                total_item = self.menu[item] * cantidad  # Calcula el total por el item.
                total_pedido += total_item  # Suma al total del pedido.
                self.ordenes.append({"mesa": numero_mesa, "producto": item, "cantidad": cantidad, "total_item": total_item})  # Agrega el pedido a las órdenes.
            else:
                print("Producto no disponible.")
        print(f"Total a pagar para la mesa {numero_mesa}: ${total_pedido:.2f}")
        return total_pedido

    def procesar_pago(self, numero_mesa):
        # Procesa el pago de la mesa indicada.
        total_pedido = sum(orden['total_item'] for orden in self.ordenes if orden['mesa'] == numero_mesa)
        if total_pedido > 0:
            metodo_pago = input("Seleccione el metodo de pago ('tarjeta' o 'efectivo'): ").lower()
            total_con_descuento = self.aplicar_promocion(total_pedido, metodo_pago)  # Aplica promociones.
            if metodo_pago == 'efectivo':
                pago_cliente = float(input("Ingrese el monto pagado por el cliente: "))
                if pago_cliente >= total_con_descuento:
                    cambio = pago_cliente - total_con_descuento
                    print(f"Pago procesado. Cambio a devolver: ${cambio:.2f}.")
                else:
                    print("El monto ingresado es menor al total. No se puede procesar el pago.")
            elif metodo_pago == 'tarjeta':
                print(f"Pago procesado para la mesa {numero_mesa} por ${total_con_descuento:.2f} con tarjeta.")
            else:
                print("Metodo de pago no valido. Intente de nuevo.") 
        else:
            print(f"No hay pedidos pendientes para la mesa {numero_mesa}.")

    def menu_principal(self):
        # Muestra el menú principal del sistema y permite al usuario interactuar con él.
        while True:
            print("\n--- Menu del Sistema ---")   
            print("1. Ver Menu")  
            print("2. Agregar Nuevo Producto al Menu")  
            print("3. Reservar Mesa")
            print("4. Ver Mesas Reservadas")
            print("5. Agregar Pedido")
            print("6. Ver Cola de Pedidos")
            print("7. Agregar Promocion") 
            print("8. Ver Promociones")
            print("9. Procesar Pago")
            print("10. Salir")
            opcion = input("Seleccione una opcion: ")  

            if opcion == "1":
                self.ver_menu()  # Muestra el menú.
            elif opcion == "2":
                self.agregar_nuevo_item()  # Permite agregar un nuevo producto.
            elif opcion == "3":
                numero_mesa = int(input("Ingrese el número de mesa: "))
                self.mesas_apartadas[numero_mesa] = True  # Reserva la mesa.
                print(f"Mesa {numero_mesa} reservada.")
            elif opcion == "4":
                print(f"Mesas reservadas: {', '.join(map(str, self.mesas_apartadas.keys()))}")  # Muestra las mesas reservadas.
            elif opcion == "5":
                numero_mesa = int(input("Ingrese el número de mesa para agregar pedido: "))
                self.Sumar_los_Pedidos(numero_mesa)  # Agrega pedidos a la mesa.
            elif opcion == "6":
                print("Cola de Pedidos:", self.ordenes)  # Muestra la cola de pedidos.
            elif opcion == "7":
                self.agregar_promocion()  # Agrega una nueva promoción.
            elif opcion == "8":
                self.ver_promociones()  # Muestra las promociones.
            elif opcion == "9":
                numero_mesa = int(input("Ingrese el número de mesa para procesar pago: "))
                self.procesar_pago(numero_mesa)  # Procesa el pago.
            elif opcion == "10":
                print("Saliendo del sistema...")  
                break  # Sale del sistema.
            else:
                print("Opción no válida. Intente de nuevo.")

# Crea una instancia del restaurante y ejecuta el menú principal.
restaurante = Restaurant()  
restaurante.menu_principal()  

