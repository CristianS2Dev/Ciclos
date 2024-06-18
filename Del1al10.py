#Hacer un algoritmo que imprima del 1 al 10

for i in range(1,11):
    print(f"número: {i}")


# While 

i=1
while i <=10:
    print(f"Número: {i}") 
    i = i+1
print(f"i vale -{i}- fuera del ciclo")


# Listas

listas=[1,2,3,4,5,"a","b","c","d"]

for i in listas:
    print(i)   

# Menú


import os

os.system("clear")

mensaje=("Opcion 1\nOpcion 2\nOpcion 3\nSalir 4\n")

menu = True
while menu:
    print(mensaje)
    opc=int (input("Escoge una opción del 1 al 2: "))
    if opc ==1:
        os.system("clear")
        print("Se esta ejecutando la opcion 1")
    elif opc ==2:
        os.sysconf("clear")
        print("Se esta ejecutando la opcion 2")
    elif opc ==3:
        os.sysconf("clear")
        print("Se esta ejecutando la opcion 3")
    elif opc == 4:
        menu=False
print("Salir")