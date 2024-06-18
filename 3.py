#Escribe un algoritmo que encuentre los elementos comunes entre dos listas y los muestre.

my_list =  [1,2,3,4,5]

my_list2 = [4,5,6,7,8]

comunes = list(set(my_list) & set(my_list2))

print (f"Elementos comunes: {comunes}")