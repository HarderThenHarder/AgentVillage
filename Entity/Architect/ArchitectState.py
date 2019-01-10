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
        random_destination = self.architect.location + Vector2(x, y)
        world_w, world_h = self.architect.world.WHOLE_MAP_SIZE
        # don't walk out of world
        if 0 < random_destination.x - 10 < world_w and 0 < random_destination.y < world_h - 10:
            self.architect.destination = random_destination

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
        if house_number * 10 < len(self.architect.main_tower.people_list) and self.architect.main_tower.wood >= 200 and self.architect.main_tower.mine >= 200:
            x_offset = randint(-self.architect.main_tower.territory_left, self.architect.main_tower.territory_right)
            y_offset = randint(-self.architect.main_tower.territory_bottom, self.architect.main_tower.territory_up)
            new_house_location = Vector2(x_offset, y_offset) + self.architect.main_tower.location
            # don't build house out of map
            if new_house_location.x < 75 or new_house_location.x > self.architect.world.WHOLE_MAP_SIZE[0] - 75 or \
                    new_house_location.y < 60 or new_house_location.y > self.architect.world.WHOLE_MAP_SIZE[1] - 60:
                return None
            # don't build house over other house
            for building in self.architect.main_tower.building_list:
                if building.is_over(new_house_location):
                    # expand territory
                    if self.architect.main_tower.location.x - self.architect.main_tower.territory_left - 50 > 0:
                        self.architect.main_tower.territory_left += 50
                    if self.architect.main_tower.location.x + self.architect.main_tower.territory_right + 50 < self.architect.world.WHOLE_MAP_SIZE[0]:
                        self.architect.main_tower.territory_right += 50
                    if self.architect.main_tower.location.y - self.architect.main_tower.territory_up - 50 > 0:
                        self.architect.main_tower.territory_up += 50
                    if self.architect.main_tower.location.y + self.architect.main_tower.territory_bottom + 50 < self.architect.world.WHOLE_MAP_SIZE[1]:
                        self.architect.main_tower.territory_bottom += 50
                    return None
            # random choose house image
            if randint(1, 10) <= 7:
                new_house = House(self.architect.world, self.architect.world.image_class.house_unfinished_img, new_house_location, 1)
            else:
                new_house = House(self.architect.world, self.architect.world.image_class.house2_unfinished_img, new_house_location, 2)
            self.architect.main_tower.wood -= 200
            self.architect.main_tower.mine -= 200
            self.architect.world.add(new_house)
            self.architect.main_tower.add_building(new_house)
            self.architect.new_house = new_house
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
        self.architect.destination = self.architect.new_house.location
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
        if self.architect.new_house.house_type == 1:
            self.architect.new_house.image = self.architect.world.image_class.house_img
        else:
            self.architect.new_house.image = self.architect.world.image_class.house2_img
        self.architect.new_house = None
        self.architect.build_process = 0
