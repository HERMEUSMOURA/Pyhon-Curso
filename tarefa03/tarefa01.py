#leia uma quantidaded de notas determinada pelo usuario e faça a soma dos valores
notasX = []
nexus = int(input("qual a quantidade de numeros que vc escolhe?"))


for i in range(nexus):
    num = float(input("Qual a sua nota?: "))
    if num >= 0 and num <=10:
        notasX.append(num)
        num +=1
    else:
        continue        
print("a soma dos valores digitados pelo usuario: ", sum(notasX))