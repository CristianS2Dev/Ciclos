#Escribe un algoritmo que elimine los primeros N elementos de una lista.

my_list= [1,2,3,4,5,6,7,8]

N= int (input ("Después de que numero desea elminar: "))

my_list= my_list[N:]

print (f"Los numeros despues de eliminar los primeros {N} Elementos: {my_list}")