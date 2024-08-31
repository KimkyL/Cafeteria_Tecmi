Algoritmo Hola

	Escribir "Este es el menu Pizza, Hamburgesa, Ensalada"
	Leer VerMenu
Segun (VerMenu) 
    Caso "Si":
        Repetir
            Escribir "Agregar Producto"
            Leer Producto
            Segun (Producto) 
                Caso "Pizza":
                    Leer Cantidad
                    Escribir "Pizza agregada "
                Caso "Hamburguesa":
                    Leer Cantidad
                    Escribir "Hamburguesa agregada "
                Caso "Ensalada":
                    Leer Cantidad
                    Escribir "Ensalada agregada"
                Caso Contrario:
                    Escribir "Error: No se encontro en el menu acaso lo escribiste bien"
            FinSegun
            Escribir "¿Finalizar pedido? (Si/No)"
            Leer Finalizar
			Hastaque alizarPedido = "Si"
			Escribir "Se calcula el total y se almacena"
		Caso "No":
			Escribir "Fin del proceso para ese cliente"
	FinSegun
	
	Escribir "Deseas reservar una mesa"
	Leer ReservarMesa
	
	Segun (ReservarMesa) Hacer
		Caso "Si":
			Escribir "Mesa reservada"
				Caso "No":
					Escribir "Error: mesa ya ocupada"
				Caso "No":
					Escribir "No se te realizo la reserva"
	FinSegun
	
	Escribir "Procesa tu pago para continuar"
	Leer ProcesarPago

	
	Segun (MetodoPagoValido) 
		Caso "Si":
			Escribir "Pago procesado y guardado"
		Caso "No":
			Escribir "Error: Metodo de ppago incorrecto"
	FinSegun
	Escribir ("Quieres ver la cola de pedidos?")
	Leer VerColaDePedidos
	
	Segun (VerColaDePedidos) 
		Caso "Si":
			Escribir "Mostrando cola de pedidos"
	FinSegun
	
	Escribir "¿Finalizar Sistema? (Si/No)"
	Leer FinalizarSistema
	Si FinalizarSistema = "Si" Entonces
		Escribir "Este sistma finalizo y va hacer kabum en 2 segundos"
	Sino
		Escribir "Volviendo al menu principal no solo que acaba el algoritmo"
	FinSi
	
FinAlgoritmo

