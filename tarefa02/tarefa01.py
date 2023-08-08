valor1 = int(input("Qual o valor informado 1: "))
valor2 = int(input("Qual o valor informado 2: "))


if valor1 >= valor2:
    while valor1>=valor2:
        valor1 -= 1
        print(valor1, ned=" ")
else:
    while valor2>=valor1:
        valor2 -= 1
        print(valor2, end=" ")
