from State import State
from random import randint
from Vector2 import Vector2


class SoldierStatePatrol(State):

    def __init__(self, soldier):
        State.__init__(self, "patrol")
        self.soldier = soldier

    def random_destination(self):
        # Let soldier walk in the edge of the main_tower
        edge_x = [randint(-self.soldier.main_tower.territory_left, -self.soldier.main_tower.territory_left + 30),
                  randint(self.soldier.main_tower.territory_right - 30, self.soldier.main_tower.territory_right)]
        edge_y = [randint(-self.soldier.main_tower.territory_up, -self.soldier.main_tower.territory_up + 30),
                  randint(self.soldier.main_tower.territory_bottom - 30, self.soldier.main_tower.territory_bottom)]
        x = edge_x[randint(0, 1)]
        y = edge_y[randint(0, 1)]
        new_destination = Vector2(x, y) + self.soldier.main_tower.location
        self.soldier.destination = new_destination

    def do_action(self):
        if abs(self.soldier.location - self.soldier.destination) < 10:
            self.random_destination()
        # Set Soldier Walk Image
        if self.soldier.location.get_xy()[0] < self.soldier.destination.get_xy()[0]:
            if self.soldier.location.get_xy()[1] < self.soldier.destination.get_xy()[1]:
                self.soldier.image = self.soldier.world.image_class.soldier_rb_img
            else:
                self.soldier.image = self.soldier.world.image_class.soldier_ru_img
        else:
            if self.soldier.location.get_xy()[1] < self.soldier.destination.get_xy()[1]:
                self.soldier.image = self.soldier.world.image_class.soldier_lb_img
            else:
                self.soldier.image = self.soldier.world.image_class.soldier_lu_img

    def check_condition(self):
        wolf = self.soldier.world.get_nearest_entity(self.soldier.main_tower.location, "wolf")
        if wolf:
            wolf_distance = abs(wolf.location - self.soldier.main_tower.location)
            if wolf_distance < self.soldier.main_tower.territory_up or \
               wolf_distance < self.soldier.main_tower.territory_bottom or \
               wolf_distance < self.soldier.main_tower.territory_left or \
               wolf_distance < self.soldier.main_tower.territory_right:
                self.soldier.hunting_target = wolf
                return "hunting"

    def entry_action(self):
        self.soldier.speed = 30
        self.soldier.destination = self.soldier.location


class SoldierStateHunting(State):

    def __init__(self, soldier):
        State.__init__(self, "hunting")
        self.soldier = soldier

    def do_action(self):
        if abs(self.soldier.location - self.soldier.destination) < 5:
            if randint(1, 10) == 1:
                self.soldier.hunting_target.bitten()
        # Set Soldier Walk Image
        if self.soldier.location.get_xy()[0] < self.soldier.destination.get_xy()[0]:
            if self.soldier.location.get_xy()[1] < self.soldier.destination.get_xy()[1]:
                self.soldier.image = self.soldier.world.image_class.soldier_rb_img
            else:
                self.soldier.image = self.soldier.world.image_class.soldier_ru_img
        else:
            if self.soldier.location.get_xy()[1] < self.soldier.destination.get_xy()[1]:
                self.soldier.image = self.soldier.world.image_class.soldier_lb_img
            else:
                self.soldier.image = self.soldier.world.image_class.soldier_lu_img
        # Update soldier destination
        self.soldier.destination = self.soldier.hunting_target.location

    def check_condition(self):
        if self.soldier.hunting_target.id not in self.soldier.world.entity_group:
            return "patrol"

    def entry_action(self):
        self.soldier.destination = self.soldier.hunting_target.location
        self.soldier.speed = 80

    def exit_action(self):
        self.soldier.speed = 30
        self.soldier.hunting_target = None
