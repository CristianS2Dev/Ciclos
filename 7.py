#Escribe un algoritmo que elimine todos los elementos negativos de una lista de números.

my_list =[1,-2,3,-4,5,-6]
lista2=[]
lista3=[]
for i in my_list:
    if i >= 0:
        lista2.append(i)
    elif i != 0:
        lista3.append(i)        
print (f"Los numeros negativos son:{lista3}")      
print(f"Lista sin elementos negativos: {lista2}")


