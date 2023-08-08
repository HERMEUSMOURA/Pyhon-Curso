#operações sobre lista () list compreention
lista = [10,20,5,50,100,6]
#criar uma nova lista com o dobro dos valores da lista anterior
lista2 = []
for i in lista:
    lista2.append(i*2)
print(lista2)
lista3 = [i*2 for i in lista]
print(lista3)
#criar uma nova lista com a metade dos valores da lista
lista4 = [i/2 for i in lista]
print(lista4)
#criar uma nova lista com os valores acima de 10, com base nas listas existentes
lista5 = [i for i in lista if i<10]
print(lista5)
#criar uma lista com valores pares baseados nas listas antigas
lista6 = [i for i in lista if i%2==0]
print(lista6)