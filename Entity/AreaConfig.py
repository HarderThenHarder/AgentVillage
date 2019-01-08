from random import randint

from Entity.Building.House import House
from Entity.Building.MainTower import MainTower
from Entity.Farmer.Farmer import Farmer
from Entity.Flower import Flower
from Entity.Forest import Forest
from Entity.Sodier.Sodier import Soldier
from Entity.Stone import Stone
from Vector2 import Vector2


class AreaConfig:

    def __init__(self, world, WHOLE_MAP_SIZE, image_class):
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

        main_tower = MainTower(world, image_class.main_tower_img, Vector2(500, 500))
        world.add(main_tower)

        house = House(world, image_class.house_img, Vector2(600, 650))
        world.add(house)

        # Create Farmer
        for i in range(10):
            x = randint(-50, 50)
            y = randint(-50, 50)
            random_location = main_tower.location + Vector2(x, y)
            farmer = Farmer(world, image_class.farmer_lb_img, random_location)
            main_tower.add(farmer)
            farmer.brain.set_state("goCutting")
            world.add(farmer)

        # Create Soldier
        for i in range(5):
            x = randint(-50, 50)
            y = randint(-50, 50)
            random_location = main_tower.location + Vector2(x, y)
            soldier = Soldier(world, image_class.soldier_rb_img, random_location)
            main_tower.add(soldier)
            # farmer.brain.set_state("goCutting")
            world.add(soldier)
