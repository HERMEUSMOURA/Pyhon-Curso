#trabalhar com estrutura de dados
dados = {}
print(type(dados))
#estrutura chave valor 0
alunos = {
    111:"karla da silva",
    222:"hello santos",
    333:"Manuel Gomes",
    444:"bruno mattos"
}
#mostrar primeiro item da tabela
print(alunos[111])
#mostrar somente as chaves do dicionario
print(alunos.keys())
#mostrar somente os valores armazenados no dicionario
print(alunos.values())
#mostrar todos os itens do dicionario
print(alunos.items())
#atualizar dicionario
alunos.update({555:"Paulo de Tarso"})
print(alunos)
alunos[666] = "teste"
print(alunos)
alunos[111] = "carlos silvana"
print(alunos)
#excluir um item de dicionario
alunos.pop(666)
print(alunos)
#mostrar somente os valores do dicionario
for i in alunos.values():
    print(i)
#mostrar somente as chaves do dicionario
for i in alunos.keys():
    print(i)
#mostrar todos os itens de um dicionario
for i in alunos.items():
    print(i)
    
for i,j in alunos.items():
    print(i,j,sep=" - ")

dados = {
    'lista_a':[1,2,2,5,8],
    'lista_b':[10,20,30,40],
    'lista_c':[100,200,300,400]
}
print(dados)
print(type(dados))
#mostrar o ultimo item da lista b
print(dados["lista_b"][-1])