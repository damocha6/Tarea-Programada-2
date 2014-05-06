# II Tarea Programada - Lenguajes de Programación - I Semestre 2014
## Estudiantes: - Edgar Solórzano
##              - Daniel Mora
##              - Gerardo Calderón


# ---------> Archivo para el manejo de la aplicación Web <---------

## Se importan las librerías necesarias de Flask

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__) # Instancia de la aplicacion


# *********************************
# ******** Mostrar Paginas ********
# *********************************

# - Funciones para mostrar las paginas desde el Menu

# - Funcion para mostrar la Pagina Principal

@app.route('/')
@app.route('/inicio')
def inicio():
	return render_template('rest.manager.htm')
	

# - Funcion para mostrar la pagina de Consulta de Restaurantes 

@app.route('/consultar/restaurantes')
def consulta_restaurantes():
	return render_template('rest.manager.consulta.restaurantes.htm')

# - Funcion para mostrar la pagina de Consulta de Platillos

@app.route('/consultar/platillos')
def consulta_platillos():
	return render_template('rest.manager.consulta.platillos.htm')


# - Funcion para mostrar la pagina de Mantenimiento de Restaurantes 

@app.route('/mantenimiento/restaurantes')
def mantenimiento_restaurantes():
	return render_template('rest.manager.mantenimiento.restaurantes.htm')
	
# - Funcion para mostrar la pagina de Mantenimiento de Platillos

@app.route('/mantenimiento/platillos')
def mantenimiento_platillos():
	return render_template('rest.manager.mantenimiento.platillos.htm')

# - Funcion para mostrar la pagina de Información del proyecto
	
@app.route('/informacion')
def informacion():
	return render_template('rest.manager.informacion.htm')


# !!!!!!!!!!!!!!!!!!!
#!!!!! CONSULTAS !!!!!!
# !!!!!!!!!!!!!!!!!!!

# - Funciones para devolver el resultado de las diferentes consultas. Se utiliza el valor de un input invisible para determinar cual consulta es la que se 
#   esta solicitando.

##############################
######## Restaurantes ########
##############################

## Mostrar todos los restaurantes ##

@app.route('/resultado', methods=['GET'])
def consultar_restaurantes_todos():
	titulo = 'Todos los restaurantes'
	## Llamar a la funcion que obtiene la lista con todos los restaurantes
	render_template('rest.manager.resultado.htm', title=titulo, restaurantes=resultado)

## Mostrar los restaurantes con un determinado tipo de comida ##

@app.route('/resultado', methods=['POST'])
def consultar_restaurantes_tipo():
	consulta = request.form['inputTipo']
	titulo = 'Restaurantes por tipo de comida: '+consulta
	## Llamar a la funcion que obtiene los restaurantes por tipo de comida
	render_template('rest.manager.resultado.htm', title=titulo, restaurantes=resultado)

## Mostrar los restaurantes con un determinado nombre ##

@app.route('/resultado', methods=['POST'])
def consultar_restaurantes_nombre():
	consulta = request.form['inputNombre']
	titulo = 'Restaurantes por nombre: '+consulta
	## Llamar a la funcion que obtiene los restaurantes por nombre
	render_template('rest.manager.resultado.htm', title=titulo, restaurantes=resultado)

## Mostrar los restaurantes que tengan platillos de cierto país ##

@app.route('/resultado', methods=['POST'])
def consultar_restaurantes_pais():
	consulta = request.form['inputPais']
	titulo = 'Restaurantes por país: '+consulta
	## Llamar a la funcion que obtiene los restaurantes que tengan platillos de cierto pais
	render_template('rest.manager.resultado.htm', title=titulo, restaurantes=resultado)



##############################
######### Platillos ##########
##############################

## Mostrar los platillos de cierto restaurante ##

@app.route('/resultado', methods=['POST'])
def consultar_platillos_restaurante():
	consulta = request.form['inputNombre']
	titulo = 'Platillos del restaurante: '+consulta
	
	## Llamar a la funcion en el archivo backend de Python que obtenga los platillos del restaurante ingresado
	render_template('rest.manager.resultado.htm', title=titulo, platillos=resultado)

## Mostrar los platillos de un restaurante que tengan cierto ingrediente ##

