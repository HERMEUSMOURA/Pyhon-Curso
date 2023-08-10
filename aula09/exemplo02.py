from logging import exception


x = 0
try:
    print(x)
except exception as e:
    print("Falha ao acessar a variavel")
    print(e)
else:
    print("parabens seu script funcionou 'corretamente'")
finally:
    print("Fim de tratamento de excessão")