#estrutura de repetição while(continuação)
#leia 5 numeros e mostre a soma de todos os valores informados
cont=1
soma=0 #acumulador

while cont<=5:
    num = float(input("informe um valor: "))
    soma = soma+num
    cont+=1
print(f"Resultado da soma e {soma}")


