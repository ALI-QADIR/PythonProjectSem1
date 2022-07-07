import pygame
import os

WIDTH, HEIGHT = 750, 400
FPS = 24
VEL = 4
FIRE_VEL = 12
SHIPSIZE = (100, 100)
WHITE = (255, 255, 255)
SHIP_IMAGE = pygame.image.load(os.path.join('assets', 'ship.png'))
BLASTERS = pygame.image.load(os.path.join('assets', 'blasters.png'))
SPEEDLINES_1 = pygame.Rect(600, 340, 2, 30)
BACKGROUND = pygame.image.load(os.path.join('assets', 'space.png'))
BACKG = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

appwindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Loading")

def draw_appwindow(model, fire):

    appwindow.fill(WHITE)
    appwindow.blit(BACKG, (0, 0))
    appwindow.blit(BLASTERS, (fire.x, fire.y))
    appwindow.blit(SHIP_IMAGE, (model.x, model.y))
    # pygame.draw.rect(appwindow, WHITE, SPEEDLINES_1)
    pygame.display.update()

def ship_movement(model):
    model.y -= VEL

def fire_movement(fire):
    fire.y -= FIRE_VEL

def main():
    
    FRAMES = pygame.time.Clock()
    run = True
    flag = True
    BLASTER_TICK = 0
    model = pygame.Rect(325, HEIGHT, SHIPSIZE[0], SHIPSIZE[1])
    fire = pygame.Rect(325, HEIGHT + 10, SHIPSIZE[0], SHIPSIZE[1])
    #model = pygame.Rect(590, 260, SHIPSIZE[0], SHIPSIZE[1])
    #fire = pygame.Rect(590, 270, SHIPSIZE[0], SHIPSIZE[1])
    while run:

        FRAMES.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

        ship_movement(model)
        if BLASTER_TICK % 3 == 0:

            fire_movement(fire)
        BLASTER_TICK += 1
        draw_appwindow(model, fire)
        if model.y + SHIPSIZE[1] < 0 and flag:
            break
        elif model.y + SHIPSIZE[1] < 0:
            model.y = HEIGHT
            fire.y = HEIGHT + 10

    pygame.quit()

if __name__ == '__main__':
    main()
