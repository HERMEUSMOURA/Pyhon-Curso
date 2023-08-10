#funçôes com retorno
def soma_numeros(v1,v2):
    total = v1+v2
    return total
#função para calcular a media de 3 valores?
def media_tres(v1,v2,v3):
    return(v1+v2+v3)/3
    
#função para mostrar o maior valor a partir de dois valores
def uiui(v1,v2):
    return max(v1,v2)  

if __name__ =='__main__':
    print(uiui(20,10))
    print(soma_numeros(10,20))
#mostrar o dobro do resultado da função
    v1 = soma_numeros(100,300)
    print(v1*2)
    print(media_tres(10,9,8))
