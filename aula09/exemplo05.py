try:
    txt =  open("aula09/dado s.txt","r")
    print("arquivo encontrado")
    txt.seek(0)
    print(txt.read)
except:
    print("seu arquivo ta errado meu nobre")