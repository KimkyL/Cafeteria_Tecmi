import tkinter as tk
from tkinter import messagebox
from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
from datetime import datetime 

# PERSONALIZACION DE LA VENTANA A VISUALIZAR
ventanas = tk.Tk()
ventanas.title("Sistema de gestión de Restaurante")
ventanas.geometry("1250x650+150+50")
ventanas.minsize(800, 500)
ventanas.iconbitmap("luna-cafe.ico")
ventanas.config(bg="#b79c6f")

bg_normal = "black"
fg_normal = "white"
bg_hover = "#6d422d"

# CONFIGURACIÓN DE LA FUENTE Y ESTILOS
font_menu = tkFont.Font(family="Poppins", size=12, weight="bold")

# FUNCIONES PARA LOS MENÚS
class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú del Restaurante")
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
        self.promociones = {}
        self.ordenes = {}
        
        # Área de visualización
        self.menu_display = tk.Text(self.root, height=20, width=80, bg="#b79c6f", font=font_menu, fg=fg_normal, bd=0.5)
        self.menu_display.pack()
        
        # Frame para el nuevo ítem
        self.frame_nuevo_item = tk.Frame(self.root, bg="#b79c6f")
        self.frame_nuevo_item.pack(pady=20)
        self.frame_reservas = tk.Frame(self.root, bg="#b79c6f")
        self.frame_reservas.pack(pady=20)
        
        self.frame_promociones = tk.Frame(self.root, bg="#b79c6f")
        self.frame_promociones.pack(pady=10, padx=10, fill='x')

        self.frame_ordenes = tk.Frame(self.root, bg="#b79c6f")
        self.frame_ordenes.pack(side='right', padx=20, pady=10, fill='y')

        # Mostrar el menú inicialmente
        self.ver_menu()

    def ver_menu(self):
        self.menu_display.delete('1.0', tk.END)
        texto_centrado = "Menú disponible:\n"
        self.menu_display.insert(tk.END, " " * 70 + texto_centrado)
        for item, precio in self.menu.items():
            self.menu_display.insert(tk.END, f"{item}: ${precio:.2f}\n")

    def ver_reservaciones(self):
        self.menu_display.delete('1.0', tk.END)
        texto_centrado = "Mostrando Reservaciones\n"
        self.menu_display.insert(tk.END, " " * 65 + texto_centrado)
        detalles_reservacion = "Aquí se mostrarán las reservaciones..."
        self.menu_display.insert(tk.END, " " * 40 + detalles_reservacion)

    def ver_pedidos(self):
        self.menu_display.delete('1.0', tk.END)
        if not self.ordenes:
            self.menu_display.insert(tk.END, "No hay pedidos en la cola.\n")
        else:
            self.menu_display.insert(tk.END, "Cola de Pedidos:\n")
            for i, (mesa, pedidos) in enumerate(self.ordenes.items(), 1):
                self.menu_display.insert(tk.END, f"Mesa {mesa}: {', '.join(pedidos)}\n")

    def agregar_nuevo_item(self):
        label_nombre = tk.Label(self.frame_nuevo_item, text="Nombre:", bg="#b79c6f", fg="white", font="Poppins")
        label_nombre.grid(row=0, column=0, padx=5, pady=5)
        self.entryNombre = tk.Entry(self.frame_nuevo_item)
        self.entryNombre.grid(row=0, column=1, padx=5, pady=5)

        label_precio = tk.Label(self.frame_nuevo_item, text="Precio:", bg="#b79c6f", fg="white", font="Poppins")
        label_precio.grid(row=1, column=0, padx=5, pady=5)
        self.entryPrecio = tk.Entry(self.frame_nuevo_item)
        self.entryPrecio.grid(row=1, column=1, padx=5, pady=5)

        boton_guardar = tk.Button(self.frame_nuevo_item, text="Guardar", command=self.guardar_item, bg="#b79c6f")
        boton_guardar.grid(row=2, column=0, columnspan=2, pady=10)

    def guardar_item(self):
        nombre = self.entryNombre.get()
        precio = self.entryPrecio.get()

        try:
            precio = float(precio)
            self.menu[nombre] = precio
            print(f"Se ha agregado: {nombre} con un precio de {precio}")
            print("Menú actualizado:", self.menu)
            self.entryNombre.delete(0, END)
            self.entryPrecio.delete(0, END)
            self.ver_menu()
        except ValueError:
            print("Error: El precio debe ser un número válido.")

    def reservar_mesa(self):
        label_numero_mesa = tk.Label(self.frame_reservas, text="Número de mesa:", bg="#b79c6f", fg="white", font="Poppins")
        label_numero_mesa.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entryNumeroMesa = tk.Entry(self.frame_reservas)
        self.entryNumeroMesa.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        label_nombre_cliente = tk.Label(self.frame_reservas, text="Nombre del cliente:", bg="#b79c6f", fg="white", font="Poppins")
        label_nombre_cliente.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entryNombreCliente = tk.Entry(self.frame_reservas)
        self.entryNombreCliente.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        boton_reservar = tk.Button(self.frame_reservas, text="Reservar Mesa", command=self.guardar_reserva, bg="#b79c6f")
        boton_reservar.grid(row=2, column=0, columnspan=2, pady=10)

    def guardar_reserva(self):
        numero_mesa = self.entryNumeroMesa.get()
        nombre_cliente = self.entryNombreCliente.get()

        if numero_mesa and nombre_cliente:
            self.mesas_apartadas[numero_mesa] = nombre_cliente
            print(f"Se ha reservado la mesa {numero_mesa} para {nombre_cliente}")
            print("Mesas reservadas:", self.mesas_apartadas)

            self.entryNumeroMesa.delete(0, END)
            self.entryNombreCliente.delete(0, END)
            self.actualizar_display_reservas()
        else:
            print("Error: Debes ingresar un número de mesa y el nombre del cliente.")

    def actualizar_display_reservas(self):
        self.menu_display.delete('1.0', tk.END)
        self.menu_display.insert(tk.END, "Mesas reservadas:\n")
        for numero_mesa, nombre_cliente in self.mesas_apartadas.items():
            self.menu_display.insert(tk.END, f"Mesa {numero_mesa}: Reservada para {nombre_cliente}\n")

    def agregar_promocion(self):
        label_nombre_promocion = tk.Label(self.frame_promociones, text="Nombre de la promoción:", bg="#b79c6f", fg="white", font="Poppins")
        label_nombre_promocion.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.entryNombrePromocion = tk.Entry(self.frame_promociones)
        self.entryNombrePromocion.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        label_descuento = tk.Label(self.frame_promociones, text="Descuento (%):", bg="#b79c6f", fg="white", font="Poppins")
        label_descuento.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.entryDescuento = tk.Entry(self.frame_promociones)
        self.entryDescuento.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        boton_guardar_promocion = tk.Button(self.frame_promociones, text="Guardar Promoción", command=self.guardar_promocion, bg="#b79c6f")
        boton_guardar_promocion.grid(row=2, column=0, columnspan=2, pady=10)

    def guardar_promocion(self):
        nombre_promocion = self.entryNombrePromocion.get()
        descuento = self.entryDescuento.get()

        try:
            descuento = float(descuento)
            self.promociones[nombre_promocion] = descuento
            print(f"Promoción agregada: {nombre_promocion} con un descuento de {descuento}%")
            print("Promociones actuales:", self.promociones)
            self.entryNombrePromocion.delete(0, END)
            self.entryDescuento.delete(0, END)
        except ValueError:
            print("Error: El descuento debe ser un número válido.")

    def ver_promociones(self):
        self.menu_display.delete('1.0', tk.END)
        if not self.promociones:
            self.menu_display.insert(tk.END, "No hay promociones disponibles.\n")
        else:
            self.menu_display.insert(tk.END, "Promociones disponibles:\n")
            for promo, desc in self.promociones.items():
                self.menu_display.insert(tk.END, f"{promo}: {desc}% de descuento\n")

    def crear_orden(self):
        label_numero_mesa = tk.Label(self.frame_ordenes, text="Número de mesa:", bg="#b79c6f", fg="white", font="Poppins")
        label_numero_mesa.grid(row=0, column=0, padx=20, pady=5, sticky='w')  # Ajustado el espaciado
        self.entryOrdenMesa = tk.Entry(self.frame_ordenes)
        self.entryOrdenMesa.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        label_items = tk.Label(self.frame_ordenes, text="Ítems (separados por comas):", bg="#b79c6f", fg="white", font="Poppins")
        label_items.grid(row=1, column=0, padx=20, pady=5, sticky='w')  # Ajustado el espaciado
        self.entryItems = tk.Entry(self.frame_ordenes)
        self.entryItems.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        boton_guardar_orden = tk.Button(self.frame_ordenes, text="Crear Orden", command=self.guardar_orden, bg="#b79c6f")
        boton_guardar_orden.grid(row=2, column=0, columnspan=2, pady=10)

    def guardar_orden(self):
        numero_mesa = self.entryOrdenMesa.get()
        items = self.entryItems.get()

        if numero_mesa and items:
            items_lista = [item.strip() for item in items.split(",")]
            self.ordenes[numero_mesa] = items_lista
            print(f"Orden creada para la mesa {numero_mesa}: {items_lista}")
            self.entryOrdenMesa.delete(0, END)
            self.entryItems.delete(0, END)
            self.ver_pedidos()
        else:
            print("Error: Debes ingresar un número de mesa y los ítems.")

