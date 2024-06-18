#Escribe un algoritmo que genere una lista de números primos menores a 20.

primos = []
 
for num in range(2, 20):
    es_primo = True


    if num <= 1:
        es_primo = False

    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break


    if es_primo:
        primos.append(num)
 
print("Lista de números primos menores a 20:", primos)