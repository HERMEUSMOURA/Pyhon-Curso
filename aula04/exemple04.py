#somar 5 valores positovos informados pelo usuario
soma = 0
cont = 1

while cont<=5:
    valor = float(input("Qual o valor que vc informa?: "))
    if valor < 0:
        continue
    soma += valor
    cont+=1
print(f"O resultado da soma e {soma}")