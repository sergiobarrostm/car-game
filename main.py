import pygame
from random import randint

pygame.init()

#importando as imagens
bg = pygame.image.load('img/bg-road.png')
car_red = pygame.image.load("img/car_red.png")
car_green = pygame.image.load("img/car_green.png")
car_yellow = pygame.image.load("img/car_yellow.png")
car_white = pygame.image.load("img/car_white.png")

#posição inicial do carro principal
pos_x_car_main = 350
pos_y_car_main = 300

#posição inicial dos demais carros
pos_x_car1 = 170
pos_y_car1 = 500
pos_x_car2 = 330
pos_y_car2 = 500
pos_x_car3 = 520
pos_y_car3 = 500

speed = 10 #velocidade do carro principal
speed_cars = 12 #velocidade dos demais carros

screen = pygame.display.set_mode([800, 700])
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
    if ( (pos_y_car1 <= -500) and (pos_y_car2 <= -500) and (pos_y_car3 <= -500)):
        pos_y_car1 = randint(800,2000)
        pos_y_car2 = randint(800,2000)
        pos_y_car3 = randint(800,2000)

    pos_y_car1 -= speed_cars
    pos_y_car2 -= speed_cars + 2
    pos_y_car3 -= speed_cars + 10

    screen.blit(bg, (0,0))
    screen.blit(car_red, (pos_x_car_main,pos_y_car_main))
    screen.blit(car_yellow, (pos_x_car1, pos_y_car1))
    screen.blit(car_green, (pos_x_car2, pos_y_car2))
    screen.blit(car_white, (pos_x_car3, pos_y_car3))
    pygame.display.flip()

pygame.quit()