import time
import os
from datetime import datetime

class Restaurant:
    def __init__(self):
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
        self.mesas_apartadas = {}
        self.ordenes = []
        self.pagos = []
        self.promociones = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def slow_print(self, text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def ver_menu(self):
        self.clear_screen()
        self.slow_print("=== Menú disponible ===")
        for item, precio in self.menu.items():
            self.slow_print(f"{item}: ${precio:.2f}")
        self.slow_print("\nPresione Enter para regresar al menú principal.")
        input()

    def agregar_nuevo_item(self):
        self.clear_screen()
        self.slow_print("=== Agregar Nuevo Producto al Menú ===")
        item = input("Ingrese el nombre del nuevo producto: ").capitalize()
        if item in self.menu:
            self.slow_print("Este producto ya existe en el menú.")
        else:
            try:
                precio = float(input("Ingrese el precio del nuevo producto: "))
                self.menu[item] = precio
                self.slow_print(f"{item} ha sido añadido al menú con un precio de ${precio:.2f}.")
            except ValueError:
                self.slow_print("Precio inválido. Intente de nuevo.")
        self.slow_print("\nPresione Enter para regresar al menú principal.")
        input()

    def agregar_promocion(self):
        self.clear_screen()
        self.slow_print("=== Agregar Promoción ===")
        nombre = input("Ingrese el nombre de la promoción: ").capitalize()
        tipo_promocion = input("Seleccione el tipo de promoción ('descuento', '2x1', 'regalo'): ").lower()

        if tipo_promocion == "descuento":
            try:
                descuento = float(input("Ingrese el descuento en porcentaje (ej. 10 para 10%): "))
            except ValueError:
                self.slow_print("Descuento inválido. Intente de nuevo.")
                return
        else:
            descuento = 0

        producto_regalo = None
        if tipo_promocion == "regalo":
            producto_regalo = input("Ingrese el nombre del producto de regalo: ").capitalize()

        producto_2x1 = None
        if tipo_promocion == "2x1":
            producto_2x1 = input("Ingrese el producto al que se le aplicará 2x1: ").capitalize()

        metodo_pago = input("¿Es una promoción válida solo al pagar con tarjeta? (s/n): ").lower() == 's'
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")

        try:
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
            self.slow_print(f"Promoción {nombre} añadida, válida hasta {fecha_venc}.")
        except ValueError:
            self.slow_print("Fecha inválida, intente de nuevo.")
        self.slow_print("\nPresione Enter para regresar al menú principal.")
        input()

    def ver_promociones(self):
        self.clear_screen()
        self.slow_print("=== Promociones Activas ===")
        if self.promociones:
            for promo in self.promociones:
                self.slow_print(f"{promo['nombre']} - Tipo: {promo['tipo']}, válido hasta {promo['vencimiento']}.")
        else:
            self.slow_print("No hay promociones activas.")
        self.slow_print("\nPresione Enter para regresar al menú principal.")
        input()

    def aplicar_promocion(self, total, metodo_pago):
        promocion_aplicada = False
        for promo in self.promociones:
            if promo['vencimiento'] >= datetime.now().date():
                if promo['solo_tarjeta'] and metodo_pago != 'tarjeta':
                    continue

                if promo['tipo'] == 'descuento':
                    aplicar = input(f"¿Desea aplicar la promoción '{promo['nombre']}' con {promo['descuento']}% de descuento? (s/n): ").lower()
                    if aplicar == 's':
                        descuento = total * (promo['descuento'] / 100)
                        total -= descuento
                        promocion_aplicada = True
                        self.slow_print(f"Se ha aplicado un descuento de ${descuento:.2f}.")
                        break
                elif promo['tipo'] == '2x1':
                    if promo['producto_2x1'] in [orden['producto'] for orden in self.ordenes]:
                        aplicar = input(f"¿Desea aplicar la promoción 2x1 en {promo['producto_2x1']}? (s/n): ").lower()
                        if aplicar == 's':
                            total -= self.menu[promo['producto_2x1']]
                            promocion_aplicada = True
                            self.slow_print(f"Se ha aplicado el 2x1 en {promo['producto_2x1']}.")
                            break
                elif promo['tipo'] == 'regalo':
                    aplicar = input(f"¿Desea aplicar la promoción '{promo['nombre']}' y recibir un {promo['producto_regalo']} gratis? (s/n): ").lower()
                    if aplicar == 's':
                        self.slow_print(f"¡Has recibido un {promo['producto_regalo']} gratis!")
                        promocion_aplicada = True
                        break
        if not promocion_aplicada:
            self.slow_print("No se aplicó ninguna promoción.")
        return total

    def Sumar_los_Pedidos(self, numero_mesa):
        total_pedido = 0
        while True:
            self.ver_menu()
            item = input("Seleccione un producto (o 'finalizar' para terminar): ").capitalize()
            if item == 'Finalizar':
                break
            elif item in self.menu:
                try:
                    cantidad = int(input(f"¿Cuántos {item} desea? "))
                    total_item = self.menu[item] * cantidad
                    total_pedido += total_item
                    self.ordenes.append({"mesa": numero_mesa, "producto": item, "cantidad": cantidad, "total_item": total_item})
                except ValueError:
                    self.slow_print("Cantidad inválida. Intente de nuevo.")
            else:
                self.slow_print("Producto no disponible.")
        self.slow_print(f"Total a pagar para la mesa {numero_mesa}: ${total_pedido:.2f}")
        self.slow_print("\nPresione Enter para regresar al menú principal.")
        input()
        return total_pedido

    def procesar_pago(self, numero_mesa):
        total_pedido = sum(orden['total_item'] for orden in self.ordenes if orden['mesa'] == numero_mesa)
        if total_pedido > 0:
            metodo_pago = input("Seleccione el método de pago ('tarjeta' o 'efectivo'): ").lower()
            total_con_descuento = self.aplicar_promocion(total_pedido, metodo_pago)
            if metodo_pago == 'efectivo':
                try:
                    pago_cliente = float(input("Ingrese el monto pagado por el cliente: "))
                    if pago_cliente >= total_con_descuento:
                        cambio = pago_cliente - total_con_descuento
                        self.slow_print(f"Pago procesado. Cambio a devolver: ${cambio:.2f}.")
                    else:
                        self.slow_print("El monto ingresado es menor al total. No se puede procesar el pago.")
                except ValueError:
                    self.slow_print("Monto inválido. Intente de nuevo.")
            elif metodo_pago == 'tarjeta':
                self.slow_print(f"Pago procesado para la mesa {numero_mesa} por ${total_con_descuento:.2f} con tarjeta.")
            else:
                self.slow_print("Método de pago no válido. Intente de nuevo.")
        else:
            self.slow_print(f"No hay pedidos pendientes para la mesa {numero_mesa}.")
        self.slow_print("\nPresione Enter para regresar al menú principal.")
        input()

    def menu_principal(self):
        while True:
            self.clear_screen()
            self.slow_print("=== Menú del Sistema ===")
            self.slow_print("1. Ver Menú")
            self.slow_print("2. Agregar Nuevo Producto al Menú")
            self.slow_print("3. Reservar Mesa")
            self.slow_print("4. Ver Mesas Reservadas")
            self.slow_print("5. Agregar Promoción")
            self.slow_print("6. Ver Promociones")
            self.slow_print("7. Sumar Pedidos")
            self.slow_print("8. Procesar Pago")
            self.slow_print("0. Salir")

            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    self.ver_menu()
                elif opcion == 2:
                    self.agregar_nuevo_item()
                elif opcion == 3:
                    numero_mesa = input("Ingrese el número de la mesa: ")
                    self.mesas_apartadas[numero_mesa] = True
                    self.slow_print(f"Mesa {numero_mesa} reservada.")
                elif opcion == 4:
                    self.slow_print("Mesas reservadas: " + ", ".join(self.mesas_apartadas.keys()))
                    self.slow_print("\nPresione Enter para continuar.")
                    input()
                elif opcion == 5:
                    self.agregar_promocion()
                elif opcion == 6:
                    self.ver_promociones()
                elif opcion == 7:
                    numero_mesa = input("Ingrese el número de la mesa para sumar pedidos: ")
                    self.Sumar_los_Pedidos(numero_mesa)
                elif opcion == 8:
                    numero_mesa = input("Ingrese el número de la mesa para procesar el pago: ")
                    self.procesar_pago(numero_mesa)
                elif opcion == 0:
                    self.slow_print("Gracias por usar el sistema. Hasta luego.")
                    break
                else:
                    self.slow_print("Opción inválida. Intente de nuevo.")
            except ValueError:
                self.slow_print("Entrada inválida. Por favor ingrese un número.")

restaurante = Restaurant()
restaurante.menu_principal()