def on_enter(e):
    e.widget.config(bg=bg_hover)

def on_leave(e):
    e.widget.config(bg=bg_normal)

# CONFIGURACIÓN DE MENÚS Y BOTONES
menu_frame = tk.Frame(ventanas, bg=bg_normal, height=30)
menu_frame.pack(fill='x')

app = RestaurantApp(ventanas)

# Creación de los botones Menubutton
boton_menu_comida = tk.Menubutton(menu_frame, text="Menú del restaurante", bg=bg_normal, fg=fg_normal, 
                                   relief='flat', font=font_menu)
boton_menu_mesas = tk.Menubutton(menu_frame, text="Reserva de mesas", bg=bg_normal, fg=fg_normal, 
                                  relief='flat', font=font_menu)
boton_menu_ordenes = tk.Menubutton(menu_frame, text="Pedidos y Órdenes", bg=bg_normal, fg=fg_normal, 
                                    relief='flat', font=font_menu)
boton_menu_promociones = tk.Menubutton(menu_frame, text="Promociones", bg=bg_normal, fg=fg_normal, 
                                        relief='flat', font=font_menu)

# ASIGNACIÓN DE MENÚS A CADA BOTÓN
menu_comida = tk.Menu(boton_menu_comida, tearoff=0, activebackground=bg_hover)
menu_comida.add_command(label="Ver Menú", command=app.ver_menu)
menu_comida.add_command(label="Agregar Producto", command=app.agregar_nuevo_item)
boton_menu_comida.config(menu=menu_comida)

