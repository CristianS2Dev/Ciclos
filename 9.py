#Escribe un algoritmo que intercale los elementos de dos listas de igual longitud.


lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
lista_intercalada = [None]*(len(lista1) + len(lista2))
lista_intercalada[0::2] = lista1
lista_intercalada[1::2] = lista2
print("Lista intercalada:", lista_intercalada)