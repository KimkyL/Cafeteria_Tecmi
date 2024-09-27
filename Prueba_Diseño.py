import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tkinter import messagebox
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
font_menu2 = tkFont.Font(family="Poppins", size=12, weight="bold",  ) 
  # Cambiamos la fuente y tamaño del menú


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
        self.ordenes = []  # Asegúrate de inicializar aquí las órdenes
        self.promociones = [] 
        # Crear el área de visualización del menú
        self.menu_display = tk.Text(self.root, height=20, width=80, bg="#b79c6f", font=font_menu2, fg=fg_normal,bd=0.5 )
        self.menu_display.pack()
        self.frame_nuevo_item = tk.Frame(root)
        self.frame_nuevo_item.pack(pady=20)


    def ver_menu(self):
        # Muestra el menú disponible en el widget Text de Tkinter.
        self.menu_display.delete('1.0', tk.END)  # Limpia cualquier contenido anterior.
        texto_centrado = "Menú disponible:\n"
        self.menu_display.insert(tk.END, " " * 70 + texto_centrado)
        for item, precio in self.menu.items():
            self.menu_display.insert(tk.END, f"{item}: ${precio:.2f}\n")
 

    def ver_reservaciones(self):
        # Muestra las reservaciones en el área de visualización del menú.
        self.menu_display.delete('1.0', tk.END)  # Limpia cualquier contenido anterior.
        texto_centrado = "Mostrando Reservaciones\n"
        self.menu_display.insert(tk.END, " " * 65 + texto_centrado)
        detalles_reservacion = "Aquí se mostrarán las reservaciones..."
        self.menu_display.insert(tk.END, " " * 40 + detalles_reservacion)
    
    def ver_pedidos(self):
        # Verifica si hay pedidos en la lista y los muestra.
        self.menu_display.delete('1.0', tk.END)
        if not self.ordenes:
            self.menu_display.insert(tk.END, "No hay pedidos en la cola.\n")
        else:
            self.menu_display.insert(tk.END, "Cola de Pedidos:\n")
            for i, pedido in enumerate(self.ordenes, 1):
                self.menu_display.insert(tk.END, f"{i}. {pedido}\n")

    def ver_promociones(self):
        # Muestra las promociones en el área de visualización del menú.
        self.menu_display.delete('1.0', tk.END)
        texto_centrado = "Mostrando Promociones\n"
        self.menu_display.insert(tk.END, " " * 65 + texto_centrado)
        if not self.promociones:
            self.menu_display.insert(tk.END, "No hay promociones activas.\n")
        else:
            for promo in self.promociones:
                self.menu_display.insert(tk.END, f"Promoción: {promo}\n")

    def agregar_nuevo_item(self):
        entry = tk.Entry(takefocus=False)
        # Posicionarla en la ventana.
        entry.place(x=550, y=450)
        entry.insert(5, "Hola mundo!")
        button = tk.Button(text="Obtener texto", command=lambda: print(entry.get()))
        button.place(x=50, y=100)

    def reservar(self):
        numero_mesa = self.entry_numero_mesa.get()

        try:
            numero_mesa = int(numero_mesa)
            if numero_mesa in self.mesas_apartadas:
                messagebox.showerror("Error", f"La mesa {numero_mesa} ya está reservada.")
            else:
                self.mesas_apartadas[numero_mesa] = True
                messagebox.showinfo("Éxito", f"Mesa {numero_mesa} reservada con éxito.")
                self.entry_numero_mesa.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número de mesa válido.")

    def agregar_promocion_ui(self):
        self.frame_promocion = tk.Frame(self.root)
        self.frame_promocion.pack(pady=20)

        tk.Label(self.frame_promocion, text="Nombre de la promoción:").grid(row=0, column=0, padx=5)
        self.entry_promo_nombre = tk.Entry(self.frame_promocion)
        self.entry_promo_nombre.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_promocion, text="Tipo de promoción:").grid(row=1, column=0, padx=5)
        self.entry_promo_tipo = tk.Entry(self.frame_promocion)
        self.entry_promo_tipo.grid(row=1, column=1, padx=5)

        tk.Label(self.frame_promocion, text="Descuento (solo para 'descuento'):").grid(row=2, column=0, padx=5)
        self.entry_promo_descuento = tk.Entry(self.frame_promocion)
        self.entry_promo_descuento.grid(row=2, column=1, padx=5)

        tk.Label(self.frame_promocion, text="Producto de regalo (solo para 'regalo'):").grid(row=3, column=0, padx=5)
        self.entry_promo_regalo = tk.Entry(self.frame_promocion)
        self.entry_promo_regalo.grid(row=3, column=1, padx=5)

        tk.Label(self.frame_promocion, text="Producto 2x1 (solo para '2x1'):").grid(row=4, column=0, padx=5)
        self.entry_promo_2x1 = tk.Entry(self.frame_promocion)
        self.entry_promo_2x1.grid(row=4, column=1, padx=5)

        tk.Label(self.frame_promocion, text="Fecha de vencimiento (YYYY-MM-DD):").grid(row=5, column=0, padx=5)
        self.entry_promo_venc = tk.Entry(self.frame_promocion)
        self.entry_promo_venc.grid(row=5, column=1, padx=5)

        tk.Button(self.frame_promocion, text="Agregar Promoción", command=self.agregar_promocion).grid(row=6, columnspan=2, pady=10)

    def agregar_promocion(self):
        nombre = self.entry_promo_nombre.get().capitalize()
        tipo_promocion = self.entry_promo_tipo.get().lower()
        descuento = self.entry_promo_descuento.get() if tipo_promocion == "descuento" else None
        producto_regalo = self.entry_promo_regalo.get() if tipo_promocion == "regalo" else None
        producto_2x1 = self.entry_promo_2x1.get() if tipo_promocion == "2x1" else None
        fecha_vencimiento = self.entry_promo_venc.get()

        try:
            fecha_venc = datetime.strptime(fecha_vencimiento, '%Y-%m-%d').date()
            self.promociones.append({
                "nombre": nombre,
                "tipo": tipo_promocion,
                "descuento": float(descuento) if descuento else None,
                "producto_regalo": producto_regalo,
                "producto_2x1": producto_2x1,
                "vencimiento": fecha_venc
            })
            messagebox.showinfo("Éxito", f"Promoción {nombre} añadida, válida hasta {fecha_venc}.")
        except ValueError:
            messagebox.showerror("Error", "Fecha inválida o datos incorrectos.")


