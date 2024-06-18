#Escribe un algoritmo que divida una lista en dos partes iguales. Si la lista tiene un número impar de elementos, la primera parte debe tener un elemento más que la segunda.

my_list= [1,2,3,4,5,6]

mitad = len(my_list)//2

if len(my_list) %2 !=0:
    mitad += 1
lista1 = my_list[:mitad]
lista2 = my_list[mitad:]

print (f"Primera parte {lista1}")
print (f"Segunda parte {lista2}")
