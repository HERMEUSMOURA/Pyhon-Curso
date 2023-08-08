dias = float(input("informe o numero de dias: "))
horas = float(input("informe o numero de horas: "))
minutos = float(input("informe o numero de minutos: "))
segundos = float(input("informe o numero de segundos: "))
diasemsegundos = dias*86400
horasemsegundos = horas*60
minutosemsegundos = minutos*60
segundostotal = diasemsegundos+horasemsegundos+minutosemsegundos+segundos
print(f"seus dias em segundos e igual a {diasemsegundos}, seu numero de horas em segundos e igual a {horasemsegundos}, seu numero de minutos em segundos e igual a {minutosemsegundos} e vc tem {segundos} segundos, no total vc tem {segundostotal} segundos")