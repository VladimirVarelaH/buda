import json
from module import recorerRed, buscarRuta, armarRes, getColors
from generate_json import generate_json

generate_json()

#Se extraen los valores del JSON con la red
archivo = open("ruta.JSON","r")
json_obj = ''
for i in archivo:
    string = str(i)
    json_obj += string

dict_obj = json.loads(json_obj)
red = dict_obj['red']

colors = getColors(red)
color = str(input(f'Ingrese el color del tren\nLos colores de la red son:\n{colors}\n'))

#Se configura el color del tren
flag = True
while flag:
    if color in colors:
        flag = False
    else:
        print('El color no está en la red')
        color = str(input(f'Ingrese un color de{colors}\n'))
tren = {
    'color': color,
    'path': 0,
    'max': 0,
}

tren = recorerRed(tren,red)
print('El tren recorrió la red, estas son los ramales:\n'+str(tren['divisiones'])+'\n')

tren = buscarRuta(tren)
print('El tren descartó las rutas más largas en cada punto de división:\n'+str(tren['divisiones'])+'\n')

res = armarRes(tren)
print('\n')
print(res)

archivo = open("resultado.md", "w")
archivo.write(res)