@app.route('/resultado', methods=['POST'])
def consultar_platillos_restaurante():
	consulta = request.form['inputNombre']
	ingrediente = request.form['inputIngrediente']
	titulo = 'Platillos del restaurante '+consulta+' que tienen '+ingrediente+':'
	
	## Llamar a la funcion en el archivo backend de Python que obtenga los platillos del restaurante ingresado con el ingrediente especificado
	render_template('rest.manager.resultado.htm', title=titulo, platillos=resultado)


# !!!!!!!!!!!!!!!!!!!
#!!! MANTENIMIENTO !!!
# !!!!!!!!!!!!!!!!!!!

# - Funciones para agregar los restaurantes y platillos a la Base de Conocimiento. Se utiliza el valor de un input invisible para determinar cual solicitud se 
#   debe realizar.   


##############################
######## Restaurantes ########
##############################

## Agregar un restaurante nuevo ##

@app.route('/resultado', methods=['POST'])
def agregar_restaurante():
	titulo = 'Restaurantes'
	mensaje_insercion = ''
	
	# Valores que ingresa el usuario:
	nombre = request.form['inputNombre']
	tipo = request.form['inputTipo']
	ubicacion = request.form['inputUbicacion']
	telefono = request.form['inputTelefono']
	horario = request.form['inputHorario']
	
	## Llamar a la funcion que agrega el restaurante en la Base de Conocimiento
	# Darle a mensaje el valor de 'El restaurante fue ingresado con éxito' o 'No se logró agregar el restaurante'
		mensaje_insercion = 'El restaurante fue ingresado con éxito'
		mensaje_insercion = 'No se logró agregar el restaurante'
	
		render_template('rest.manager.resultado.htm', title=titulo, mensaje=mensaje_insercion)

## Agregar un platillo a la lista de platillos de un restaurante ##

@app.route('/resultado', methods=['POST'])
def asignar_platillo():
	titulo = 'Platillos del Restaurante'
	mensaje_asignacion = ''
	
	# Valores que ingresa el usuario:
	nombre = request.form['inputNombre']
	platillo = request.form['inputPlatillo']
		
	## Llamar a la funcion que agrega el platillo a la lista de platillos del Restaurante ingresado
	# Darle a mensaje el valor de 'El platillo fue asignado con éxito' o 'No se logró asignar el platillo'
		mensaje_asignacion = 'El platillo fue asignado con éxito'
		mensaje_asignacion = 'No se logró asignar el platillo'
	
		render_template('rest.manager.resultado.htm', title=titulo, mensaje=mensaje_asignacion)

##############################
######### Platillos ##########
##############################

## Agregar un platillo nuevo ##

@app.route('/resultado', methods=['POST'])
def agregar_platillo():
	titulo = 'Platillos'
	mensaje_platillo = ''
	
	# Valores que ingresa el usuario:
	nombre = request.form['inputNombre']
	sabor = request.form['inputSabor']
	pais = request.form['inputPais']
	ingredientes = request.form['txtareaIngredientes']
		
	## Llamar a la funcion que agrega el platillo a la base de conocimientos
	# Darle a mensaje el valor de 'El platillo se agregó con éxito' o 'No se logró agregar el platillo'
		mensaje_platillo = 'El platillo se agregó con éxito'
		mensaje_platillo = 'No se logró agregar el platillo'
	
		render_template('rest.manager.resultado.htm', title=titulo, mensaje=mensaje_platillo)
		
## Agregar un ingrediente a un platillo ##

@app.route('/resultado', methods=['POST'])
def agregar_ingrediente():
	titulo = 'Ingredientes del Platillo'
	mensaje_ingrediente = ''
	
	# Valores que ingresa el usuario:
	platillo = request.form['inputNombre']
	ingrediente = request.form['inputIngrediente']
		
	## Llamar a la funcion que le agrega el ingrediente al platillo
	# Darle a mensaje el valor de 'El platillo fue asignado con éxito' o 'No se logró asignar el platillo'
		mensaje_ingrediente = 'El ingrediente fue agregado con éxito'
		mensaje_ingrediente = 'No se logró agregar el ingrediente'
	
		render_template('rest.manager.resultado.htm', title=titulo, mensaje=mensaje_ingrediente)


###############################################
# - Se corre el servidor web para la aplicación
###############################################
if __name__ == '__main__':
	app.run(debug=True)
