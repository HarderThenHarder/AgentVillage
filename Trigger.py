from random import randint

from Entity.Architect.Architect import Architect
from Entity.Chef.Chef import Chef
from Entity.Farmer.Farmer import Farmer
from Entity.Sodier.Sodier import Soldier
from Vector2 import Vector2


class Trigger:

    @staticmethod
    def strike_random_event(world):
        pass

    @staticmethod
    def strike_add_people_event(main_tower, world):
        if main_tower.wood >= 250 and main_tower.mine >= 250:
            if randint(1, 100) == 1:
                # 30%-Architect  40%-Farmer  30%-Soldier
                random_occupation = randint(0, 100)
                if random_occupation <= 30:
                    x = randint(-50, 50)
                    y = randint(-50, 50)
                    random_location = main_tower.location + Vector2(x, y)
                    architect = Architect(world, world.image_class.architect_rb_img, random_location)
                    main_tower.add(architect)
                    architect.brain.set_state("free")
                    world.add(architect)
                elif random_occupation <= 70:
                    x = randint(-50, 50)
                    y = randint(-50, 50)
                    random_location = main_tower.location + Vector2(x, y)
                    farmer = Farmer(world, world.image_class.farmer_lb_img, random_location)
                    main_tower.add(farmer)
                    farmer.brain.set_state("goCutting")
                    world.add(farmer)
                elif random_occupation <= 90:
                    x = randint(-50, 50)
                    y = randint(-50, 50)
                    random_location = main_tower.location + Vector2(x, y)
                    soldier = Soldier(world, world.image_class.soldier_rb_img, random_location)
                    main_tower.add(soldier)
                    soldier.brain.set_state("patrol")
                    world.add(soldier)
                elif random_occupation <= 100:
                    x = randint(-50, 50)
                    y = randint(-50, 50)
                    random_location = main_tower.location + Vector2(x, y)
                    chef = Chef(world, world.image_class.chef_rb_img, random_location)
                    main_tower.add(chef)
                    chef.brain.set_state("patrol")
                    world.add(chef)

    @staticmethod
    def strike_hungry_people_event(main_tower, world):
        if main_tower.food == 0:
            if randint(1, 20) == 1:
                random_idx = randint(0, len(main_tower.people_list) - 1)
                dead_people = main_tower.people_list[random_idx]
                world.remove(dead_people.id)
                del main_tower.people_list[random_idx]

    @staticmethod
    def strike_remove_farmland_event(main_tower, world):
        if main_tower.food == 0:
            number_of_farm_land = 0
        else:
            number_of_farm_land = main_tower.food // 200 + 1
        actually_farm_land = main_tower.get_building_entity_number("planting")
        need_to_remove_number = int(actually_farm_land - number_of_farm_land)
        farmland_list = main_tower.get_building_entity_list("planting")
        for i in range(need_to_remove_number):
            farmland_to_remove = farmland_list[i]
            world.remove(farmland_to_remove.id)
            main_tower.building_list.remove(farmland_to_remove)

