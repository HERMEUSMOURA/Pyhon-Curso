try:
    txt = open("aula09/dados2.txt","a+")
    for i in range(5):
        nome = input("informe o seu nome meu amigo: ")
        txt.write(f"Nome:{nome}\n")
except:
    print("nao foi possivel acessar o seu arquivo")
else:
    txt.close