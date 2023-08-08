valor1 = 2
valor2 = 42.5

#operações aritmeticas
# print("soma:",valor1+valor2)
# print("mini:",valor1-valor2)
# print("div:",valor1/valor2)
# print("mute:",valor1*valor2)
print(f"divisão com 2 casas decimais: {valor1/valor2:.2f}")
print(f"valor 2: {valor2:.1f}")
#obter dados do teclado(entrada de dados)
# usuario = input("Informe o seu nome seu desgraçado:")
# print(f"seja bem vindo {usuario}")
# idade = int(input("me diga sua idade sujeito meliante:"))
# print(f"vc escapou de ser preso por ter a idade de: {idade}")
# print(f"sua idade no dobro e: {idade*2}")
#mostrar os tipo de dados das variantes
# print("idade: ",type(idade))
# print("usuario: ",type(usuario))
valor_curso = float(input("informe o valor do seu curso meu jovem: "))
print(f"o valor imformado do curso que vc quer fazer e {valor_curso}")
#mostrar mensagem coim 25% do valor do curso
#parabens!!! vc ganhou <valor> de credito na proxima compra
print(f"Parabens!!! vc ganhou 25% de desconto, seu novo valor a ser pago e de {25/100*valor_curso}")

parcelas = int(input("Qual a quantidade de parcelas que vc gostaria de fazer?: "))
print(f"ok, com o seu parcelamento, seu valor de {valor_curso} vai ser {valor_curso/parcelas} divido em {parcelas} parcelas")
