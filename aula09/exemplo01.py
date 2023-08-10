#ler a divisão entre dois numeros
try:
    n1 = float(input("Qual o primeiro valor que vc deseja que seja lido?: "))
    n2 = float(input("Qual o segundo valor que vc deseja que seja lido?: "))
    print(f"o resultado do valor da divisãio e {n1/n2:.2f}")
except ValueError:
    print("E pra digitar um numero seu burro")    
except ZeroDivisionError:
    print("houe um problema de divisão.......")