from random import randint

from State import State
from Vector2 import Vector2


class WolfStateHiding(State):

    def __init__(self, wolf):
        State.__init__(self, "hiding")
        self.wolf = wolf

    def check_condition(self):
        if randint(1, 1000) == 1:
            return "goAttacking"

    def entry_action(self):
        self.wolf.destination = self.wolf.location
        self.wolf.image = None
        # self.wolf.color = None


class WolfStateGoAttacking(State):

    def __init__(self, wolf):
        State.__init__(self, "goAttacking")
        self.wolf = wolf

    def do_action(self):
        # Set wolf Walk Image
        if self.wolf.location.get_xy()[0] < self.wolf.destination.get_xy()[0]:
            if self.wolf.location.get_xy()[1] < self.wolf.destination.get_xy()[1]:
                self.wolf.image = self.wolf.world.image_class.wolf_rb_img
            else:
                self.wolf.image = self.wolf.world.image_class.wolf_ru_img
        else:
            if self.wolf.location.get_xy()[1] < self.wolf.destination.get_xy()[1]:
                self.wolf.image = self.wolf.world.image_class.wolf_lb_img
            else:
                self.wolf.image = self.wolf.world.image_class.wolf_lu_img

    def check_condition(self):
        # walk in main_tower area
        distance_to_main_tower = abs(self.wolf.location - self.wolf.destination)
        if distance_to_main_tower < self.wolf.attack_main_tower.territory_up or \
           distance_to_main_tower < self.wolf.attack_main_tower.territory_bottom or \
           distance_to_main_tower < self.wolf.attack_main_tower.territory_left or \
           distance_to_main_tower < self.wolf.attack_main_tower.territory_right:
            return "attacking"

    def entry_action(self):
        self.wolf.speed = 50
        self.wolf.attack_main_tower = self.wolf.world.get_nearest_entity(self.wolf.location, "main_tower")
        self.wolf.destination = self.wolf.attack_main_tower.location


class WolfStateAttacking(State):

    def __init__(self, wolf):
        State.__init__(self, "attacking")
        self.wolf = wolf

    def do_action(self):
        # if target dead, choose another target
        if self.wolf.attack_people.id not in self.wolf.world.entity_group:
            self.wolf.attack_people = self.wolf.attack_main_tower.get_nearest_people(self.wolf.location)
            self.wolf.destination = self.wolf.attack_people.location
        # 1/10 probability to hit people
        elif abs(self.wolf.location - self.wolf.destination) < 5:
            if randint(1, 10) == 1:
                self.wolf.attack_people.bitten()
        # Set wolf Walk Image
        if self.wolf.location.get_xy()[0] < self.wolf.destination.get_xy()[0]:
            if self.wolf.location.get_xy()[1] < self.wolf.destination.get_xy()[1]:
                self.wolf.image = self.wolf.world.image_class.wolf_rb_img
            else:
                self.wolf.image = self.wolf.world.image_class.wolf_ru_img
        else:
            if self.wolf.location.get_xy()[1] < self.wolf.destination.get_xy()[1]:
                self.wolf.image = self.wolf.world.image_class.wolf_lb_img
            else:
                self.wolf.image = self.wolf.world.image_class.wolf_lu_img
        # update wolf destination
        self.wolf.destination = self.wolf.attack_people.location - Vector2(10, 10)

    def check_condition(self):
        # if self.wolf.attack_people is None:
        #     return "retreating"
        return None

    def entry_action(self):
        self.wolf.speed = 70
        self.wolf.attack_people = self.wolf.attack_main_tower.get_nearest_people(self.wolf.location)
        self.wolf.destination = self.wolf.attack_people.location - Vector2(10, 10)


class WolfStateRetreating(State):

    def __init__(self, wolf):
        State.__init__(self, "retreating")
        self.wolf = wolf

    def do_action(self):
        # Set wolf Walk Image
        if self.wolf.location.get_xy()[0] < self.wolf.destination.get_xy()[0]:
            if self.wolf.location.get_xy()[1] < self.wolf.destination.get_xy()[1]:
                self.wolf.image = self.wolf.world.image_class.wolf_rb_img
            else:
                self.wolf.image = self.wolf.world.image_class.wolf_ru_img
        else:
            if self.wolf.location.get_xy()[1] < self.wolf.destination.get_xy()[1]:
                self.wolf.image = self.wolf.world.image_class.wolf_lb_img
            else:
                self.wolf.image = self.wolf.world.image_class.wolf_lu_img

    def check_condition(self):
        if abs(self.wolf.location - self.wolf.destination) < 10:
            return "hiding"

    def entry_action(self):
        self.wolf.destination = self.wolf.forest.location
        self.wolf.speed = 30