def pago_efectivo():
    pantalla.config(text="Pago en Efectivo")

def pago_tarjeta():
    pantalla.config(text="Pago con Tarjeta")

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
                                   relief='flat', font=font_menu, )
boton_menu_mesas = tk.Menubutton(menu_frame, text="Reserva de mesas", bg=bg_normal, fg=fg_normal, 
                                  relief='flat', font=font_menu,)
boton_menu_ordenes = tk.Menubutton(menu_frame, text="Pedidos y Órdenes", bg=bg_normal, fg=fg_normal, 
                                    relief='flat', font=font_menu, )
boton_menu_promociones = tk.Menubutton(menu_frame, text="Promociones", bg=bg_normal, fg=fg_normal, 
                                        relief='flat', font=font_menu, )
boton_menu_pago = tk.Menubutton(menu_frame, text="Pago", bg=bg_normal, fg=fg_normal, 
                                 relief='flat',font=font_menu, )


# ASIGNACIÓN DE MENÚS A CADA BOTÓN
menu_comida = tk.Menu(boton_menu_comida, tearoff=0, activebackground=bg_hover)
menu_comida.add_command(label="Ver Menú", command=app.ver_menu)
menu_comida.add_command(label="Agregar Producto", command=app.agregar_nuevo_item)
boton_menu_comida.config(menu=menu_comida)

menu_mesas = tk.Menu(boton_menu_mesas, tearoff=0, activebackground=bg_hover)
menu_mesas.add_command(label="Ver Reservaciones", command=app.ver_reservaciones)
menu_mesas.add_command(label="Reservar Mesa", command=app.reservar)
boton_menu_mesas.config(menu=menu_mesas)

menu_ordenes = tk.Menu(boton_menu_ordenes, tearoff=0, activebackground=bg_hover)
menu_ordenes.add_command(label="Ver pedidos", command=app.ver_pedidos)
boton_menu_ordenes.config(menu=menu_ordenes)

menu_promociones = tk.Menu(boton_menu_promociones, tearoff=0, activebackground=bg_hover)
menu_promociones.add_command(label="Ver promociones", command=app.ver_promociones)
boton_menu_promociones.config(menu=menu_promociones)

menu_pago = tk.Menu(boton_menu_pago, tearoff=0, activebackground=bg_hover)
menu_pago.add_command(label="Efectivo", command=pago_efectivo)
menu_pago.add_command(label="Tarjeta", command=pago_tarjeta)
boton_menu_pago.config(menu=menu_pago)


# EMPAQUETAR LOS BOTONES
boton_menu_comida.pack(side='left', padx=10)
boton_menu_comida.bind("<Enter>", on_enter)
boton_menu_comida.bind("<Leave>", on_leave)


boton_menu_mesas.pack(side='left', padx=10)
boton_menu_mesas.bind("<Enter>", on_enter)
boton_menu_mesas.bind("<Leave>", on_leave)

boton_menu_ordenes.pack(side='left', padx=10)
boton_menu_ordenes.bind("<Enter>", on_enter)
boton_menu_ordenes.bind("<Leave>", on_leave)


boton_menu_promociones.pack(side='left', padx=10)
boton_menu_promociones.bind("<Enter>", on_enter)
boton_menu_promociones.bind("<Leave>", on_leave)


boton_menu_pago.pack(side='left', padx=10)
boton_menu_pago.bind("<Enter>", on_enter)
boton_menu_pago.bind("<Leave>", on_leave)




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