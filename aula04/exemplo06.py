#somar 3 valores positovos ou negativo informados pelo usuario
media = 0
cont = 1

while cont<=3:
    valor = float(input("Qual o valor da sua nota: "))
    if valor <= 0 or valor>10:
        continue 
    media += valor
    cont+=1
print(f"a soma das notas e {media}")
print(f"a sua media e igual a {media/3:.2f}")