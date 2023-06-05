# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=15524

### File Handling ###

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("Intermediate/my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
print(txt_file.readlines()) # Te devuelve una lista con todo el contenido que hay dentro del fichero
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

# with open("Intermediate/my_file.txt", "a") as my_other_file:
#     my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt")

## Clase en vídeo (03/11/22): https://www.twitch.tv/videos/1642512950

## .json file

# import json


json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev"}

json.dump(json_test, json_file, indent=2) # Sirve para escribir el fichero json

json_file.close()

json_file=open("Intermediate/my_file.json", "r+")
print(json_file.read())
# prueba = json.load(json_file) no se porque esta linea da error y no deja ponerlo como diccionario si es lo mismo que abajo
# print(prueba)
json_file.close()

# with open("Intermediate/my_file.json") as my_other_file:
#     for line in my_other_file.readlines():
#         print(line)

json_dict = json.load(open("Intermediate/my_file.json")) # Esto lo que hace es leer el JSON y directamente te lo trae en formato diccionario OSEA ESTA FUNCION PARA HABRILO ES MUY BUENA 
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file


csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?
