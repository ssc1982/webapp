# codeing = utf-8

from pygame.locals import *
import pygame
import time
import random

class Plane(object):

    def __init__(self, x, y, screen, image_url):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image_url)
        self.bulletList = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
            if bullet.isOutOfBoundary():
                self.bulletList.remove(bullet)


class MyWarPlane(Plane):

    def __init__(self, screen):
        Plane.__init__(self, 180, 600, screen, "./feiji/hero1.png")

    def moveLeft(self):
        self.x -= 5

    def moveRight(self):
        self.x += 5

    def fire(self):
        self.bulletList.append(Bullet(self.screen, self.x, self.y))


class EnemyWarPlane(Plane):

    def __init__(self, screen):
        Plane.__init__(self, 0, 0, screen, "./feiji/enemy0.png")
        self.direction = "right"

    def moveRandom(self):

        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x > 430:
            self.direction = "left"
        elif self.x < 0:
            self.direction ="right"

    def fire(self):
        if random.randint(1, 100) == 25 or random.randint(1, 100) == 60:
            self.bulletList.append(EnemyBullet(self.screen, self.x, self.y))


class BaseBullet(object):
    def __init__(self, x, y , screen, image_url):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image_url)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class EnemyBullet(BaseBullet):

    def __init__(self, screen, x, y):
        BaseBullet.__init__(self, x + 20, y + 50, screen,"./feiji/bullet1.png")

    def move(self):
        self.y += 2

    def isOutOfBoundary(self):
        if self.y > 850:
            return True
        else:
            return False

class Bullet(BaseBullet):

    def __init__(self, screen, x, y):
        BaseBullet.__init__(self, x + 40, y - 50, screen, "./feiji/bullet.png")

    def move(self):
        self.y -= 5

    def isOutOfBoundary(self):
        if self.y < 0:
            return True
        else:
            return False

def keyBoardEventListener(myWarplane):
    # keyboard event listener
    for event in pygame.event.get():

        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                myWarplane.moveLeft()
            elif event.key == K_d or event.key == K_RIGHT:
                myWarplane.moveRight()
            elif event.key == K_SPACE:
                myWarplane.fire()

def main():
    # show background
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # load background picture
    background = pygame.image.load("./feiji/background.png")
    # load myWarplane picture
    myWarplane = MyWarPlane(screen)
    # load EnemyWarPlane
    enemyWarPlane = EnemyWarPlane(screen)

    while True:
        # nest the background picture
        screen.blit(background, (0, 0))
        # nest the myWarplane picture
        myWarplane.display()
        # listening for keyboard event
        keyBoardEventListener(myWarplane)
        # nest the myWarplane picture
        enemyWarPlane.display()
        # enemywaplan moves randomly
        enemyWarPlane.moveRandom()
        #
        enemyWarPlane.fire()
        # update the screen
        pygame.display.update()
        # wait for 0.01s
        time.sleep(0.01)

if __name__ == "__main__":
    main()
