def aluno_boletim(nome,nota,dtCad):
    try:
        for i in range(5):
                dadosnota = float(input("Qual a sua nota?: "))
                soma = sum(dadosnota)
        txt = open("farefa07/dados.txt","a+",encoding='utf-8')
        nome = input("Qual o seu nome?: ")
        dtCad = dtCad.strtime('%d/%m/%Y')
        nota = soma
        txt.write(f"{nome:^15} - {nota/5} - {dtCad}\n")
    except:
        print("error ao gravar os dados!!!!")
print(aluno_boletim())