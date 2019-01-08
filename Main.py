import pygame
from pygame.locals import *
from sys import exit
from pygame.time import Clock
from Entity.AreaConfig import AreaConfig
from ImageClass import ImageClass
from Vector2 import Vector2
from World import World


def main():
    # init
    pygame.mixer.pre_init()
    pygame.init()
    pygame.display.set_caption("StoneAge v1.0")
    grab_flag = True
    pygame.event.set_grab(grab_flag)
    clock = Clock()

    # set Img
    image_class = ImageClass()

    # Constant Value
    ORIGIN = (0, 0)

    # set Screen
    WHOLE_MAP_SIZE = [9600, 5400]
    # WIDTH_HEIGHT = [1536, 864]
    WIDTH_HEIGHT = [1920, 1080]
    screen = pygame.display.set_mode(WIDTH_HEIGHT, RESIZABLE, 32)
    start_draw_pos = Vector2(0, 0)

    # Create world
    world = World(image_class.world_bg, WIDTH_HEIGHT, image_class)

    # Create area_config to init the world
    area_config = AreaConfig(world, WHOLE_MAP_SIZE, image_class)

    while True:
        time_passed = clock.tick(30)

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            if event.type == KEYDOWN:
                # press ESC to set mouse grab
                if event.key == K_ESCAPE:
                    grab_flag = not grab_flag
                    pygame.event.set_grab(grab_flag)

            if event.type == VIDEORESIZE:
                WIDTH_HEIGHT = event.size
                screen = pygame.display.set_mode(WIDTH_HEIGHT, RESIZABLE, 32)

        # Use Mouse To Move Map
        if pygame.mouse.get_pos()[0] <= 10:
            if start_draw_pos.x + 100 <= 0:
                start_draw_pos = start_draw_pos + Vector2(100, 0)
        elif pygame.mouse.get_pos()[0] >= WIDTH_HEIGHT[0] - 10:
            if start_draw_pos.x - 100 >= WIDTH_HEIGHT[0] - WHOLE_MAP_SIZE[0]:
                start_draw_pos = start_draw_pos - Vector2(100, 0)
        if pygame.mouse.get_pos()[1] <= 10:
            if start_draw_pos.y + 100 <= 0:
                start_draw_pos = start_draw_pos + Vector2(0, 100)
        elif pygame.mouse.get_pos()[1] >= WIDTH_HEIGHT[1] - 10:
            if start_draw_pos.y - 100 >= WIDTH_HEIGHT[1] - WHOLE_MAP_SIZE[1]:
                start_draw_pos = start_draw_pos - Vector2(0, 100)

        world.process(start_draw_pos.get_xy(), WIDTH_HEIGHT, time_passed)
        world.render(screen, start_draw_pos.get_xy())
        pygame.display.update()


if __name__ == '__main__':
    main()
