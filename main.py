#Aqui se encontrara el menu principal, donde se correrá el programa. 
#Se importaran las funciones de los otros modulos para llevar esto a cabo.

#Empezaremos importando

from modulo1_registro import database_paises, database_estados, database_datos_meterologicos
from modulo2_reportes import imprimir_ubicaciones_disponibles, mostrar_datos_pais

#Crearemos el menu.

while True:
    opcion=(input("""
Si desea salir del programa; ingrese [0]
                  
Si desea ver todas las ubicaciones disponibles en el sistema; ingrese [1]
                  
Si desea conocer los datos sobre las ubicaciones disponibles en el sistema; ingrese [2]
                  
-------->  """))
    
    if opcion.strip()=="0": 
      print("Fin del programa.")
      break 

#Mostrar ubicaciones: Al seleccionar esta opción, se deberán mostrar por consola todas las ubicaciones 
# disponibles en el sistema.

    elif opcion.strip()=="1":
      print("Las ubicaciones disponibles en el sistema son:")
      imprimir_ubicaciones_disponibles()

    if opcion.strip()=="2":
       mostrar_datos_pais()

    else:
    print('''Opción no válida. Ingrese unicamente "0", "1" o "2".''')

