
# Codigo Prolog-Pyhton

#Edgar Solorzano
#Daniel Mora
#Gerardo Calderon

from pyswip import * #Importacion de la libreria que conecta prolog y python
from string import lower


p = Prolog() #Se inicia conexion Prolog-Python

#Crea las inserciones a la Base de Conocimientos

assertz = Functor("assertz")
restaurante = Functor("restaurante",5)
restaurante_modulo = newModule("restaurante_modulo")

assertz = Functor("assertz")
platillo = Functor("platillo",5)
platillo_modulo = newModule("platillo_modulo")

global lista_variables
global lista_variables2
global lista_parametros

global variables
global variables2
global parametros

#global listaIngredientes

#listaIngredientes = []
lista_variables = []
lista_variables2 = []
lista_parametros = []

variables = []
variables2 = []
parametros = []



#______________________________________________________________________________________________________________________________________#

#Funcion que agrega los restaurantes a la Base de Conocimientos
    
def agregar_restaurante():
    
    print"\nDigite los Datos del Nuevo Restaurante\n"
    indice = 0
    while indice == 0:
        nombre_restaurante = raw_input("Nombre Restaurante: ")#Aqui tenes que poner el .get del entry
        if nombre_restaurante == "":
            print "No digito nada"
        else:
            indice = 1

    indice = 0
    while indice == 0:
        tipoComida = raw_input("Tipo de comida: ")#Aqui tenes que poner el .get del entry
        if tipoComida == "":
            print "No digito nada"
        else:
            indice = 1
    indice = 0
    while indice == 0:
        ubicacion = raw_input("Ubicacion: ")#Aqui tenes que poner el .get del entry
        if ubicacion == "":
            print "No digito nada"
        else:
            indice = 1
            
    indice = 0        
    while indice == 0:
        telefono= raw_input("Telefono: ")#Aqui tenes que poner el .get del entry
        if telefono == "":
            print "No digito nada"
        else:
            indice = 1
            
    indice = 0
    while indice == 0:
        horario = raw_input("Horario: ")#Aqui tenes que poner el .get del entry
        if horario == "":
            print "No digito nada"
        else:
            indice = 1
    call(assertz(restaurante(nombre_restaurante.lower(),tipoComida.lower(),ubicacion.lower(),telefono.lower(),horario.lower())),module = restaurante_modulo)
    print"\nRestaurante Agregado con exito a la Base de Conocimientos"

#________________________________________________________________________________________________________________________________________________#
    
#Funcion que consulta los restaurantes desde la base de conocimientos

def Consultar_Restaurante(Nombre, Comida, Ubicacion, Telefono, Horario, lista_parametros, lista_variables2):
    q = Query(restaurante(Nombre, Comida, Ubicacion, Telefono, Horario), module = restaurante_modulo) #realiza la consulta a la base de conocimientos
    contador = 0 #Contador que lleva los resultados de la busqueda
    ind = 0 #lleva el indice de la lista_variables2
    while q.nextSolution():
        contador += 1
        for elemento in lista_parametros: #imprime la lista de los parametros del restaurante
            print elemento

        for i in lista_variables:	
            print lista_variables2[ind] + str(i.value) #imprime los resultados de los restaurantes encontrados
            ind += 1 #Verifica si obtuvo resultados
        ind = 0
        print "\n"
    if contador == 0:
        print "Su busqueda no Obtuvo Resultados"
        q.closeQuery() #se cierra la consulta

#________________________________________________________________________________________________________________________________________________#

#Funcion que imprime todos los restaurantes disponibles
        
def muestra_consulta_restaurantes():

    print "Restaurantes Disponibles en la Base de Conocimientos\n"
    
    Nombre = Variable()
    lista_variables.append(Nombre)
    lista_variables2.append("Nombre: ")

    Comida = Variable()
    lista_variables.append(Comida)
    lista_variables2.append("Comida: ")

    Ubicacion = Variable()
    lista_variables.append(Ubicacion)
    lista_variables2.append("Ubicacion: ")

    Telefono = Variable()
    lista_variables.append(Telefono)
    lista_variables2.append("Telefono: ")

    Horario = Variable()
    lista_variables.append(Horario)
    lista_variables2.append("Horario: ")

    Consultar_Restaurante(Nombre,Comida,Ubicacion,Telefono,Horario,lista_parametros,lista_variables2) #Llama a la funcion que consulta restaurantes

    General = []
    General.append([Nombre,Comida,Ubicacion,Telefono,Horario])
    print General

