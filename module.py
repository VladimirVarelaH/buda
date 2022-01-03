def getColors(red):
    colors = ""
    for i in red:
        if i['tipo']=='estacion':
            if i['color'] in colors:
                pass
            else:
                colors += ' '+i['color']
        elif i['tipo']=='division':
            for j in i['ramificaciones']:
                for k in j['estaciones']:
                    if (k['color'] in colors):
                        pass
                    else:
                        colors += ' '+k['color']
        
    return colors

def recorerRed(tren, red):
    tren['divisiones'] = []
    #Crea los espacios para sumar las ramificaciones
    for i in red:
        if i['tipo']=='division':
            div = {"name":i['name'], "ramales":[]}
            #añade la division en la red al tren
            tren['divisiones'].append(div)
            for estacion in i['ramificaciones']:
                #añade los ramales de la división para sumar las detenciones
                tren['divisiones'][len(tren['divisiones'])-1]['ramales'].append({"name":estacion['name'],"value":0})

    #Recorre la red y las divisiones en la misma, sumando las estaciones obligatorias al path
    for i in red:
        if (i['tipo']=='estacion'):
            # Si el color de la estación y el tren son la misma se detiene
            # Si el tren no tiene color, se detiene
            # Si la estación no tiene color, se detiene
            if i['color'] == tren['color'] or i['color']=='none' or tren['color'] == 'none':
                tren['path'] += 1

        elif(i['tipo']=='division'):
            for ramal in i['ramificaciones']:
                for estacion in ramal['estaciones']:
                    if tren['color'] == 'none' or  estacion['color'] == tren['color'] or estacion['color']=='none':
                        #Se comprueba a qué ramal corresponde la parada y suma uno
                        for division in tren["divisiones"]:
                            for ramificacion in division['ramales']:
                                if ramificacion['name'] == ramal['name']:
                                    ramificacion['value']+=1
                                    #Se verifica si este ramal es el que tiene más detenciones, de ser así se establece como máximo
                                    if ramificacion['value']>tren['max']:
                                        tren['max'] = ramificacion['value']

    return(tren)

def buscarRuta(tren):
    count = 0
    for div in tren['divisiones']:
        count +=1
        maxi = tren['max']
        for j in div['ramales']:
            if maxi > j['value']:
                maxi = j['value']
                tren['divisiones'][count-1]['ramales'] = {"name":j['name'],"value":j['value']}
            elif maxi == j['value']:
                tren['divisiones'][count-1]['ramales'] = {"name":"none","value":j['value']}
                j == len(div['ramales'])+1

    return tren

def armarRes(tren):
    respuesta = ""
    for i in tren['divisiones']:
        respuesta += f"la ruta mas corta en la division {i['name']}, es la ramificacion {i['ramales']['name']} con {i['ramales']['value']} detenciones; "

    respuesta = f"Para el tren con color {tren['color']} "+respuesta+f" y la ruta obligatoria cuenta con {tren['path']} detenciones"
    respuesta = "# Resultado\n"+respuesta
    return respuesta