menu_mesas = tk.Menu(boton_menu_mesas, tearoff=0, activebackground=bg_hover)
menu_mesas.add_command(label="Ver Reservaciones", command=app.ver_reservaciones)
menu_mesas.add_command(label="Reservar Mesa", command=app.reservar_mesa)
boton_menu_mesas.config(menu=menu_mesas)

menu_ordenes = tk.Menu(boton_menu_ordenes, tearoff=0, activebackground=bg_hover)
menu_ordenes.add_command(label="Ver pedidos", command=app.ver_pedidos)
menu_ordenes.add_command(label="Crear Orden", command=app.crear_orden)
boton_menu_ordenes.config(menu=menu_ordenes)

menu_promociones = tk.Menu(boton_menu_promociones, tearoff=0, activebackground=bg_hover)
menu_promociones.add_command(label="Agregar Promoción", command=app.agregar_promocion)
menu_promociones.add_command(label="Ver promociones", command=app.ver_promociones)
boton_menu_promociones.config(menu=menu_promociones)

# EMPAQUETAR LOS BOTONES
boton_menu_comida.pack(side='left', padx=10)
boton_menu_mesas.pack(side='left', padx=10)
boton_menu_ordenes.pack(side='left', padx=10)
boton_menu_promociones.pack(side='left', padx=10)

