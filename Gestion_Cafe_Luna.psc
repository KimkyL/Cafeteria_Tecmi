Algoritmo Gestion_Cafe_Luna
	Definir opcion_comando, orden Como Cadena
	Definir mesas_disponibles, tiempo_espera Como Entero
	Definir menu_actualizado, pedidos_priorizados, pago_procesado Como Lógico

	mesas_disponibles <- 20
	menu_actualizado <- FALSO 
	pedidos_priorizados <- FALSO
	pago_procesado <- FALSO
	tiempo_espera <- 0
	
	Escribir 'Bienvenido a la Gestión de Luna Café'
	Escribir 'Seleccione una opción:'
	Escribir '1. Gestión de Pedidos'
	Escribir '2. Gestión de Mesas'
	Escribir '3. Procesamiento de Pagos'
	Escribir '4. Actualización del Menú'
	Leer opcion_comando
	Según opcion_comando Hacer
		'1':
			
			Escribir 'Ingrese la orden del cliente:'
			Leer orden
			Escribir 'Pedido registrado: ', orden
			pedidos_priorizados <- VERDADERO
			Escribir 'Pedido priorizado y enviado a cocina.'
		'2':
			
			Escribir 'Gestión de Mesas'
			Si mesas_disponibles>0 Entonces
				mesas_disponibles <- mesas_disponibles-1
				Escribir 'Mesa asignada. Mesas disponibles: ', mesas_disponibles
			SiNo
				Escribir 'No hay mesas disponibles en este momento.'
			FinSi
		'3':
			
			Escribir 'Procesando pago...'
			tiempo_espera <- tiempo_espera-5
			pago_procesado <- VERDADERO 
			Escribir 'Pago completado. Tiempo de espera: ', tiempo_espera, ' minutos.'
		'4':
			
			Escribir 'Actualizando menú...'
			menu_actualizado <- VERDADERO
			Escribir 'Menú actualizado exitosamente. Se agregaron nuevas promociones.'
		De Otro Modo:
			Escribir 'Opción no válida, por favor seleccione una opción válida.'
	FinSegún
FinAlgoritmo
