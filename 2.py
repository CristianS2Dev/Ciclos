#Escribe un algoritmo que calcule el producto de todos los elementos impares de una lista de números enteros.
my_list=[1,2,3,4,5,6]
impares = 1
for i in my_list:
    if i %2 != 0:
       impares = impares *i
print (f"El producto de la lista es: {impares}")