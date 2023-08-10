#soma de n valores
def soma_coxinhas(*args):
    return sum(args)

def media_valores(*args):
    return sum(args)/len(args)

def valores(*args):
    return type(args)

def valores_teste(**kwargs):
    return type(kwargs)

if __name__ == '__main__':
    print(soma_coxinhas(6,10))
    print(soma_coxinhas(6,10,20))
    print(soma_coxinhas(6,10,5,8,9,4))
    print("==== media de n valores ====")
    print(media_valores(10,8,5))
    print(media_valores(10,10,10,10,10))
    print(media_valores(10,2,2))
    print(valores(5,6,9,8))
    print(valores_teste(idade=3,preco=6,qtd=9))