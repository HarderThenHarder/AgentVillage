import pygame
from pygame.locals import *
from sys import exit
from pygame.time import Clock
from Entity.Stone import Stone
from Entity.Forest import Forest
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
    world_bg = pygame.image.load(r"img\world2.jpg")
    forest_img = pygame.image.load(r"img\forest.png")
    forest_img = pygame.transform.scale(forest_img, (100, 60))
    stone_img = pygame.image.load(r"img\stone.png")
    stone_img = pygame.transform.scale(stone_img, (50, 50))

    # Constant Value
    ORIGIN = (0, 0)

    # set Screen
    WHOLE_MAP_SIZE = [9600, 5400]
    # WIDTH_HEIGHT = [1536, 864]
    WIDTH_HEIGHT = [1920, 1080]
    screen = pygame.display.set_mode(WIDTH_HEIGHT, RESIZABLE, 32)
    start_draw_pos = Vector2(0, 0)

    # Create world
    world = World(world_bg, WIDTH_HEIGHT)

    # tree = Tree(world, tree_img, Vector2(500, 300))
    # world.add(tree)
    # tree = Tree(world, tree_img, Vector2(490, 320))
    # world.add(tree)
    #
    # stone= Stone(world, stone_img, Vector2(540, 340))
    # world.add(stone)
    # stone = Stone(world, stone_img, Vector2(550, 360))
    # world.add(stone)

    for i in range(100):
        x = randint(100, WHOLE_MAP_SIZE[0] - 100)
        y = randint(100, WHOLE_MAP_SIZE[1] - 100)
        random_location = Vector2(x, y)
        forest = Forest(world, forest_img, random_location)
        world.add(forest)

    for i in range(100):
        x = randint(100, WHOLE_MAP_SIZE[0] - 100)
        y = randint(100, WHOLE_MAP_SIZE[1] - 100)
        random_location = Vector2(x, y)
        stone = Stone(world, stone_img, random_location)
        world.add(stone)

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

        world.process(start_draw_pos.get_xy())
        world.render(screen, start_draw_pos.get_xy())
        pygame.display.update()


if __name__ == '__main__':
    main()
