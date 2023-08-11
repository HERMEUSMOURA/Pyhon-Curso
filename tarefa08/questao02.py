import datetime
from time import time

def CursoDados():
    try:
        txt = open("dados2.txt","a+")
        nomeCurso = input("Qual o nome do seu curso?: ")
        cargaHoraria = int(input("Carga horaria: "))
        valorCurso = float(input("Qual o valor do seu curso?: "))
        txt.write(f"nome do curso: {nomeCurso} - Carga Horaria: {cargaHoraria} - Valor do Curso: {valorCurso}")
        txt.close()
    except Exception as e:
        print("erro!!!!!!!!!!!!!!!!!!!!!!")
        print(e)

CursoDados()