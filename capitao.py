import pygame
import random
import time
pygame.init()
import os
import time
geloSound = pygame.mixer.Sound("assets/acertoGelo.wav")
quedaSound = pygame.mixer.Sound("assets/letraCaindo.wav")
icone = pygame.image.load("assets/capitaoIcon.ico.png")
pygame.display.set_caption("Capitão América do Rian")
pygame.display.set_icon(icone)
largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/neve.png")
capitao = pygame.image.load("assets/capitão.png")
vogais = pygame.image.load("assets/vogais.png")
preto = (0, 0, 0)
branco = (255, 255, 255)
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
