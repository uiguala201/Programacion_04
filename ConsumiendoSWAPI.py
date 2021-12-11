#*Urbano Iguala*
#*Consumiendo SWAPI*



import requests
import unittest
import swapi

from swapi.planets import (
    PlanetsQuerySet
)
from swapi.species import (
    SpeciesQuerySet
)
from swapi.startships import (
    StartshipsQuerySet
)
from swapi.utils import query
from swapi.exceptions import ResourceDoesNotExist
from swapi.settings import BASE_URL

class Swapi():

    def get_all(self):
        planets = swapi.get_all('planets')
        self.assertEquals(people.count(), 7)
        self.assertEquals('<PlanetsQuerySet - 7>', people.__repr__())
        species = swapi.get_all('species')
        self.assertEquals(species.count(), 7)
        self.assertEquals('<SpeciesQuerySet - 7>', species.__repr__())
        startships = swapi.get_all('starships')
        self.assertEquals(starships.count(), 7)
        self.assertEquals('<StarshipsQuerySet - 7>', species.__repr__())
     
     
Climaarido= []
Species= []
Startships= []

if __name__ == '__main__' :
    url='https://swapi.dev/api/'
    response = requests.get(url)
    if response.status_code == 200:
        
def principal():
    menu = """
Consumiendo SWAPI
a) En cuántas películas aparecen planetas cuyo clima sea árido?
b) ¿Cuántos Wookies aparecen en la sexta película?
c) ¿Cuál es el nombre de la aeronave más grande en toda la saga?

f) Salir
Elige: """
    elegido = ""
    while elegido != "f":
        eleccion = input(menu)
        if elegido == "a":
            Clima_Arido= 'https://swapi.dev/api/planets/?climate=%22arid%22'
            response = requests.get(Clima_Arido)
            if response.status_code == 200:
                for i in range (255):
                    response_json = response.json()
                    planets=response_json[i]
                    Climaarido.append(planets)
                    print Climaarido ()
        if elegido == "b":
            Wookies='https://swapi.dev/api/species/3/?films=%226%22'
            response = requests.get(Wookies)
            if response.status_code == 200:
                for i in range (255):
                    response_json = response.json()
                    species=response_json[i]
                    Species.append(species)
                    print Species ()
        if elegido == "c":
            Aeronave='https://swapi.dev/api/starships/?length'
            response = requests.get(Wookies)
            if response.status_code == 200:
                for i in range (255):
                    response_json = response.json()
                    startships=response_json[i]
                    Startships.append(startships)
                    print Startships ()



        