#________________________________________________________________________________________________________________________________________________#

#Funcion que agrega los restaurantes a la Base de Conocimientos

global listaIngredientes
listaIngredientes = []
    
def agregar_platillo():

      
    print"\nDigite los Datos del Nuevo Platillo\n"

    indice = 0
    while indice == 0:
        platillo_restaurante = raw_input("Restaurante al que pertenece el platillo: ")#Aqui tenes que poner el .get del entry
        if platillo_restaurante == "":
            print "No digito nada"
        else:
            indice = 1

    indice = 0
    while indice == 0:
        nombre_platillo = raw_input("Nombre del Platillo: ")#Aqui tenes que poner el .get del entry
        if nombre_platillo == "":
            print "No digito nada"
        else:
            indice = 1

    indice = 0
    while indice == 0:
        sabor = raw_input("Sabor: ")#Aqui tenes que poner el .get del entry
        if sabor == "":
            print "No digito nada"
        else:
            indice = 1
    indice = 0
    while indice == 0:
        origen = raw_input("Origen: ")#Aqui tenes que poner el .get del entry
        if origen == "":
            print "No digito nada"
        else:
            indice = 1
            
    indice = 0        
    while indice == 0:
        ingredientes= raw_input("Ingredientes: ")#Aqui tenes que poner el .get del entry
        if ingredientes == "":
            print "No digito nada"
        else:
            listaIngredientes + [ingredientes]
            indice = 1
    call(assertz(platillo(platillo_restaurante.lower(),nombre_platillo.lower(),sabor.lower(),origen.lower(),listaIngredientes)),module = platillo_modulo)
    print"\nPlatillo Agregado con Exito a la Base de Conocimientos"
    
 
#________________________________________________________________________________________________________________________________________________#

#Funcion que consulta los platillos de la base de conocimientos        

def Consultar_Platillo(Restaurante, Nombre, Sabor, Origen, listaIngredientes, parametros, variables2):
    q = Query(platillo(Restaurante, Nombre, Sabor, Origen, listaIngredientes), module = platillo_modulo) #realiza la consulta a la base de conocimientos
    contador = 0 #Lleva un contador de los resultados de la busqueda
    ind = 0 #lleva el indice de variables2
    while q.nextSolution():
        contador += 1
        for elemento in parametros: #imprime la lista de los parametros del platillo
            print elemento

        for i in variables:	
            print variables2[ind] + str(i.value) #imprime los resultados de los platillos encontrados
            ind += 1 #Verifica si obtuvo resultados
        ind = 0
        print "\n"
    if contador == 0:
        print "Su Busqueda no Obtuvo Resultados"
        q.closeQuery() #se cierra la consulta

#______________________________________________________________________________________________________________________________________________#
        
#Funcion que muestra todos los platillos disponibles

def muestra_consulta_platillos():

    print "Platillos Disponibles en la Base de Conocimientos\n"

    Restaurante = Variable()
    variables.append(Restaurante)
    variables2.append("Restaurante al que pertenece el platillo: ")
   
    Nombre = Variable()
    variables.append(Nombre)
    variables2.append("Nombre del Platillo: ")

    Sabor = Variable()
    variables.append(Sabor)
    variables2.append("Sabor: ")

    Origen = Variable()
    variables.append(Origen)
    variables2.append("Origen: ")

    listaIngredientes = Variable()
    variables.append(listaIngredientes)
    variables2.append("Ingredientes: ")

    Consultar_Platillo(Restaurante,Nombre,Sabor,Origen,listaIngredientes,parametros,variables2)
    
#_____________________________________________________________________________________________________________________________________________#

#Funcion que muestra los datos por parametros
    
