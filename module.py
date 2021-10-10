def getColors(red):
    colors = ""
    for i in red:
        if i['type']=='estacion':
            if i['color'] in colors:
                pass
            else:
                colors += ' '+i['color']
        elif i['type']=='div':
            for j in i['ramif']:
                for k in j['ram']:
                    if (k['color'] in colors):
                        pass
                    else:
                        colors += ' '+k['color']
        
    return colors

def recorerRed(tren, red):
    for i in red:
        if i['type']=='div':
            div = {"name":i['name'], "rams":[]}
            tren['divs'].append(div)
            for j in i['ramif']:
                tren['divs'][len(tren['divs'])-1]['rams'].append({"name":j['name'],"value":0})

    #Recorre la red y las divisiones en la misma, sumando las estaciones obligatorias al path
    for i in red:
        if (i['type']=='estacion'):
            # Si el color de la estación y el tren son la misma se detiene
            if i['color'] == tren['color'] or i['color']=='none' or tren['color'] == 'none':
                tren['path'] += 1

        elif(i['type']=='div'):
            for j in i['ramif']:
                for k in j['ram']:
                    if k['color']!='none' and  k['color'] == tren['color'] or k['color']=='none':
                        for l in tren["divs"]:
                            for m in l['rams']:
                                if m['name'] == j['name']:
                                    m['value']+=1
                                    if m['value']>tren['max']:
                                        tren['max'] = m['value']
                    elif tren['color'] == 'none':
                        for l in tren["divs"]:
                            for m in l['rams']:
                                if m['name'] == j['name']:
                                    m['value']+=1
                                    if m['value']>tren['max']:
                                        tren['max'] = m['value']

    return(tren)

def buscarRuta(tren):
    count = 0
    for i in tren['divs']:
        count +=1
        maxi = tren['max']
        for j in i['rams']:
            if maxi > j['value']:
                maxi = j['value']
                tren['divs'][count-1]['rams'] = {"name":j['name'],"value":j['value']}
            elif maxi == j['value']:
                tren['divs'][count-1]['rams'] = {"name":"none","value":j['value']}
                j == len(i['rams'])+1

    return tren

def armarRes(tren):
    respuesta = ""
    for i in tren['divs']:
        respuesta += f"la ruta mas corta en la division {i['name']}, es la ramificacion {i['rams']['name']} con {i['rams']['value']} detenciones; "

    respuesta = f"Para el tren con color {tren['color']} "+respuesta+f" y la ruta obligatoria cuenta con {tren['path']} detenciones"
    respuesta = "# Resultado\n"+respuesta
    return respuesta


