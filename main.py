import json
from module import recorerRed, buscarRuta, armarRes, getColors


#Se extraen los valores del JSON con la red
archivo = open("ruta.JSON","r")
json_obj = ''
for i in archivo:
    string = str(i)
    json_obj += string

dict_obj = json.loads(json_obj)
red = dict_obj['red']

colors = getColors(red)
color = str(input(f'Ingrese el color del tren\nLos colores de la red son{colors}\n'))

#Se configura el color del tren
flag = True
while flag:
    if color in colors:
        flag = False
    else:
        print('El color no está en la red')
        color = str(input(f'Ingrese un color de{colors}\n'))
        print('\n')

tren = {
    'color': color,
    'path': 0,
    'max': 0,
    'divs': []
}

tren = recorerRed(tren,red)
print('\n')
print(tren)
tren = buscarRuta(tren)
print('\n')
print(tren)
res = armarRes(tren)
print('\n')
print(res)

archivo = open("resultado.md", "w")
archivo.write(res)


