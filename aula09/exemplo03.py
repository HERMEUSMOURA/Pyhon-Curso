#ler a idade de eum funconario e tratar possiveis nuemros negatuivos ou valores acima de 130
idade = int(input("Qual a sua idade?: "))

if idade >= 130:
    raise ValueError("vc e velho demais")
elif idade <= 0:
    raise ValueError("Se vca nao nasceu, vc nao entra aqui")
else:
    print(idade)