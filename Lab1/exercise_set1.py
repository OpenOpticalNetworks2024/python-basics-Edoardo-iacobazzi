"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    value1 = float(input("inresisci un primo valore: "))
    value2 = float(input("inresisci un secondo valore: "))

    product = value1 * value2
    result = value1 + value2
    print(value1, value2)

    if product > 1000:
        print("la somma vale ", result)
    else:
        print("il prodotto vale ", product)

# ex2
def exercise2():
    start_value = int(input("inserisci un valore iniziale (intero): "))
    end_value = int(input("inserisci un valore finale (intero): "))

    vector = np.arange(start_value, end_value, 1)
    precedente = None

    print("Vettore:", vector)

    for element in vector:
        if precedente is not None:  # Verifica se c'è un valore precedente
            somma = element + precedente  # Somma dell'elemento corrente con il precedente
            print(element, "+", precedente, "=", somma)
        precedente = element  # Aggiorna il valore precedente con l'elemento corrente

# ex3
def exercise3():
    fine = 0
    lista1 = []
    lista2 = []

    print("LISTA 1")
    while fine == 0:
        new_element = input("inerisci un numero intero, scrivere -fine- per terminare: ")
        if new_element == "fine":  # per accettare i numeri in modo case insensitive
            fine = 1
        else:
            lista1.append(int(new_element))

    fine = 0

    print("LISTA 2")
    while fine == 0:
        new_element = input("inerisci un numero intero, scrivere -fine- per terminare: ")
        if new_element == "fine":  # per accettare i numeri in modo case insensitive
            fine = 1
        else:
            lista2.append(int(new_element))

    def controllo_lista(x):
        if len(x) > 0 and x[0] == x[len(x) - 1]:
            return True
        else:
            return False

    def divisione5(x):
        lista_int = []
        for element in x:
            if element % 5 == 0:
                lista_int.append(element)
        return lista_int

    def even_odd_check(x, y):
        third_list = []
        for element in x:
            if element % 2 == 0:
                third_list.append(element)
        for element in y:
            if element % 2 != 0:
                third_list.append(element)
        return third_list

    print(even_odd_check(lista1, lista2))
    print(controllo_lista(lista1))
    print(divisione5(lista1))


# ex4
def exercise4():
    pass


# ex5
def exercise5():
    stringa1 = "Emma is a good developer. emma is also a writer"
    stringa2 = "ops sono in mezzo"  # devo appenderla in mezzo alla frase
    frase = ""

    parole = stringa1.split()  # altrimenti itero su ogni carattere

    counter_emma = 0
    counter_parole = 0
    posizione_centrale = len(stringa1) // 2

    for element in parole:
        if element.lower() == "emma":
            counter_emma += 1

    posizione_spazio = stringa1.find(' ', posizione_centrale)
    frase = stringa1[:posizione_spazio] + stringa2 + stringa1[posizione_spazio:]

    print("emma compare: ", counter_emma, " volte")
    print(frase)


# ex6
def exercise6():
    pass


# ex7
def exercise7():
    stringa1 = "Emma is a good developer. emma is also a writer"
    stringa2 = "ops sono in mezzo"  # devo appenderla in mezzo alla frase
    frase = ""

    parole = stringa1.split()  # altrimenti itero su ogni carattere

    counter_emma = 0
    counter_parole = 0
    posizione_centrale = len(stringa1) // 2

    for element in parole:
        if element.lower() == "emma":
            counter_emma += 1

    posizione_spazio = stringa1.find(' ', posizione_centrale)
    frase = stringa1[:posizione_spazio] + stringa2 + stringa1[posizione_spazio:]

    print("emma compare: ", counter_emma, " volte")
    print(frase)


# ex8
def exercise8():
    frase8 = input("insersici una stringa: ")
    frase8_2 = input("insersici un'altra stringa: ")
    frase_new = ""
    counter = 0
    spazio = ' '

    lunghezza1 = len(frase8)
    lunghezza2 = len(frase8_2)

    for char in frase8 and frase8_2:
        if counter == 0:
            frase_new = frase_new + frase8[counter] + frase8_2[counter] + spazio
        if counter == lunghezza1 // 2:
            frase_new = frase_new + frase8[counter] + spazio
        if counter == lunghezza2 // 2:
            frase_new = frase_new + frase8_2[counter] + spazio
        if counter == lunghezza1 - 1:
            frase_new = frase_new + frase8[counter] + spazio
        if counter == lunghezza2 - 1:
            frase_new = frase_new + frase8_2[counter] + spazio
        counter += 1

    print("frase finale: ", frase_new)

# ex9
def exercise9():
    pass


# ex10
def exercise10():
    pass


# ex11
def exercise11():
    pass


# ex12
def exercise12():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 1")
    print("EX1")
    exercise1()
    #print(f"EX1{exercise1()}") deve esserci un return nella funzione però
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    exercise4()
    print("EX5")
    exercise5()
    print("EX6")
    exercise6()
    print("EX7")
    exercise7()
    print("EX8")
    exercise8()
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()
    print("EX11")
    exercise11()
    print("EX12")
    exercise12()
