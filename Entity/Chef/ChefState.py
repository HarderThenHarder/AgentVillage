from Entity.Plantings import Plantings
from State import State
from random import randint
from Vector2 import Vector2


class ChefStateFree(State):

    def __init__(self, chef):
        State.__init__(self, "free")
        self.chef = chef

    def random_walk(self):
        x = randint(-50, 50)
        y = randint(-50, 50)
        random_destination = self.chef.location + Vector2(x, y)
        world_w, world_h = self.chef.world.WHOLE_MAP_SIZE
        # don't walk out of world
        if 0 < random_destination.x - 10 < world_w and 0 < random_destination.y < world_h - 10:
            self.chef.destination = random_destination

    def do_action(self):
        if abs(self.chef.location - self.chef.destination) < 5:
            if randint(1, 50) == 1:
                self.random_walk()
        # Set chef Walk Image
        if self.chef.location.get_xy()[0] < self.chef.destination.get_xy()[0]:
            if self.chef.location.get_xy()[1] < self.chef.destination.get_xy()[1]:
                self.chef.image = self.chef.world.image_class.chef_rb_img
            else:
                self.chef.image = self.chef.world.image_class.chef_ru_img
        else:
            if self.chef.location.get_xy()[1] <= self.chef.destination.get_xy()[1]:
                self.chef.image = self.chef.world.image_class.chef_lb_img
            else:
                self.chef.image = self.chef.world.image_class.chef_lu_img

    def check_condition(self):
        # 10 people need one farmland
        farm_land_number = self.chef.main_tower.get_building_entity_number("planting")
        if farm_land_number < len(self.chef.main_tower.people_list) // 10:
            x_offset = randint(-self.chef.main_tower.territory_left, self.chef.main_tower.territory_right)
            y_offset = randint(-self.chef.main_tower.territory_bottom, self.chef.main_tower.territory_up)
            new_farmland_location = Vector2(x_offset, y_offset) + self.chef.main_tower.location
            # don't build house out of map
            if new_farmland_location.x < 75 or new_farmland_location.x > self.chef.world.WHOLE_MAP_SIZE[0] - 75 or \
                    new_farmland_location.y < 60 or new_farmland_location.y > self.chef.world.WHOLE_MAP_SIZE[1] - 60:
                return None
            # don't build house over other house
            for building in self.chef.main_tower.building_list:
                if building.is_over(new_farmland_location):
                    # expand territory
                    if self.chef.main_tower.location.x - self.chef.main_tower.territory_left - 50 > 0:
                        self.chef.main_tower.territory_left += 50
                    if self.chef.main_tower.location.x + self.chef.main_tower.territory_right + 50 < \
                            self.chef.world.WHOLE_MAP_SIZE[0]:
                        self.chef.main_tower.territory_right += 50
                    if self.chef.main_tower.location.y - self.chef.main_tower.territory_up - 50 > 0:
                        self.chef.main_tower.territory_up += 50
                    if self.chef.main_tower.location.y + self.chef.main_tower.territory_bottom + 50 < \
                            self.chef.world.WHOLE_MAP_SIZE[1]:
                        self.chef.main_tower.territory_bottom += 50
                    return None
            if randint(1, 10) <= 7:
                new_farmland = Plantings(self.chef.world, self.chef.world.image_class.wheats_unfinished_img, new_farmland_location, 1)
            else:
                new_farmland = Plantings(self.chef.world, self.chef.world.image_class.carrots_unfinished_img, new_farmland_location, 2)
            self.chef.world.add(new_farmland)
            self.chef.new_farmland = new_farmland
            return "goPlanting"
        return None

    def entry_action(self):
        self.chef.speed = 30
        self.chef.destination = self.chef.location


class ChefStateGoPlanting(State):
    
    def __init__(self, chef):
        State.__init__(self, "goPlanting")
        self.chef = chef

    def do_action(self):
        if self.chef.location.get_xy()[0] < self.chef.destination.get_xy()[0]:
            if self.chef.location.get_xy()[1] < self.chef.destination.get_xy()[1]:
                self.chef.image = self.chef.world.image_class.chef_rb_img
            else:
                self.chef.image = self.chef.world.image_class.chef_ru_img
        else:
            if self.chef.location.get_xy()[1] <= self.chef.destination.get_xy()[1]:
                self.chef.image = self.chef.world.image_class.chef_lb_img
            else:
                self.chef.image = self.chef.world.image_class.chef_lu_img
        
    def check_condition(self):
        if abs(self.chef.location - self.chef.destination) < 10:
            return "planting"
        return None

    def entry_action(self):
        self.chef.destination = self.chef.new_farmland.location
        self.chef.speed = 50


class ChefStatePlanting(State):

    def __init__(self, chef):
        State.__init__(self, "planting")
        self.chef = chef

    def do_action(self):
        self.chef.build_process += self.chef.time_passed / 1000

    def check_condition(self):
        if self.chef.build_process >= 10:
            return "free"
        return None

    def entry_action(self):
        self.chef.image = self.chef.world.image_class.chef_work_img
        self.chef.destination = self.chef.location

    def exit_action(self):
        if self.chef.new_farmland.plant_type == 1:
            self.chef.new_farmland.image = self.chef.world.image_class.wheats_img
        else:
            self.chef.new_farmland.image = self.chef.world.image_class.carrots_img
        self.chef.main_tower.add_building(self.chef.new_farmland)
        self.chef.main_tower.food += self.chef.new_farmland.food
        self.chef.new_farmland = None
        self.chef.build_process = 0
