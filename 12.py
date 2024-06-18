#Escribe un algoritmo que filtre una lista de palabras y devuelva solo las palabras que contienen una subcadena específica.

palabras =["hola","Mundo","holanda","python","holístico"]

subcadena = "hol"

palabras_filtradas = [ palabra for palabra in palabras if subcadena in palabra]

print (f"Palabras que tienen {subcadena}: {palabras_filtradas}")