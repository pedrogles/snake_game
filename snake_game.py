import pygame
from pygame.display import list_modes
from pygame.draw import circle
from pygame.locals import *
from sys import exit
from random import randint

pygame.init() # Inicializar todas funções e variaveis da biblioteca.
background_music = pygame.mixer.music.load("Dee Yan-Key - Grave.mp3") # Musica de fundo.
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
collision = pygame.mixer.Sound("salamisound-6336713-impact-on-iron-flip-against.wav") # Som de colisão.
collision.set_volume(0.03)
width,height = 640, 480 # Largura/altura da tela.
width_snake, height_snake = 20,20 # Altura e Largura da Cobra.
x_snake,y_snake = int(width/2), int(height/2) # Posiciona a Cobra no centro da tela.

speed = 10 # Velocidade de movimentação

x_control, y_control = speed, 0

x_apple,y_apple = randint(40, 600), randint(50, 430) # Gera um local aleatorio dentro da tela do jogo para bola branca.

watch = pygame.time.Clock() # Objeto para definir a taxa de frames/s
screen = pygame.display.set_mode((width,height)) # Variavel que cria a altura e largura da tela.
pygame.display.set_caption("Snake Game.") # Nome que aparece na janela da aplicação.

# Formatação da fonte, tamanho e estilo da fonte.
font = pygame.font.SysFont('sans-serif', 40, True,True)

point = 0
list_snake = []
len_snake = 5
die = False
def snake_tail(list_snake): 
    for xey in list_snake:
        pygame.draw.rect(screen, (0,255,0), (xey[0], xey[1], 20, 20))
def reset_game():
    global point, len_snake, x_snake, y_snake, list_snake, list_head, x_apple, y_apple, die
    point = 0
    len_snake = 5
    x_snake,y_snake = int(width/2), int(height/2) 
    list_snake = []
    list_head = []
    x_apple,y_apple = randint(40, 600), randint(50, 430)
    die = False

#Loop Principal.
while True:
    watch.tick(20) # Controla a taxa de frames/s
    screen.fill((255,255,255)) # Preenche a tela de acordo com a cor que você colocar.
    msg = f'Pontos: {point}'
    msg_format = font.render(msg, True,(0,0,0))
    for event in pygame.event.get(): # A cada interação checa se o evento ocorreu.
        if event.type == QUIT: # Fecha janela quando clicada em exit.
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control == speed:
                    pass
                else:
                    x_control = -speed
                    y_control = 0
            if event.key == K_d:
                if x_control == -speed:
                    pass
                else:    
                    x_control = speed
                    y_control = 0
            if event.key == K_w:
                if y_control == speed:
                    pass
                else:
                    y_control = -speed
                    x_control = 0
            if event.key == K_s:
                if y_control == -speed:
                    pass
                else:
                    y_control = speed
                    x_control = 0
    x_snake += x_control
    y_snake += y_control
    #Objetos(Cobra-maça)
    snake = pygame.draw.rect(screen, (0,255,0),(x_snake,y_snake, height_snake,width_snake))
    apple = pygame.draw.circle(screen,(255,0,0),(x_apple,y_apple),10)
    #Colisão de objetos.
    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        point += 1
        len_snake += 1
        collision.play()
    #Listas contendo rotas onde a cobra passou.
    list_head = []
    list_head.append(x_snake)
    list_head.append(y_snake)
    list_snake.append(list_head)
   # Processo de quando a cobra se morde.
    if list_snake.count(list_head) > 1: 
        msg2 = 'You ate your tail. Press R to restart.'
        text_format = font.render(msg2, True,(0,0,0)) 
        die = True
        while die:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reset_game()
            screen.blit(text_format, (50,200))
            pygame.display.update()
    # Quando a cobra encosta nas paredes, retorna do lado oposto.
    if x_snake > width:
        x_snake = 0
    if x_snake < 0:
        x_snake = width      
    if y_snake < 0:
        y_snake = height
    if y_snake > height:
        y_snake = 0
    # Se a lista for maior que o comprimento da cobra, deletar indice 0 da lista.
    if len(list_snake) > len_snake: 
        del list_snake[0]
    snake_tail(list_snake)
    screen.blit(msg_format,(450,20)) # Posiciona mensagem na tela.
    pygame.display.update() # A cada interação do loop principal essa função atualiza a tela.