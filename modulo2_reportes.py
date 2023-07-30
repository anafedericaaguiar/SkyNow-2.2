"""Mostrar países: Al seleccionar esta opción, se deberán mostrar por consola todas 
las ubicaciones disponibles en el sistema."""

from modulo1_registro import database_paises, Pais


#MOSTRAR UBICACIONES DISPONIBLES

#Vamos a crear una funcion que me imprima las ubicaciones disponibles.
#Para ello, creamos una lista de objetos.
#Luego, iterando la base de datos que nos da la API de los paises procedimos a llenar la lista con el obj. Pais.

def imprimir_ubicaciones_disponibles():
    pais_con_datos=[] #Lista de Objetos
    for diccionario_paises in database_paises:
        pais = diccionario_paises["location_name"]
        capital = diccionario_paises["location_capital"]
        poblacion = diccionario_paises["population"]
        area = diccionario_paises["area"]
        moneda = diccionario_paises["currency"]
        idioma = diccionario_paises["main_language"]

        pais_con_datos.append(Pais(diccionario_paises["location_name"], diccionario_paises["location_capital"],diccionario_paises["population"], diccionario_paises["area"], diccionario_paises["currency"], diccionario_paises["main_language"]))

    #Aqui ya hemos llenado la lista de objetos, compuesta por el objeto "Pais" y sus atributos.
    #Procedemos a iterar dicha lista de objetos, pero solo extraemos el atributo que nos da el nombre del pais.

    for pais in pais_con_datos:
        print(f" {pais.pais}")

    #Listo, obtuvimos las ubicaciones disponibles.

#----------------------------------------------------------------------------------------------------------------------------------------------

#MOSTRAR DATOS POR PAIS

# Supongamos que ya tienes la lista pais_con_datos

def mostrar_datos_pais():
    # Pedir al usuario que ingrese el nombre del país
    ubicacion_conocer_datos=input("Ingrese el nombre de la ubicación a la cual desee conocer sus datos: ")

    pais_con_datos=[] #Lista de Objetos en donde vamos a buscar
    for diccionario_paises in database_paises:
        pais = diccionario_paises["location_name"]
        capital = diccionario_paises["location_capital"]
        poblacion = diccionario_paises["population"]
        area = diccionario_paises["area"]
        moneda = diccionario_paises["currency"]
        idioma = diccionario_paises["main_language"]

        pais_con_datos.append(Pais(diccionario_paises["location_name"], diccionario_paises["location_capital"],diccionario_paises["population"], diccionario_paises["area"], diccionario_paises["currency"], diccionario_paises["main_language"]))

    ubicacion_conocer_datos=ubicacion_conocer_datos.strip().title()

    #ESTA LISTA LA CREE PARA LA CONDICION DE ABAJO, PORQUE LA VOY A NECESITAR -------------------------------------------
   
    lista_paises=[]
    for diccionario_paises in database_paises:
        for pais in pais_con_datos:
            pais = diccionario_paises["location_name"]
        lista_paises.append(pais)

    #print(lista_paises)

    #------------------------------------------------------------------------------------------------------------------------------

    while not ubicacion_conocer_datos.replace(" ","").isalpha() or ubicacion_conocer_datos not in lista_paises: 
        print("Ingreso inválido.")
        ubicacion_conocer_datos=input("Ingrese el nombre de la ubicacion a la cual desee conocer los datos meteorologicos: ")
        ubicacion_conocer_datos=ubicacion_conocer_datos.strip().title()


    pais_encontrado = None 
    for pais in pais_con_datos: #Usando la lista que creamos arriba, vamos a buscar pais iterando.
        if pais.pais == ubicacion_conocer_datos: #Si la ubicacion que se ingreso, concuerda con uno de los datos de la lista.
            pais_encontrado = pais #Entonces la variable pais pasa a ser pais encontrado.
            break

    # Mostrar los datos del país encontrado (si se encontró)
    if pais_encontrado:
        print("Datos del país:")
        print(f"País: {pais_encontrado.pais}")
        print(f"Capital: {pais_encontrado.capital}")
        print(f"Población: {pais_encontrado.poblacion}")
        print(f"Área (en km²): {pais_encontrado.area}")
        print(f"Moneda: {pais_encontrado.moneda}")
        print(f"Idioma: {pais_encontrado.idioma}")



# LISTO
