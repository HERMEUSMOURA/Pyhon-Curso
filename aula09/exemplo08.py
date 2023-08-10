#ler um nome e email e armazenar no arquivo dados3.txt

try:
    txt = open("aula09/dados3.txt","a+",encoding='utf-8')
    nome = input("informe o nome:")
    email = input("informe o email: ")
    txt.write(f"{nome:^15} - {email:^15}\n")
except:
    print("error ao gravar os dados")