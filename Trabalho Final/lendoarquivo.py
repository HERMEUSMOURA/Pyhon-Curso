def lendoArquivo():
    try:
        f = open("dados_produtos.txt","r")
        print(f.read())
    except Exception as e:
        print("Ate a proxima!!!")
        print(e)
lendoArquivo()