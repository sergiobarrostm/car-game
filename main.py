import pygame
from random import randint

pygame.init()

#importando as imagens
bg = pygame.image.load('img/bg-road.png')
car1 = pygame.image.load("img/cars/car1.png")
car2 = pygame.image.load("img/cars/car2.png")
car3 = pygame.image.load("img/cars/car3.png")
car4 = pygame.image.load("img/cars/car4.png")
car5 = pygame.image.load("img/cars/car5.png")
car6 = pygame.image.load("img/cars/car6.png")
car7 = pygame.image.load("img/cars/car7.png")
car8 = pygame.image.load("img/cars/car8.png")
car_player = pygame.image.load("img/cars/car9.png")


cars = [car1, car2, car3, car4, car5,car6, car7, car8]


road_1 = cars[(randint(0, len(cars) -1))]
road_2 = cars[(randint(0, len(cars) -1))]
road_3 = cars[(randint(0, len(cars) -1))]

#posição inicial do carro principal
pos_x_car_main = 350
pos_y_car_main = 400

#posição inicial dos demais carros
pos_x_car1 = 180
pos_y_car1 = -1200
pos_x_car2 = 330
pos_y_car2 = -800
pos_x_car3 = 500
pos_y_car3 = -400
y = 0

speed = 15 #velocidade do carro principal
speed_cars = 10 #velocidade dos demais carros

#variaveis para marca o tempo
time=0
tempo_segundo=0

font=pygame.font.SysFont('arial black',20) #fonte da letra
texto=font.render("Tempo:  0",True,(255,255,255)) # cor
pos_texto=texto.get_rect()
pos_texto.center= 60,30 # posição do texto

screen = pygame.display.set_mode([800, 700])  # tamanho da tela em pixel
pygame.display.set_caption("Car Game")

game_open = True

while game_open:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_open = False

    key = pygame.key.get_pressed()

    # movimentar o carro para os lados
    if key[pygame.K_RIGHT] and pos_x_car_main<= 530:
        pos_x_car_main += speed
    if key[pygame.K_LEFT] and pos_x_car_main >= 170:
        pos_x_car_main -= speed

    # aparecer os carros aleatoriamente
    if ( (pos_y_car1 >= 700) and (pos_y_car2 >= 700) and (pos_y_car3 >= 700)):
        pos_y_car1 = randint(-3000, -2500)
        pos_y_car2 = randint(-2000, -1500)
        pos_y_car3 = randint(-1200, -400)

        road_1 = cars[(randint(0, len(cars) - 1))]
        road_2 = cars[(randint(0, len(cars) - 1))]
        road_3 = cars[(randint(0, len(cars) - 1))]

    #como atualizamos a tela a cada 50 milisegundos, multiplicmos x 20 para que se contabilize 1 segundo
    if (time<20):
        time+=1
    else: # quando passar de um segundo vai implementar em tempo_segundo
        tempo_segundo+=1
        texto = font.render("Tempo:  "+str(tempo_segundo), True, (255, 255, 255) )
        time=0


    if tempo_segundo == 15:
        speed_cars = 15
        speed = 20

    elif tempo_segundo == 30:
        speed_cars = 20
        speed = 25

    elif tempo_segundo == 45:
        speed_cars = 30
        speed = 35

    elif tempo_segundo == 60:
        speed_cars = 50
        speed = 40

    if ( y <= - 50 ):
        y = 0

    y -= speed

    pos_y_car1 += speed_cars
    pos_y_car2 += speed_cars + 2
    pos_y_car3 += speed_cars + 5

    # colocando a posição dos carros na tela
    screen.blit(bg, (0,y))
    screen.blit(car_player, (pos_x_car_main,pos_y_car_main))
    screen.blit(road_1, (pos_x_car1, pos_y_car1))
    screen.blit(road_2, (pos_x_car2, pos_y_car2))
    screen.blit(road_3, (pos_x_car3, pos_y_car3))
    screen.blit(texto,pos_texto)
    pygame.display.flip()

pygame.quit()