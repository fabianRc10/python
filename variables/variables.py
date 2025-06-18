edad = 19
nombre = "Fabian"
apellido = "Rivera"
lenguaje = "Python"
hobbies = "Jugar futbol"
#concatenar variables con el operador +
animeFav = "Dragon Ball Z" + " " + "le gusta a" + " " + nombre
serie_fav = "Rapidos y Furiosos"
#concatenar variables con f-string
serieFav = f"Mi serie favorita es {serie_fav} y me gusta {hobbies} en mi tiempo libre"
nota1 = 18
nota2 = 20

promedio = (nota1 + nota2) / 2

print(animeFav)
print(serieFav)
# Imprimir variables con "f" string
print(f"El alumno {nombre} {apellido} su promedio es {promedio}")

# Operadores de pertenencia
print(f"¿{lenguaje} está en la lista de lenguajes? {'Python' in lenguaje}")
print(f"¿{animeFav} está en la lista de animes favoritos? {'Dragon Ball Z' not in animeFav}")