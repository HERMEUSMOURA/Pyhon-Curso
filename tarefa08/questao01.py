import datetime

def boletimAluno():
    try:
        txt = open("dados.txt", "a+")
        name = input("Qual o seu nome meu amigo?: ")
        nota1 = int(input("Qual a sua primeira nota?: "))
        nota2 = int(input("Qual a sua segunda nota?: "))
        nota3 = int(input("Qual a sua terceira nota?: "))
        soma = nota1 + nota2 + nota3
        media = soma / 3
        dt_Cad = datetime.datetime.now()  
        txt.write(f"Nome: {name} - Média: {media:.2f} - Data de cadastro: {dt_Cad}\n")
        txt.close()  
    except Exception as e:
        print("Erro!!!!!!!!!!!")
        print(e)  

boletimAluno()
