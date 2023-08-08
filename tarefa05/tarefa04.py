lista_de_numoros = []
for i in range(10):
    numero = int(input("Qual numero vc escolhe seu maluco?: "))
    lista_de_numoros.append(numero)
    
listafinal = [i for i in lista_de_numoros if i > 0]

print(sorted(listafinal))
print("o maior valor e:",max(listafinal))
print("o menor valor e:",min(listafinal))