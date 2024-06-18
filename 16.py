#Escribe un algoritmo que genere una lista de los primeros 10 números de Fibonacci
fibonacci = [0, 1]

for i in range(0, 11):

    siguiente = fibonacci[-1] + fibonacci[-2]

    fibonacci.append(siguiente) 

print("Lista de los primeros 10 números de Fibonacci:", fibonacci) 