try:
    txt = open("aula09/dados2.txt","r")
    print("Arquivo encontrado")
except ValueError:
    print("vc acessou o arquivo errado meu mano")