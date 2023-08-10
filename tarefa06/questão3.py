def multiplação(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado
resultado = multiplação(2,3,4,5,6,7)
print("O resultado entre a multiplicação dos valores n e:", resultado)