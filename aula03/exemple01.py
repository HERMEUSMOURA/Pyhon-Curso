#estruturas de decisão(condicionais)
idadealuno = int(input("qual a sua idade meu nobre?: "))
if idadealuno < 3:
    print("idade invalida")
elif idadealuno <= 10:
    print("Sua categoria e infantil")
elif idadealuno <= 17:
    print("sua categoria e junior")
elif idadealuno <= 39:
    print("sua categoria e adulto")
elif idadealuno <= 130:
    print("sua categoria e senior")
else:
    print("Idade invalida ")