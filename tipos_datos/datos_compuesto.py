# Conjunto de datos
# Un conjunto de datos es una colección de diferentes tipos de datos que pueden ser combinados en
# una sola estructura. En Python, los conjuntos de datos se pueden crear utilizando listas, tuplas o diccionarios.
lista = ["Fabian Rivera", 19, "Python", "Jugar futbol", "Dragon Ball Z", "Rapidos y Furiosos", 18, 20]
print("Lista de datos:", lista)
print("Tipo de dato de la lista:", type(lista))
# Acceso a elementos de la lista se empieza desde el 0
print("Primer elemento de la lista:", lista[0])
print("Último elemento de la lista:", lista[-1])
lista[1] = 20  # Modificar el segundo elemento de la lista
print("Lista modificada:", lista[0:2])  # Imprimir los dos primeros elementos de la lista

# La tupla es una colección de datos inmutable, es decir, no se puede modificar una vez creada.
tupla = ("Fabian Rivera", 19, "Python", "Jugar futbol", "Dragon Ball Z", "Rapidos y Furiosos", 18, 20)
print("Tupla de datos:", tupla)
print("Tipo de dato de la tupla:", type(tupla))
# Acceso a elementos de la tupla se empieza desde el 0
print("Primer elemento de la tupla:", tupla[0])
print("Último elemento de la tupla:", tupla[-1])
# La tupla no se puede modificar, por lo que no se puede cambiar el segundo elemento
# tupla[1] = 20  # Esto generaría un error, ya que las tuplas son inmutables
# Imprimir los dos primeros elementos de la tupla
print("Tupla 2 valores", tupla[0:2])  # Imprimir los dos primeros elementos de la tupla

# el conjunto es una colección de datos que no permite elementos duplicados y no tiene un orden específico y no se pueden modificar.
# Se puede reconstruir como una lista o tupla, pero no se puede acceder a los elementos por índice.
conjunto = {"Fabian Rivera", 19, "Python", "Jugar futbol", "Dragon Ball Z", "Rapidos y Furiosos", 18, 20}
print("Conjunto de datos:", conjunto)
print("Tipo de dato del conjunto:", type(conjunto))


# El diccionario es una colección de datos que almacena pares clave-valor. Cada elemento del diccionario 
# tiene una clave única que se utiliza para acceder al valor asociado.

diccionario = {    "nombre": "Fabian Rivera",
    "edad": 19,
    "lenguaje": "Python",
    "hobbies": "Jugar futbol",
    "anime_fav": "Dragon Ball Z",
    "serie_fav": "Rapidos y Furiosos",
    "nota1": 18,
    "nota2": 20
}

print("Diccionario de datos:", diccionario)
print("Tipo de dato del diccionario:", type(diccionario))
# Acceso a elementos del diccionario
print("Nombre:", diccionario["nombre"])
print("Edad:", diccionario["edad"])
print("Nota 1:", diccionario["nota1"] + 2)