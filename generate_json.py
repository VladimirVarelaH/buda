import json
def generate_json():
  red = [
      {"tipo":"estacion","estacion": "A", "color": "none"},
      {"tipo":"estacion","estacion": "B", "color": "none"},
      {"tipo":"estacion","estacion": "C", "color": "none"},
      {"tipo":"division","name":"split_1","ramificaciones": [{
        "tipo":"ramal", "name":"ram_1","estaciones":[
          {"tipo":"estacion","estacion": "D", "color": "none"},
          {"tipo":"estacion","estacion": "E", "color": "none"}
        ]
      },
      {
      "tipo":"ramal", "name":"ram_2","estaciones":[
        {"tipo":"estacion","estacion": "G", "color": "verde"},
        {"tipo":"estacion","estacion": "H", "color": "rojo"},
        {"tipo":"estacion","estacion": "I", "color": "verde"}
      ]
      }]
      },
      {"tipo":"estacion","estacion":"F", "color":"none"}

  ]

  res = {"red": red}
  json_object = json.dumps(res, indent = len(res["red"])) 
  archivo = open("ruta.json", "w")
  archivo.write(json_object)
