#leia dois valores e mostre a soma entre eles
a = float(input("indique o valor 1: "))
b = float(input("indique o valor 2: "))
ac = 0

if a == b:
    print("Seus numeros são iguais!!")
elif a <= b:
    while a <= b:
        ac += a
        a += 1
    print(f"A soma dos intervalos e igual a {ac}")
else:
    while b <= a:
        ac += b
        b +=1
    print(f"A somad dos intervalos e igual a {ac}")