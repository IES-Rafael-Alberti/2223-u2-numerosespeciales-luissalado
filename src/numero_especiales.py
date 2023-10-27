# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def  calcular_suma_pares_no_multiplos_de_3():
    listapares=[]
    suma = 0
    for i in range(10,20):
        if i % 2 == 0:
            if i % 3 == 0:
                pass
            else:
                listapares.append(i)
                for j in len(listapares):
                    suma += j
        return suma
    

def calcular_suma_impares_no_multiplos_de_3():
    listaimpares =[]
    suma = 0
    for i in range (10,20):
        if not i % 2 == 0:
            if i % 3 == 0:
                pass
            else:
                listaimpares.append(i)
                for j  in len(listaimpares):
                    suma += j
        return suma

def mensaje():
    pares = calcular_suma_pares_no_multiplos_de_3
    impares = calcular_suma_impares_no_multiplos_de_3

    print("La suma de los pares es: ", pares)
    print("La suma de los impares es:", impares)


if __name__=="__main__":

    mensaje()
    







    






