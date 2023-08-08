faltas = int(input("Quantas faltas vc tem?: "))
mediafinal = float(input("Qual a sua media final?: "))

if faltas < 0:
    print("vc ta mentindo meu nobre, excluido do programa") 
elif faltas > 14 and mediafinal <7:
    print(f"vc ta ferrado meu nego, ta lascado, sua media final foi {mediafinal}  para passar e 7 e faltas foi {faltas}, para passar e menos que 14")
elif faltas < 14 and mediafinal >7:
    print(f"vc conseguiu meu heroi!!!!!! sua media final foi {mediafinal} e faltas foi {faltas}")
else:
    print("vc ta ferrado de um jeito ou de outro kkkkkkkkkkkkkkkkkkkkkk")