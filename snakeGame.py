import pygame
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.load('the-final-boss-battle-158700.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

largura = 1000
altura = 600

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

x_controle = 10
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo")
lista_cobra = [(x_cobra, y_cobra)]
comprimento_inicial = 5
velocidade = 10

def aumenta_cobra(lista_cobra):
    for segmento in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (segmento[0], segmento[1], 20, 20))

def reiniciar_jogo():
    global comprimento_inicial,x_cobra,y_cobra,lista_cabeça,lista_cobra,x_maca,y_maca,morreu
    comprimento_inicial = 5
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeça = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

executando = True
direcao = 'RIGHT'  
while executando:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP] and direcao != 'DOWN':
        x_controle = 0
        y_controle = -10
        direcao = 'UP'
    if comandos[pygame.K_DOWN] and direcao != 'UP':
        x_controle = 0
        y_controle = 10
        direcao = 'DOWN'
    if comandos[pygame.K_RIGHT] and direcao != 'LEFT':
        x_controle = 10
        y_controle = 0
        direcao = 'RIGHT'
    if comandos[pygame.K_LEFT] and direcao != 'RIGHT':
        x_controle = -10
        y_controle = 0
        direcao = 'LEFT'

    x_cobra += x_controle
    y_cobra += y_controle

    tela.fill((255, 255, 255))  # Limpeza da tela

    ret_verde = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 40, 40))
    pygame.draw.circle(tela, (255, 0, 0), (x_maca, y_maca), 20)

    if ret_verde.colliderect(pygame.Rect(x_maca - 20, y_maca - 20, 40, 40)):
       x_maca = randint(40, 600)
       y_maca = randint(50, 430)
       comprimento_inicial += 1


    lista_cobra.append((x_cobra, y_cobra))
    aumenta_cobra(lista_cobra)

    lista_cabeça = []
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    lista_cobra.append(lista_cabeça)
    
    if lista_cobra.count(lista_cabeça)>1:
        fonte1 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Aperte R e reinicie o jogo'
        texto_formatado = fonte1.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:  
                   if event.key == pygame.K_r:
                       reiniciar_jogo() 
            ret_texto.center = (largura//2,altura//2)
            tela.blit(texto_formatado,ret_texto)           
            pygame.display.update()             

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    
    pygame.display.flip()

pygame.quit()





