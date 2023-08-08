#calcular a soma dos valores de intervalo fechados das variaveis a e b(280)
a = 10
b = 25
ac = 0

while a <= b:
    print(a,end=" ")
    ac += a
    a += 1
print(f"O resultado final da soma dos intervalos e igual a {ac}")