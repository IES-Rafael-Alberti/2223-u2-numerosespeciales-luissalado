# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def leernumero():
    try:
        numero = int(input("Introduzca un numero entero positivo: "))
        if numero > 0:
            return numero
        else:
            raise ValueError("Es un numero negativo.")
    except ValueError:
        print('Por favor, introduzca un número válido.')
        return leernumero()
    
num =leernumero()  

def  calcular_suma_pares_no_multiplos_de_3(num):
    for i in range(10,20):
        if i % 2 == 0:
            l
    

def calcular_suma_impares_no_multiplos_de_3(num):
    listaimpares =[]
    for i in range (10,20):
        if not i % 2 == 0:




    







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    

    #ENTRADA

    num = int(input("Introduzca un numero hasta poner 0:"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
