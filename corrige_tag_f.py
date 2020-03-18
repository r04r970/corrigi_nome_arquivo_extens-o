import os

try:
        nc = input('Digite N de caracteres de vai apagar no começo: ')
        for nome in os.listdir('.'):
                if nome != "corrige_tag_f.py":
                        novo_nome = nome[int(nc):]
                        os.rename(nome, novo_nome)
except:
        print("Somente numeros sao aceitos. Tente novamente.")
        exit(0)

nn = input('Digite o novo nome da tag: ')
for nome in os.listdir('.'):
        if nome != "corrige_tag_f.py":
                novo_nome = nn + nome
                os.rename(nome, novo_nome)

try:
        nc = input('Digite N de caracteres que vai apagar no final: ')
        ex = input('Digite a extensao do arquivo: ')
        for nome in os.listdir('.'):
                if nome != "corrige_tag_f.py":
                        novo_nome = nome[:-int(nc)] + '.' + ex
                        novo_nome = novo_nome.replace(' ','_')
                        novo_nome = novo_nome.replace('-','')
                        novo_nome = novo_nome.replace('__','_')
                        os.rename(nome, novo_nome)   
except:
        print("Somente numeros sao aceitos. Tente novamente.")
        exit(0)
