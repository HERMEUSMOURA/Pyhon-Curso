#criar uma lista de notas
notas = [ 6,25,2,10,9,8,8,]
#valor maximo de uma nota de lista
print("maior valor: ",max(notas))
#valor minimo de uma nota de lista
print("menor valor: ",min(notas))
#quantidade de itens na lista de notas
print("quantidade de itens na lista de notas: ",len(notas))
#soma total das notas da lista
print("soma das notas: ",sum(notas))
#mostar media das notas da lista
print(f"media das notas e igual a: {sum(notas)/len(notas):.2f}")
#operador in
print(11 in notas)
#loop for com listas
for i in notas:
    print(i, end=" ")
#leia 5 notas utilizando lista e estruturas de repetrição
print("\n")
notas2 = []
for i in range(5):
    num = float(input("Qual a sua nota?: "))
    notas2.append(num)
print("todas as notas informadas: ", notas2)
print("quantidades de notas informas", notas2)
print("A soma das notas e:", sum(notas2))

l1 = [1,2,5]
l2 = l1
l2.append(100)
print(l1)


    