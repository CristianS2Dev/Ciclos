import os
import math
i=True

while i:
    menu =int (input(f"""Ingrese el numero del ejercicio: 
                     1:
                     2:
                     3:
                     4:
                     5:
                     6:
                     7:
                     8:
                     9:
                     10:
                     11:
                     12:
                     13:
                     14:
                     15:
                     16:
                     17:
                     18:
                     19:
                     20:
                     Ingrese el numero del ejercicio que desea ver: """))



    if menu == 1:
        os.system("clear")
        my_list=[1,2,3,4,5,6]
        acumulador = 0
        for i in my_list:
            if i %2 == 0:
                acumulador = acumulador +i
        print (f"La suma de los pares es: {acumulador}")

    elif menu ==2:
        os.system("clear")
        my_list=[1,2,3,4,5,6]
        impares = 1
        for i in my_list:
            if i %2 != 0:
             impares = impares *i
        print (f"El producto de la lista es: {impares}")
    
    elif menu == 3:
        os.system("clear")
        my_list =  [1,2,3,4,5]

        my_list2 = [4,5,6,7,8]

        comunes = list(set(my_list) & set(my_list2))

        print (f"Elementos comunes: {comunes}")
    

    elif menu == 4:
        os.system("clear")
        my_list= [1,2,3,4,5,6,7,8]

        N= int (input ("Después de que numero desea elminar: "))

        my_list= my_list[N:]

        print (f"Los numeros despues de eliminar los primeros {N} Elementos: {my_list}")
    

    elif menu == 5: 
        os.system("clear")
        my_list = []

        for i in range (1, 11):
            cubos= i **3
            my_list.append(cubos)
            print (f"Lista de cubos: {my_list}")    

    elif menu == 6:
        os.system("clear")
        palabras = ["Python", "es", "un", "lenguaje","de","programacion"]

        palabras_ordenadas = sorted(palabras,key=len)

        print (f"Palabras ordenadas por longitud {palabras_ordenadas}")
    
    elif menu == 7:
        os.system("clear")
        my_list =[1,-2,3,-4,5,-6]
        lista2=[]
        for i in my_list:
            if i >= 0:
                lista2.append(i)
        print(f"Lista sin elementos negativos: {lista2}")
    
    elif menu == 8:
        os.system("clear")
        my_list=[1,2,3,4,5]
        my_list.sort()
        print(f"El numero segundo mayor de la lista es: {my_list[-2]}")

    elif menu == 9:
        os.system("clear")
        lista1 = [1, 3, 5]
        lista2 = [2, 4, 6]
        lista_intercalada = [None]*(len(lista1) + len(lista2))
        lista_intercalada[::2] = lista1
        lista_intercalada[1::2] = lista2
        print("Lista intercalada:", lista_intercalada)
    
    elif menu == 10:
        os.system("clear")
        my_list= [1,2,3,4,5,6]

        mitad = len(my_list)//2

        if len(my_list) %2 !=0:
            mitad += 1
        lista1 = my_list[:mitad]
        lista2 = my_list[mitad:]

        print (f"Primera parte {lista1}")
        print (f"Segunda parte {lista2}")
    
    elif menu == 11:
        os.system("clear")
        
        factoriales = [math.factorial(i) for i in range(1,7)]

        print (f"los numeros factoriales son: {factoriales}")
    elif menu == 12:
        os.system("clear")
        palabras =["hola","Mundo","holanda","python","holístico"]

        subcadena = "hol"

        palabras_filtradas = [ palabra for palabra in palabras if subcadena in palabra]

        print (f"Palabras que tienen {subcadena}: {palabras_filtradas}")

