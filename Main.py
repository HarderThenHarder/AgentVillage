import pygame
from pygame.locals import *
from sys import exit
from pygame.time import Clock

from Entity.Farmer.Farmer import Farmer
from Entity.Flower import Flower
from Entity.Stone import Stone
from Entity.Forest import Forest
from Entity.Village import Village
from ImageClass import ImageClass
from Vector2 import Vector2
from World import World
from random import randint


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
    WIDTH_HEIGHT = [1536, 864]
    # WIDTH_HEIGHT = [1920, 1080]
    screen = pygame.display.set_mode(WIDTH_HEIGHT, RESIZABLE, 32)
    start_draw_pos = Vector2(0, 0)

    # Create world
    world = World(image_class.world_bg, WIDTH_HEIGHT, image_class)

    # Create Forest
    for i in range(100):
        x = randint(100, WHOLE_MAP_SIZE[0] - 100)
        y = randint(100, WHOLE_MAP_SIZE[1] - 100)
        random_location = Vector2(x, y)
        forest = Forest(world, image_class.forest_img, random_location)
        world.add(forest)

    # Create Stone
    for i in range(50):
        x = randint(100, WHOLE_MAP_SIZE[0] - 100)
        y = randint(100, WHOLE_MAP_SIZE[1] - 100)
        random_location = Vector2(x, y)
        stone = Stone(world, image_class.stone_img, random_location)
        world.add(stone)

    # Create Flower
    for i in range(20):
        x = randint(100, WHOLE_MAP_SIZE[0] - 100)
        y = randint(100, WHOLE_MAP_SIZE[1] - 100)
        random_location = Vector2(x, y)
        flower = Flower(world, image_class.flower_img, random_location)
        world.add(flower)

    # Create Berry
    for i in range(20):
        x = randint(100, WHOLE_MAP_SIZE[0] - 100)
        y = randint(100, WHOLE_MAP_SIZE[1] - 100)
        random_location = Vector2(x, y)
        berry = Flower(world, image_class.berry_img, random_location)
        world.add(berry)

    village = Village(world, image_class.village_img, Vector2(500, 500))
    world.add(village)

    # Create Farmer
    for i in range(10):
        x = randint(-50, 50)
        y = randint(-50, 50)
        random_location = village.location + Vector2(x, y)
        farmer = Farmer(world, image_class.farmer_lb_img, random_location, village)
        farmer.brain.set_state("goCutting")
        world.add(farmer)

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
