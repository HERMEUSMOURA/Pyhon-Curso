def aplicativoCompras():
    try:
        txt = open("dados_produtos.txt", "a+")
        nomeProduto = input("Qual o nome do seu produto?: ")
        
        if any(c.isdigit() for c in nomeProduto):
            raise Exception("O nome do produto não pode conter números.")
        
        precoProduto = float(input("Qual o preço do seu produto?: "))
        qt_compra = int(input("Qual a quantidade de produto comprado?: "))
        
        if not isinstance(precoProduto, (int, float)):
            raise Exception("isso aqui e um preço, nao a sua opinião.")
        
        if not isinstance(qt_compra, int):
            raise Exception("NIGUEM COMPRA NADA PELA METADE!!! so bolo.")
        
        if precoProduto <= 0:
            raise Exception("NADA DE PREÇO NEGATIVO!.")
        
        if qt_compra <= 0:
            raise Exception("VC TA QUERENDO FAZER UMA DOAÇÃO PRA LEVAR COISAS NEGATIVAS?.")
        
        txt.write(f"Nome do produto: {nomeProduto}\n - Preço do produto: R${precoProduto:.2f}\n - Quantidade Vendida: {qt_compra}\n\n")
        txt.close()
    except ValueError:
        print("Digite um valor válido.")
    except Exception as e:
        print(e)

aplicativoCompras()