# Configurar el efecto hover para los botones
boton_menu_comida.bind("<Enter>", on_enter)
boton_menu_comida.bind("<Leave>", on_leave)

boton_menu_mesas.bind("<Enter>", on_enter)
boton_menu_mesas.bind("<Leave>", on_leave)

boton_menu_ordenes.bind("<Enter>", on_enter)
boton_menu_ordenes.bind("<Leave>", on_leave)

boton_menu_promociones.bind("<Enter>", on_enter)
boton_menu_promociones.bind("<Leave>", on_leave)




# Crear etiqueta principal
pantalla = tk.Label(ventanas, text="Bienvenido a Luna Café\nSeleccione una opción en el menú", 
                    bg="#b79c6f", fg="white", font=("Poppins", 12, "bold"))
pantalla.pack(pady=50)

canvas = tk.Canvas(ventanas, width=220, height=700, background="#b79c6f", highlightthickness=0)

# Cargar la primera imagen PNG con transparencia
img = Image.open("file.png")  # Asegúrate de que sea un archivo PNG con transparencia
img = img.resize((200, 250))  # Redimensionar si es necesario
img_tk = ImageTk.PhotoImage(img)  # Convertir la imagen a un formato compatible con Tkinter

# Cargar la segunda imagen PNG con transparencia
img2 = Image.open("file2.png")  # Asegúrate de que sea un archivo PNG con transparencia
img2 = img2.resize((200, 250))  # Redimensionar si es necesario
img2_tk = ImageTk.PhotoImage(img2)

# Cargar la tercera imagen PNG con transparencia
img3 = Image.open("file3.png")  # Asegúrate de que sea un archivo PNG con transparencia
img3 = img3.resize((200, 250))  # Redimensionar si es necesario
img3_tk = ImageTk.PhotoImage(img3)

# Agregar la primera imagen al Canvas
canvas.create_image(-40, -40, anchor="nw", image=img_tk)

# Agregar la segunda imagen al Canvas, asegurando que esté dentro del área visible
canvas.create_image(20, 100, anchor="nw", image=img2_tk)  # Alinear la segunda imagen debajo de la primera
canvas.create_image(-15, 280, anchor="nw", image=img3_tk) 

canvas.place(x=10, y=60)

# Segundo canvas 
canvas2 = tk.Canvas(ventanas, width=200, height=900, background="#b79c6f", highlightthickness=0)

# Cargar la cuarta imagen PNG con transparencia (taza de café)
img4 = Image.open("Liquidon.png")  # Asegúrate de que sea un archivo PNG con transparencia
img4 = img4.resize((200, 250))  # Redimensionar si es necesario
img4_tk = ImageTk.PhotoImage(img4)  # Convertir la imagen a un formato compatible con Tkinter

# Cargar la quinta imagen PNG con transparencia (texto)
img5 = Image.open("taza.png")  # Asegúrate de que sea un archivo PNG con transparencia
img5 = img5.resize((200, 250))  # Redimensionar si es necesario
img5_tk = ImageTk.PhotoImage(img5)

# Agregar la cuarta imagen al Canvas
canvas2.create_image(30, 90, anchor="nw", image=img4_tk)

# Agregar la quinta imagen al Canvas
canvas2.create_image(0, 220, anchor="nw", image=img5_tk)

canvas2.place(x=1030, y=60)

# Iniciar el loop de la ventana
ventanas.mainloop()  

