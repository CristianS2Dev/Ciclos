#Escribe un algoritmo que ordene una lista de palabras por su longitud.

palabras = ["Python", "es", "un", "lenguaje","de","programacion"]

palabras_ordenadas = sorted(palabras,key=len)

print (f"Palabras ordenadas por longitud {palabras_ordenadas}")
 