import random
import string

print("Deixe em branco para uma configuração padrão")
tamanho = input('Escolha o tamanho de caracteres da sua senha: ')

conteudo = input('Digite os caracteres especiais que sua senha vai possuir: ')

if not tamanho :
    tamanho = 16

if not conteudo:
    conteudo = "!@#$%¨&*()-=}{];/:"


chars = string.ascii_letters + string.digits + conteudo

rnd = random.SystemRandom()

print('-'*60)
print(''.join(rnd.choice(chars) for i in range(int(tamanho))))
print('-'*60)