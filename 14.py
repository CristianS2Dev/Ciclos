#Escribe un algoritmo que alterne mayúsculas y minúsculas en una lista de strings.

palabras = ["Python","es","genial"]

letrasAlteradas = [palabra.upper() if i%2 == 0 else palabra.lower() for i, palabra in enumerate(palabras)]

print (f"Palabras con alternancia de mayusculas y minusculas {letrasAlteradas}")