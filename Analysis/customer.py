import pygame
import random
import math
from pygame.math import Vector2
#from limitless import fireball


A = 0
D = 1
W = 2
S = 3

class Enemy:
    def __init__ (self):
        self.pos = Vector2(500,850)
        self.direction = D
        self.isAlive = True
        self.HP = 1000
    
    def die(self, ballx, bally, cleavex, cleavey, hollow):
        if math.sqrt((self.pos.x-ballx)**2 + (self.pos.y-bally)**2) <= 20:
            if hollow == True:
                self.HP -= 200
                if self.HP < 0:
                    self.isAlive = False
            else:
                self.HP -= 100
                if self.HP < 0:
                    self.isAlive = False
        if math.sqrt((self.pos.x-cleavex)**2 + (self.pos.y-cleavey)**2) <= 20:
            self.HP -= 100
            if self.HP < 0:
                self.isAlive = False

        
    
    def draw(self, screen):
        if self.isAlive == True:
            pygame.draw.rect(screen, (20, 20, 40), ( self.pos.x, self.pos.y, 30, 30))
    
    def spawn(self, ticker, more, av, less):
        if less == True:
            if self.isAlive == False:
                self.pos.x = 500
                self.pos.y = 850
                if ticker % 40 == 0:
                    self.isAlive = True
        elif more == True:
            if self.isAlive == False:
                self.pos.x = 500
                self.pos.y = 850
                if ticker % 500 == 0:
                    self.isAlive = True
        elif av == True:
            if self.isAlive == False:
                self.pos.x = 500
                self.pos.y = 850
                if ticker % 250 == 0:
                    self.isAlive = True


    def move(self, map, ticket):
        #if ticker % 40 == 0: #change this number to make him change direction less or more often
            #num = random.randrange(0, 4)
            #if num == 0:
                #self.direction = D
            #elif num == 1:
                #self.direction = A
            #elif num == 2:
                #self.direction = W
            #elif num == 3:
                #self.direction = S
        #check if the player is in the line of sight

        if ticket == False:
            if self.pos.y > 300:
                self.pos.y -=3
            elif self.pos.x > 405:
                self.pos.x -= 3
            else:
                print("hello?")
        if ticket == True:
            if self.pos.x < 700:
                self.pos.x += 3
            elif self.pos.y > 100:
                self.pos.y -= 3
            else:
                print("ty")
        #elif ticket == True:


        if self.direction == D and map[int((self.pos.y) / 50)][int((self.pos.x + 20) / 50)] == 2:
            self.direction = W
            self.pos.x -= 6
        if self.direction == A and map[int((self.pos.y) / 50)][int((self.pos.x - 20) / 50)] == 2:
            self.direction = S
            self.pos.x += 6
        if self.direction == S and map[int((self.pos.y + 20) / 50)][int((self.pos.x) / 50)] == 2:
            self.direction = A
            self.pos.y -= 6
        if self.direction == W and map[int((self.pos.y - 20) / 50)][int((self.pos.x) / 50)] == 2:
            self.direction = D
            self.pos.y += 6

        #if self.direction == D:
            #self.pos.x += 3
        #elif self.direction == A:
            #self.pos.x -= 3
        #elif self.direction == W:
            #self.pos.y -=3
        #elif self.direction == S:
            #self.pos.y +=3


#class Frog(Enemy):
    #def __init__(self):
        #Enemy.__init__(self)

    #def die(self, ballx, bally, cleavex, cleavey, hollow):
        #Enemy.die(self, ballx, bally, cleavex, cleavey, hollow)


    #def move(self, map, ticker, px, py):
        #Enemy.move(self, map, ticker, px, py)

    #def draw(self, screen): #for now
        #if self.isAlive == True:
            #pygame.draw.rect(screen, (20, 20, 40), ( self.pos.x, self.pos.y, 20, 20))


#class Normcurse(Enemy):
    #def __init__(self):
        #Enemy.__init__(self)

    #def die(self, ballx, bally, cleavex, cleavey, hollow):
        #Enemy.die(self, ballx, bally, cleavex, cleavey, hollow)


    #def move(self, map, ticker, px, py):
        #Enemy.move(self, map, ticker, px, py)

    #def draw(self, screen): #for now
        #if self.isAlive == True:
            #pygame.draw.rect(screen, (20, 20, 40), ( self.pos.x, self.pos.y, 20, 20))