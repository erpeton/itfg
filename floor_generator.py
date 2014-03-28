import sys, pygame
from pygame.locals import *

fps = 30

gray     = (100, 100, 100)
navyblue = ( 60,  60, 100)
white    = (255, 255, 255)

seed        = 9639
begin_floor = 0
end_floor   = 170
moverate    = 10

def main():
    global fps_clock, display_surface, basic_font

    pygame.init()
    fps_clock = pygame.time.Clock()
    display_surface = pygame.display.set_mode((640, 480))
    basic_font = pygame.font.Font('freesansbold.ttf', 12)
    pygame.display.set_caption('Floor generator')

    camera      = begin_floor*80
    moveUp      = False
    moveDown    = False

    floors = generate_floors(seed,end_floor)

    while True:

        display_surface.fill(navyblue)

        pygame.draw.rect(display_surface, gray, (0, 0, 72, 480))
        pygame.draw.rect(display_surface, gray, (567, 0, 72, 480))

        for i in range(int((camera/80))-7, int((camera/80))+7):  
            pygame.draw.rect(display_surface, gray, (floors[i]['floor_start']*16, (430-i*80)+camera, floors[i]['length']*16, 30))
            textSurf = basic_font.render(str(i), True, white)
            textRect = textSurf.get_rect()
            textRect.center = (floors[i]['floor_start']*16)+(floors[i]['length']*16)/2, (430-i*80)+camera+30/2
            display_surface.blit(textSurf, textRect)

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    moveDown = False
                    moveUp = True
                elif event.key == K_DOWN:
                    moveUp = False
                    moveDown = True
                elif event.key == K_SPACE:
                    moveUp = False
                    moveDown = False
                elif event.key == K_ESCAPE:
                    terminate()

        if moveUp and camera < (end_floor*80-410):
            camera += moverate
        if moveDown and camera > 0:
            camera -= moverate
            
        pygame.display.update()
        fps_clock.tick(fps)

def generate_floors(seed,end_floor):

    floors = []
    detail = {}

    for i in range(0,end_floor+7):
        if (i <= 1000 and i%50 == 0) or (i > 1000 and i%500 == 0):
            floor_start = 0
            floor_end   = 40
            length      = 39 #:P
        else:
            if i <= 240:
                seed   = seed * 214013 + 2531011
                value  = (seed >> 16) & 0x7FFF
                if i%30 == 0:
                    length1 = 6 + value%(9-i/30)
                    length2 = 6 + value%(10-i/30)
                    if length1 == length2:
                        length = length1
                    else:
                        length = length2
                else:
                    length = 6 + value%(9-i/30)
            elif i < 600:
                seed   = seed * 214013 + 2531011
                value  = (seed >> 16) & 0x7FFF
                length = 6
            elif i < 1000:
                length = 6
            elif i < 1500:
                length = 5
            elif i < 2000:
                length = 4
            elif i < 10000:
                length = 3
            else:
                length = 2

            seed   = seed * 214013 + 2531011
            value  = (seed >> 16) & 0x7FFF
            floor_start = 5 + value%(30-length)
            floor_end   = floor_start + length


        detail['floor_start'] = floor_start
        detail['length'] = length+1
        floors.append(detail.copy())
    
    return floors

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
