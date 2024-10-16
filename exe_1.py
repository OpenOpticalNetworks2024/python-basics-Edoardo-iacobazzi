import matplotlib.pyplot as plt
import numpy as np    #import di tutta la libreria

#quando chiamo per esempio array dalla libreira "np.array()"

############# ESERCIZIO 1 ############
print()
print("ESERCIZIO 1: ")
#value1 = float(input("inresisci un primo valore: "))
#value2 = float(input("inresisci un secondo valore: "))

value1 = 1
value2 = 2

product = value1 * value2
result = value1 + value2
print(value1, value2)

if product > 1000 :
    print("la somma vale " ,result)
else :
    print("il prodotto vale ", product)

############# ESERCIZIO 2 ############
print()
print("ESERCIZIO 2: ")

#start_value = int(input("inserisci un valore iniziale (intero): "))
#end_value = int(input("inserisci un valore finale (intero): "))

start_value = 100
end_value = 102

vector = np.arange(start_value,end_value,1)
precedente = None

print("Vettore:", vector)

for element in vector:
    if precedente is not None:  # Verifica se c'è un valore precedente
        somma = element + precedente  # Somma dell'elemento corrente con il precedente
        print(element, "+", precedente, "=", somma)
    precedente = element  # Aggiorna il valore precedente con l'elemento corrente

############# ESERCIZIO 3-4-6 ############
print()
print("ESERCIZIO 3: ")

fine = 0
lista1 = []
lista2 = []

print("LISTA 1")
while fine==0:
    new_element = input("inerisci un numero intero, scrivere -fine- per terminare: ")
    if new_element == "fine": #per accettare i numeri in modo case insensitive
        fine = 1
    else:
        lista1.append (int(new_element))

fine = 0

print("LISTA 2")
while fine==0:
    new_element = input("inerisci un numero intero, scrivere -fine- per terminare: ")
    if new_element == "fine": #per accettare i numeri in modo case insensitive
        fine = 1
    else:
        lista2.append (int(new_element))


def controllo_lista(x):
    if len(x)>0 and  x[0] == x[len(x)-1]:
        return True
    else:
        return False

def divisione5(x):
    lista_int= []
    for element in x :
        if element % 5 == 0:
            lista_int.append(element)
    return lista_int

def even_odd_check(x,y):
    third_list = []
    for element in x:
        if element % 2 == 0:
            third_list.append(element)
    for element in y:
        if element % 2 != 0:
            third_list.append(element)
    return third_list

print(even_odd_check(lista1,lista2))
print(controllo_lista(lista1))
print(divisione5(lista1))

############# ESERCIZIO 5-7 ############

stringa1 = "Emma is a good developer. emma is also a writer"
stringa2 = "ops sono in mezzo" #devo appenderla in mezzo alla frase
frase = ""

parole = stringa1.split()  #altrimenti itero su ogni carattere


counter_emma = 0
counter_parole = 0
posizione_centrale = len(stringa1)//2

for element in parole:
    if element.lower() == "emma":
        counter_emma += 1

posizione_spazio = stringa1.find(' ', posizione_centrale)
frase = stringa1[:posizione_spazio] + stringa2 + stringa1[posizione_spazio:]



print("emma compare: ",counter_emma, " volte")
print(frase)

############# ESERCIZIO 8 ############


babracadabra = 0
lololollo= 0

