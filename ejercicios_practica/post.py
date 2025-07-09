'''
API Post [Python]
---------------------------
Autor: Ing.Jesús Matías González
Version: 1.0
 
Descripcion:
Se utiliza request para generar un HTTP post al servidor Flask
'''

__author__ = "Ing.Jesús Matías González"
__email__ = "ingjesusmrgonzalez@gmail.com"
__version__ = "1.0"

import requests

endpoint = 'registro'
url = f'http://127.0.0.1:5000/{endpoint}'

if __name__ == "__main__":
    try:
        name = str(input('Ingrese el nombre de la persona: '))
        age = int(input('Ingrese la edad: '))
        post_data = {"name": name, "age": age}
        x = requests.post(url, json=post_data)
        print('POST enviado a:', url)
        print('Datos:')
        print(post_data)
    except Exception as e:
        print('Error, POST no efectuado')
        print('Detalle del error:', e)
