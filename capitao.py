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

def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()
def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf",50)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()
def dead(desvios):
    pygame.mixer.Sound.play(geloSound)
    pygame.mixer.music.stop()
    message_display("Você Morreu com "+str(desvios)+" desvios")

def escrevendoPlacar(desvios):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios:"+str(desvios), True, branco)
    display.blit(texto, (0, 0))
    
def jogo():
    pygame.mixer.music.load('assets/capitaoAmerica.mp3')
    pygame.mixer.music.play(-1)
    capitaoPosicaoX = largura * 0.25
    capitaoPosicaoY = altura * 0.5
    capitaoLargura = 160
    movimentoX = 0
    vogaisPosicaoX = largura * 0.45
    vogaisPosicaoY = -220
    vogaisLargura = 40
    vogaisAltura = 250
    vogaisVelocidade = 5

    desvios = 0

    while True:
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()  
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                movimentoX = 0
        display.fill(branco)  
        display.blit(fundo, (0, 0)) 
        capitaoPosicaoX = capitaoPosicaoX + movimentoX
        if capitaoPosicaoX < 0:
            capitaoPosicaoX = 0
        elif capitaoPosicaoX > 630:
            capitaoPosicaoX = 630
        display.blit(capitao, (capitaoPosicaoX, capitaoPosicaoY))
        display.blit(vogais, (vogaisPosicaoX, vogaisPosicaoY))
        vogaisPosicaoY = vogaisPosicaoY + vogaisVelocidade

        if vogaisPosicaoY > altura:
            pygame.mixer.Sound.play(quedaSound)
            vogaisPosicaoY = -220
            vogaisVelocidade += 1
            vogaisPosicaoX = random.randrange(0, largura-50)
            desvios = desvios + 1
        escrevendoPlacar(desvios)  
        if capitaoPosicaoY < vogaisPosicaoY + vogaisAltura:
            if capitaoPosicaoX < vogaisPosicaoX and capitaoPosicaoX+capitaoLargura > vogaisPosicaoX or vogaisPosicaoX+vogaisLargura > capitaoPosicaoX and vogaisPosicaoX+vogaisLargura < capitaoPosicaoX+capitaoLargura:
                dead(desvios)  
        pygame.display.update()
        fps.tick(60)
jogo()
print("Volte sempre....")
