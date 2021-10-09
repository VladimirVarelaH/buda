import json

red = [
    {"type":"estacion","estacion": "A", "color": "none"},
    {"type":"estacion","estacion": "B", "color": "none"},
    {"type":"estacion","estacion": "C", "color": "none"},
    {"type":"div","name":"ram_1","ramif": [{
      "type":"ram", "name":"ram_1_1","ram":[
        {"type":"estacion","estacion": "D", "color": "none"},
        {"type":"estacion","estacion": "E", "color": "none"}
      ]
    },
    {
    "type":"ram", "name":"ram_1_2","ram":[
      {"type":"estacion","estacion": "G", "color": "verde"},
      {"type":"estacion","estacion": "H", "color": "rojo"},
      {"type":"estacion","estacion": "I", "color": "verde"}
    ]
    }]
    },
    {"type":"estacion","estacion":"F", "color":"none"}

]

res = {"red": red}
json_object = json.dumps(res, indent = len(res["red"])) 
archivo = open("ruta.JSON", "w")
archivo.write(json_object)