import pygame
from random import randint

pygame.init()
pygame.mixer.init()  # inicializando sistema de audio


#importando as imagens
bg_road = pygame.image.load('img/bg_road.png')
car1 = pygame.image.load("img/cars/car1.png")
car2 = pygame.image.load("img/cars/car2.png")
car4 = pygame.image.load("img/cars/car3.png")
car5 = pygame.image.load("img/cars/car4.png")
car6 = pygame.image.load("img/cars/car5.png")
car7 = pygame.image.load("img/cars/car6.png")
car8 = pygame.image.load("img/cars/car7.png")
car_player = pygame.image.load("img/cars/car_player.png")

pygame.mixer.music.load("sons/music.mp3")
pygame.mixer.music.play(-1)

cars = {
    0: [car1, 89, 153],
    1: [car2, 92, 160],
    2: [car4, 95, 179],
    3: [car5, 85, 175],
    4: [car6, 103, 170],
    5: [car7, 80, 146],
    6: [car8, 103, 170],
}

road_1 = cars[(randint(0, len(cars) -1))]
road_2 = cars[(randint(0, len(cars) -1))]
road_3 = cars[(randint(0, len(cars) -1))]

#posição inicial do carro principal
pos_x_car_player = 360
pos_y_car_player = 450

#posição inicial dos demais carros
pos_x_car1 = 230
pos_y_car1 = -1200
pos_x_car2 = 350
pos_y_car2 = -800
pos_x_car3 = 480
pos_y_car3 = -400
y = 0

speed = 15 #velocidade do carro principal
speed_cars = 8 #velocidade dos demais carros

#variaveis para marca o tempo
time=0
tempo_segundo=0
score=0
bonus=0

#musica do jogo
#pygame.mixer.music.load('')

#tempo na tela
font=pygame.font.SysFont('arial black',20) #fonte da letra
texto=font.render("Tempo:  0",True,(255,255,255)) # cor
pos_texto=texto.get_rect()
pos_texto.center= 60,30 # posição do texto

# pontuação 'score'
texto1=font.render("score:  0",True,(255,255,255)) # cor
pos_texto1=texto1.get_rect()
pos_texto1.center= 60,60 # posição do texto

screen = pygame.display.set_mode([800, 700])  # tamanho da tela em pixel
pygame.display.set_caption("Car Game")
game_open = True
fps = pygame.time.Clock()

while game_open:
    fps.tick(30)

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_open = False

        if key[pygame.K_RIGHT] and pos_x_car_player < 480:
            pos_x_car_player += 120

        if key[pygame.K_LEFT] and pos_x_car_player > 240:
            pos_x_car_player -= 120

    # aparecer os carros aleatoriamente
    if (pos_y_car1 > 700):
        pos_y_car1 = randint(-3000, -2500)
        road_1 = cars[(randint(0, len(cars) - 1))]

    if (pos_y_car2 > 700) :
        pos_y_car2 = randint(-1200,-800)
        road_2 = cars[(randint(0, len(cars) - 1))]

    if (pos_y_car3 > 700):
        pos_y_car3 = randint(-5000,-3200)
        road_3 = cars[(randint(0, len(cars) - 1))]

    #como atualizamos a tela a cada 50 milisegundos, multiplicmos x 20 para que se contabilize 1 segundo
    if (time<30):
        time+=1
    else: # quando passar de um segundo vai implementar em tempo_segundo
        tempo_segundo+= + 1
        texto = font.render("Tempo:  "+str(tempo_segundo), True, (255, 255, 255) )
        time=0
        score= bonus+10*tempo_segundo
        texto1 = font.render("score:  " + str(score), True, (255, 255, 255))



    if tempo_segundo == 15:
        speed_cars = 15
        speed = 20
        bonus=100
    elif tempo_segundo == 30:
        speed_cars = 20
        speed = 25
        bonus=200
    elif tempo_segundo == 45:
        speed_cars = 30
        speed = 35
        bonus=300
    elif tempo_segundo == 60:
        speed_cars = 40
        speed = 50
        bonus=500

    if ( y <= - 50 ):
        y = 0

    y -= speed_cars

    pos_y_car1 += speed_cars
    pos_y_car2 += speed_cars + 2
    pos_y_car3 += speed_cars + 5

    # colocando a posição dos carros na tela
    screen.blit(bg_road, (0,y))

    # rect_car1 = pygame.draw.rect(screen, (255, 0, 0), (pos_x_car1, pos_y_car1, road_1[1], road_1[2]))
    # rect_car2 = pygame.draw.rect(screen, (255, 0, 0), (pos_x_car2, pos_y_car2, road_2[1], road_2[2]))
    # rect_car3 = pygame.draw.rect(screen, (255, 0, 0), (pos_x_car3, pos_y_car3, road_3[1], road_3[2]))
    # rect_car4 = pygame.draw.rect(screen, (0, 0, 255), (pos_x_car_player, pos_y_car_player, 85, 167))

    colisao_road1 = pygame.Rect(pos_x_car1, pos_y_car1, road_1[1], road_1[2])
    colisao_road2 = pygame.Rect(pos_x_car2, pos_y_car2, road_2[1], road_2[2])
    colisao_road3 = pygame.Rect(pos_x_car3, pos_y_car3, road_3[1], road_3[2])
    colisao_car_player = pygame.Rect(pos_x_car_player, pos_y_car_player, 85, 167)

    if colisao_car_player.colliderect(colisao_road1):
        print("colidiu 1")
    if colisao_car_player.colliderect(colisao_road2):
        print("colidiu 2")
    if colisao_car_player.colliderect(colisao_road3):
        print("colidiu 3")

    screen.blit(car_player, (pos_x_car_player,pos_y_car_player))
    screen.blit(road_1[0], (pos_x_car1, pos_y_car1))
    screen.blit(road_2[0], (pos_x_car2, pos_y_car2))
    screen.blit(road_3[0], (pos_x_car3, pos_y_car3))
    screen.blit(texto,pos_texto)
    screen.blit(texto1,pos_texto1)
    pygame.display.flip()

pygame.quit()