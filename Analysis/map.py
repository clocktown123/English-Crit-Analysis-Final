import pygame

brick = pygame.image.load('brick.png')
tree = pygame.image.load('tree.png')
street = pygame.image.load('street.png')
sign = pygame.image.load('Signs.png')
door = pygame.image.load('glass_door.png')
table = pygame.image.load('table.png')
table2 = pygame.image.load('table_5.png')
poster = pygame.image.load('fnaf_poster.png')
spot = pygame.image.load('spot.png')
spot2 = pygame.image.load('spot2.png')
side = pygame.image.load('side_walk.png')
parked1 = pygame.image.load('parked_car1.png')
parked2 = pygame.image.load('parked_car2.png')
parked3 = pygame.image.load('parked_car3.png')
parked4 = pygame.image.load('parked_car4.png')
parked5 = pygame.image.load('parked_car5.png')
floor = pygame.image.load('Movie_Floor4.png')


def MapF (screen, map):
    for i in range(20):
                for j in range(20):
                    if map[i][j] == 1:
                        screen.blit(tree, (j*50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 2:
                        screen.blit(brick, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 3:
                        screen.blit(sign, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 4:
                        screen.blit(door, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 5:
                        screen.blit(street, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 6:
                        screen.blit(table, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 7:
                        screen.blit(table2, (j *50, i * 50), (0, 0, 50, 50))
                    if map[i][j] == 8:
                         screen.blit(poster, (j*50, i*50), (0,0,50,50))
                    if map[i][j] == 9:
                         screen.blit(spot, (j*50, i*50), (0,0,50,50))
                    if map[i][j] == 10:
                         screen.blit(spot2, (j*50, i*50), (0,0,50,50))
                    if map[i][j] == 11:
                         screen.blit(side, (j*50, i*50), (0,0,50,50))
                    if map[i][j] == 12:
                         screen.blit(parked1, (j*50, i*50), (0,0,50,50))
                    if map[i][j] == 13:
                         screen.blit(parked2, (j*50, i*50), (0,0,50,50))
                    if map[i][j] == 14:
                         screen.blit(parked3, (j*50, i*50), (0,0,50,50))
                    if map[i][j] == 15:
                         screen.blit(parked4, (j*50, i*50), (0,0,50,50))
                    if map[i][j] == 16:
                         screen.blit(parked5, (j*50, i*50), (0,0,50,50))
                    if map[i][j] == 0:
                         screen.blit(floor, (j*50, i*50), (0,0,50,50))