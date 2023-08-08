valordoproduto = float(input("Qual o valor do seu produto meu lindo?: "))
valordesconto1 = valordoproduto - (5/100 * valordoproduto)
valordesconto2 = valordoproduto - (10/100 * valordoproduto)

if valordoproduto < 100:
    print(f"Você recebeu 5% de desconto, seu valor de desconto é igual a {valordesconto1}")
else:
    print(f"Você recebeu 10% de desconto, seu valor de desconto é igual a {valordesconto2}")
 