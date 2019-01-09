from Entity.Building.House import House
from State import State
from random import randint
from Vector2 import Vector2


class ArchitectStateFree(State):

    def __init__(self, architect):
        State.__init__(self, "free")
        self.architect = architect

    def random_walk(self):
        x = randint(-50, 50)
        y = randint(-50, 50)
        self.architect.destination = self.architect.location + Vector2(x, y)

    def do_action(self):
        if abs(self.architect.location - self.architect.destination) < 5:
            if randint(1, 50) == 1:
                self.random_walk()
        # Set architect Walk Image
        if self.architect.location.get_xy()[0] < self.architect.destination.get_xy()[0]:
            if self.architect.location.get_xy()[1] < self.architect.destination.get_xy()[1]:
                self.architect.image = self.architect.world.image_class.architect_rb_img
            else:
                self.architect.image = self.architect.world.image_class.architect_ru_img
        else:
            if self.architect.location.get_xy()[1] <= self.architect.destination.get_xy()[1]:
                self.architect.image = self.architect.world.image_class.architect_lb_img
            else:
                self.architect.image = self.architect.world.image_class.architect_lu_img

    def check_condition(self):
        house_number = self.architect.main_tower.get_building_entity_number("house")
        # house capacity is 10, need 500 wood & 200 stone to build house
        if house_number * 10 < len(self.architect.main_tower.people_list) and self.architect.main_tower.wood >= 500 and self.architect.main_tower.mine >= 200:
            return "goBuilding"
        return None

    def entry_action(self):
        self.architect.speed = 30
        self.architect.destination = self.architect.location


class ArchitectStateGoBuilding(State):

    def __init__(self, architect):
        State.__init__(self, "goBuilding")
        self.architect = architect

    def check_condition(self):
        if abs(self.architect.location - self.architect.destination) < 10:
            return "building"
        return None

    def entry_action(self):
        while True:
            x_offset = randint(-self.architect.main_tower.territory_R, self.architect.main_tower.territory_R)
            y_offset = randint(-self.architect.main_tower.territory_R, self.architect.main_tower.territory_R)
            new_house_location = Vector2(x_offset, y_offset) + self.architect.main_tower.location
            for building in self.architect.main_tower.building_list:
                if building.is_over(new_house_location):
                    self.architect.main_tower.territory_R += 50
                    continue
            break
        new_house = House(self.architect.world, self.architect.world.image_class.house_unfinished_img, new_house_location)
        self.architect.main_tower.wood -= 500
        self.architect.main_tower.mine -= 200
        self.architect.world.add(new_house)
        self.architect.main_tower.add_building(new_house)
        self.architect.new_house = new_house
        self.architect.destination = new_house_location
        self.architect.speed = 50


class ArchitectStateBuilding(State):

    def __init__(self, architect):
        State.__init__(self, "building")
        self.architect = architect

    def do_action(self):
        self.architect.build_process += self.architect.time_passed / 1000

    def check_condition(self):
        if self.architect.build_process >= 10:
            return "free"
        return None

    def entry_action(self):
        self.architect.image = self.architect.world.image_class.architect_work_img
        self.architect.destination = self.architect.location

    def exit_action(self):
        self.architect.new_house.image = self.architect.world.image_class.house_img
        self.architect.new_house = None
