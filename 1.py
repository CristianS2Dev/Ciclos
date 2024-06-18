my_list=[1,2,3,4,5,6]
acumulador = 0
for i in my_list:
    if i %2 == 0:
        acumulador = acumulador +i
print (f"La suma de los pares es: {acumulador}")