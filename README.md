# Red de Metro

Al ejecutar el programa, el mismó modtrará el progreso en la consola, utilizando para esto datos de ejemplo. Si los datos de ejemplo se quieren modificar hay información más detallada en le sección de **Para personalizar la red**, presente más abajo.

## Funcionamiento general

1) EL programa inicia con una red, este es un objeto iterable (específicamente un array) que contiene diccionarios.
Estos diccionarios pueden representar uno de tres tipos de objetos:
* **Estaciones**: Puntos en la red en los que el tren puede parar o no.
* **Divisiones**: Puntos en los que la red se divide, en particular, son iterables que contienen *ramales*.
* **Ramales**: Son las rutas alternativas que el tren tendrá que cotejar para encontrar el camino más corto, son iterables que contienen *estaciones*.  
2) Luego de tener una red, el programa la recorre, para decirle al usuario entre qué colores debe elegir para su tren.  
El tren representa a un objeto que recorrerá la red almacenando información de cada ramificación, particularmente su nombre y la cantidad de estaciones en las que se detiene.  
3) El tren se detiene en una estación si cualquiera de las siguientes condiciones se cumplen.  
* Si el color de la estación y del tren coinciden.
* Si el color del tren el 'none'.
* Si el color de la estación es 'none'.
Al detenerse suma la estación a la ramificación correspondiente y, si no es parte de ninguna ramificación, suma la detención a su ruta obligatoria (o al `path` del tren).  
4) Al finalizar su recorrido, el tren compara cada ramal con los que se correspondan a su punto de división, es decir, si la red tuviera más de unpunto de ramificación, el tren compararía cada grupo de ramales como una ruta a parte.  
5) El programa escribe en consola la ruta más corta y crea un documento `resultado.md` en el que se puede ver la respuesta.

## Para personalizar la red
Si se quieiera, es posible modificar la red a recorrer, lo importante es seguir la convensión aquí explicada:
* Declarar una estación: La estación es de lo más sencillo, 
```python
	{"tipo":"estacion","estacion": "A", "color": "none"}
```
* Declarar una división: La división debe tener un nombre único y un iterable con nombre `ramificaciones`
```python
	{"tipo":"division","name":"split_1","ramificaciones": [/* Aquí van los ramales */]}
```
* Declarar un ramal: El ramal debe tener un nombre único y un iterable con nombre `estaciones`
```python
	{"tipo":"ramal","name":"ram_1","estaciones": [/* Aquí van las estaciones */]}
```
Así se puede ver que el programa utiliza el tipo del objeto para saber cómo tartarlo y el nombre para comparar las rutas, de ahí su importancia.  
El objeto de red final quedaría algo así:
```python
red = [
    {"tipo":"estacion","estacion": "A", "color": "none"},

    {"tipo":"division","name":"split_1","ramificaciones": [
        {"tipo":"ramal","name":"ram_1","estaciones": [
            {"tipo":"estacion","estacion": "B", "color": "none"}
        ]}
    ]},

    {"tipo":"estacion","estacion": "B", "color": "none"}
]
```
Si se quiere modificar la red, se puede hacer en el archivo `generate_json.py`, aunque el programa podría modificarse de manera sencilla para funcionar como una API.

## Testing
Para ejecutar las pruebas del código se debe ejecutar el comando `py -m doctest test.txt`, estando en la carpeta donde se encuentre el programa y teniendo Python instalado.  
Si el test es exitoso, no se verá ningún mensaje en la consola. Si por el contrario falla, aparecerá información sobre el error obtenido, la respuesta esperada y la obtenida.