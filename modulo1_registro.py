import json
import requests


database_paises = requests.get("https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-data-api.json").json()
#Aqui obtenemos la informacion de la API sobre los países. 
# De muchos paises obtenemos: País, Capital, Población, Area, Moneda, Idioma.
#print(database_paises) #Para verificar que se extrayeron correctamente los datos.

database_estados = requests.get("https://raw.githubusercontent.com/Andresarl16/API-Retos/main/location-states-api.json").json()
#Aqui obtenemos la informacion de la API sobre los estados.
# De muchos paises, obtenemos muchos estados y de cada estado obtenemos su: capital, poblacion, area. 
#print(database_estados) #Para verificar que se extrayeron correctamente los datos.

database_datos_meterologicos = requests.get('https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-api.json').json()
#Aqui obtenemos la informacion de la API sobre los datos meterologicos de cada pais (como en el reto #1)
#print(database_datos_meterologicos) #Para verificar que se extrayeron correctamente los datos.

#--------
# Almacenamiento de Datos Utilizando POO.

#Creamos el objeto pais.

class Pais:
    def __init__(self, pais, capital, poblacion, area, moneda, idioma ) -> None:
        """_summary_
        #Este método es el constructor de la clase Pais. 
        Args:
            pais (_type_): _description_
            capital (_type_): _description_
            poblacion (_type_): _description_
            area (_type_): _description_
            moneda (_type_): _description_
            idioma (_type_): _description_
        """
        self.pais = pais
        self.capital = capital
        self.poblacion = poblacion
        self.area = area
        self.moneda = moneda
        self.idioma = idioma

#Creo una lista de objetos donde almacenaré la informacion de cada país iterando la API.

pais_con_datos=[]
for diccionario_paises in database_paises:
    pais = diccionario_paises["location_name"]
    capital = diccionario_paises["location_capital"]
    poblacion = diccionario_paises["population"]
    area = diccionario_paises["area"]
    moneda = diccionario_paises["currency"]
    idioma = diccionario_paises["main_language"]
    pais_con_datos.append(Pais(diccionario_paises["location_name"], diccionario_paises["location_capital"],diccionario_paises["population"], diccionario_paises["area"], diccionario_paises["currency"], diccionario_paises["main_language"]))


