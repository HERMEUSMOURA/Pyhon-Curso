#leia 2 nomeros e mostre a contagem dos intervalos dos valores
valor1 = int(input("Qual o numero inicial?: "))
valor2 = int(input("Qual o valor final?: "))

if valor1 <= valor2:
    while valor1 <= valor2:
        print(valor1, end=" ")
        valor1 = valor1 + 1
else:
    while valor2 <= valor1:
        print(valor2, end=" ")
        valor2 = valor2 + 1