def muestra_por_parametro_restaurante():
    print "\nIndique los Parametros de los Restaurantes que Desea Consultar\n"

    nombre = raw_input ("Nombre del Restaurante: ")
    if nombre == "":
        Nombre = Variable()
        lista_variables.append(Nombre)
        lista_variables2.append("Nombre del Restaurante ")
    else:
        Nombre = lower(nombre)
        lista_parametros.append("Nombre del Restaurante: " + str(Nombre))   

    comida = raw_input ("Tipo de Comida: ")
    if comida == "":
        Comida = Variable()
        lista_variables.append(Comida)
        lista_variables2.append("Tipo de Comida ")
    else:
        Comida = lower(comida)
        lista_parametros.append("Tipo de Comida: " + str(Comida))

    
    ubicacion = raw_input ("Ubicacion: ")
    if ubicacion == "":
        Ubicacion = Variable()
        lista_variables.append(Ubicacion)
        lista_variables2.append("Ubicacion: ")
    else:
        Ubicacion = lower(ubicacion)
        lista_parametros.append("Ubicacion: " + str(Ubicacion))

    telefono = raw_input ("Telefono: ")
    if telefono == "":
        Telefono = Variable()
        lista_variables.append(Telefono)
        lista_variables2.append("Telefono: ")
    else:
        Telefono = lower(telefono)
        lista_parametros.append("Telefono: " + str(Telefono))

    horario = raw_input ("Horario: ")
    if horario == "":
        Horario = Variable()
        lista_variables.append(Horario)
        lista_variables2.append("Horario: ")
    else:
        Horario = lower(horario)
        lista_parametros.append("Horario: " + str(Horario))

    print "\nLa Busqueda se hizo Bajo los Siguientes Parametros:\n"

    #se imprimen primero los datos en los que se baso la busqueda
    for i in lista_parametros:
        print i
    print "\nLos Resultados de la Consulta son: \n"
    Consultar_Restaurante(Nombre,Comida,Ubicacion,Telefono,Horario,lista_parametros,lista_variables2)            
#_____________________________________________________________________________________________________________________________________________________#


#Funcion que muestra los datos por parametros
    
def muestra_por_parametro_platillo():
    print "\nIndique los Parametros de los Restaurantes que Desea Consultar\n"

    nombre = raw_input ("Nombre del Restaurante al que pertenece el platillo: ")
    if nombre == "":
        Nombre = Variable()
        variables.append(Nombre)
        variables2.append("Nombre del Restaurante al que pertenece el platillo")
    else:
        Nombre = lower(nombre)
        parametros.append("Nombre del Restaurante al que pertenece el platillo: " + str(Nombre))   

    nomb_platillo = raw_input ("Nombre del Platillo: ")
    if nomb_platillo == "":
        NombrePlatillo = Variable()
        variables.append(NombrePlatillo)
        variables2.append("Nombre del Platillo")
    else:
        NombrePlatillo = lower(comida)
        parametros.append("Nombre del Platillo: " + str(Comida))

    
    sabor = raw_input ("Sabor: ")
    if sabor == "":
        Sabor = Variable()
        variables.append(Sabor)
        variables2.append("Sabor: ")
    else:
        Sabor = lower(sabor)
        parametros.append("Sabor: " + str(Sabor))

    origen = raw_input ("Origen: ")
    if origen == "":
        Origen = Variable()
        variables.append(Origen)
        variables2.append("Origen: ")
    else:
        Origen = lower(origen)
        parametros.append("Origen: " + str(Origen))

    ingredientes = raw_input ("Ingredientes: ")
    if ingredientes == "":
        Ingredientes = Variable()
        variables.append(Ingredientes)
        variables2.append("Ingredientes: ")
    else:
        Ingredientes = lower(ingredientes)
        parametros.append("Ingredientes: " + str(Ingredientes))

    print "\nLa Busqueda se hizo Bajo los Siguientes Parametros:\n"

    #se imprimen primero los datos en los que se baso la busqueda
    for i in parametros:
        print i
    print "\nLos Resultados de la Consulta son: \n"
    Consultar_Platillo(Nombre,NombrePlatillo,Sabor,Origen,Ingredientes,parametros,variables2)            
#_____________________________________________________________________________________________________________________________________________________#
