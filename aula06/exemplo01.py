


lista = [2,8,10,4,55,'coxinha',34,'maionese',33]
print(type(lista))
print('primeiro item da lista',lista[0])
print('ultimo item da lista',lista[8])
print('ultimo item da lista',lista[-1])
print('penultimo item da lista',lista[-2])
print('quantidade de itens da lista', len(lista))
#print("lista ordenada",sorted(lista))
pc = ["mouse","monitor","hd","memoria ram","camera"]
print(sorted(pc))
lista2 = [6,8,4,11,55,0,3]
print(sorted(lista2))
#mostrar o intervalo da sita
print(lista2)
print(lista2[2:5])
print(lista2[3:])
print(lista2[4:])
#adicionar o item ao final da lista
lista2.append(1000)
print(lista2)
#inserir item em posição determinada da lista
lista2.insert(2,5000)
print(lista2)
#unir duas listas
lista2.extend(lista)
print(lista2)
#remover o ultimo item da lista
lista.pop()
print(lista2)
lista2.remove('coxinha')
print(lista2)
lista3 = pc
lista4 = pc.copy()
print("lista 3", lista3)
print("lista 4", lista4)
pc.append("SSD")
pc.append("teclado")
print(lista3)
lista3.append("placa de video")
print(lista4)
print(pc)