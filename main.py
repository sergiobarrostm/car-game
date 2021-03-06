import pygame
from random import randint

pygame.mixer.init()  # inicializando sistema de audio
pygame.init()

#importando as imagens
bg_game_menu = pygame.image.load('img/game_menu.png')
bg_road = pygame.image.load('img/bg_road.png')
bg_gamer_over = pygame.image.load('img/bg_gamerover.png')

#imagem do carros
car1 = pygame.image.load("img/cars/car1.png")
car2 = pygame.image.load("img/cars/car2.png")
car4 = pygame.image.load("img/cars/car3.png")
car5 = pygame.image.load("img/cars/car4.png")
car6 = pygame.image.load("img/cars/car5.png")
car7 = pygame.image.load("img/cars/car6.png")
car8 = pygame.image.load("img/cars/car7.png")
car_player = pygame.image.load("img/cars/car_player.png")

#imagem do bonus
score_100 =pygame.image.load("img/scores/score_100.png")
score_200 =pygame.image.load("img/scores/score_200.png")
score_300 =pygame.image.load("img/scores/score_300.png")
score_500 =pygame.image.load("img/scores/score_500.png")

#reproduzir a musica
pygame.mixer.music.load("sons/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

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

#variaveis do jogo
pos_x_car_player = 360
pos_y_car_player = 460
pos_x_car1 = 230
pos_y_car1 = -1200
pos_x_car2 = 350
pos_y_car2 = -800
pos_x_car3 = 480
pos_y_car3 = -400
y = 0
time = 0
tempo_segundo = 0
score=0
bonus=0
pontuacao = 10
speed_init = 15
speed_cars_init = 8
speed = speed_init
speed_cars = speed_cars_init

#tempo na tela
font=pygame.font.SysFont('arial black',20) #fonte da letra
font2=pygame.font.SysFont('arial black',48) #fonte da letra

text_time=font.render("Tempo:  0",True,(255,255,255)) # cor
pos_text_time=text_time.get_rect()
pos_text_time.center= 60,30 # posição do texto

# pontuação 'score'
text_score =font.render("score:  0",True,(255,255,255)) # cor
pos_text_score=text_score.get_rect()
pos_text_score.center= 60,60 # posição do texto

screen = pygame.display.set_mode([800, 700])  # tamanho da tela em pixel
pygame.display.set_caption("Car Game")
game_open = False
game_over = False
fps = pygame.time.Clock()

def change_speed(handle_tempo_segundo , handle_speed_cars , handle_speed, handle_bonus, bonus_img):
    global speed, speed_cars, bonus
    if tempo_segundo == handle_tempo_segundo:
        screen.blit(bonus_img, (110, 180))
        speed_cars = handle_speed_cars
        speed = handle_speed
        bonus = handle_bonus

while True:
    fps.tick(30)

    key = pygame.key.get_pressed()

    if game_open == False:
        screen.blit(bg_game_menu, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if key[pygame.K_SPACE]:
                game_open = True

    else:
        # colocando a posição dos carros na tela
        screen.blit(bg_road, (0,y))
        screen.blit(car_player, (pos_x_car_player,pos_y_car_player))
        screen.blit(road_1[0], (pos_x_car1, pos_y_car1))
        screen.blit(road_2[0], (pos_x_car2, pos_y_car2))
        screen.blit(road_3[0], (pos_x_car3, pos_y_car3))
        screen.blit(text_time,pos_text_time)
        screen.blit(text_score,pos_text_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if key[pygame.K_RIGHT] and pos_x_car_player < 480:
                pos_x_car_player += 120

            elif key[pygame.K_LEFT] and pos_x_car_player > 240:
                pos_x_car_player -= 120

        colisao_road1 = pygame.Rect(pos_x_car1, pos_y_car1, road_1[1], road_1[2])
        colisao_road2 = pygame.Rect(pos_x_car2, pos_y_car2, road_2[1], road_2[2])
        colisao_road3 = pygame.Rect(pos_x_car3, pos_y_car3, road_3[1], road_3[2])
        colisao_car_player = pygame.Rect(pos_x_car_player, pos_y_car_player, 85, 167)

        if colisao_car_player.colliderect(colisao_road1) or  colisao_car_player.colliderect(colisao_road2) or colisao_car_player.colliderect(colisao_road3):
            game_over = True

        if game_over:
            screen.blit(bg_gamer_over, (0, 0))
            text_score_total = font2.render("Score:  "+str(score), True, (255, 255, 255) )
            screen.blit(text_score_total, (250,170))

            if key[pygame.K_SPACE]:
                speed = speed_init
                speed_cars = speed_cars_init
                tempo_segundo = 0
                time = 0
                score = 0
                bonus = 0
                pos_y_car1 = -400
                pos_y_car2 = -1200
                pos_y_car3 = -800
                pos_x_car_player = 360
                game_over = False

        else:

            #como atualizamos a tela a cada 50 milisegundos, multiplicmos x 20 para que se contabilize 1 segundo
            if (time < 30):
                time+=1
            else: # quando passar de um segundo vai implementar em tempo_segundo
                tempo_segundo += 1
                time=0
                score += pontuacao
                if bonus != 0:
                    score += bonus
                    bonus = 0

                text_time = font.render("Tempo:  "+str(tempo_segundo), True, (255, 255, 255) )
                text_score = font.render("Score:  " + str(score), True, (255, 255, 255))

            if ( y <= - 50 ):
                y = 0
            y -= speed_cars
            pos_y_car1 += speed_cars
            pos_y_car2 += speed_cars
            pos_y_car3 += speed_cars

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

            change_speed(15, 12, 20, 100, score_100)
            change_speed(30, 15, 25, 200, score_200)
            change_speed(45, 25, 35, 300, score_300)
            change_speed(60, 35, 40, 500, score_500)

    pygame.display.flip()