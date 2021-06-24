import os
import time
def LimparTela():
    os.system("cls")
    return

nome = input(' Qual o seu nome? ')
email = input(' Qual o seu e-mail') 

archive= open('records.txt', 'w')
archive.write("\n seu nome: " + nome)
archive.write("\n seu email: " + email)
archive.close()
archive = open('records.txt', 'r')
print(archive.read)
archive.close()
LimparTela()