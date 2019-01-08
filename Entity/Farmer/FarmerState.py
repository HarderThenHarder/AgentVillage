from State import State
from random import randint
from Vector2 import Vector2


class FarmerStateGoCutting(State):

    def __init__(self, farmer):
        State.__init__(self, "goCutting")
        self.farmer = farmer

    def do_action(self):
        # Set Farmer Walk Image
        if self.farmer.location.get_xy()[0] < self.farmer.destination.get_xy()[0]:
            if self.farmer.location.get_xy()[1] < self.farmer.destination.get_xy()[1]:
                self.farmer.image = self.farmer.world.image_class.farmer_rb_img
            else:
                self.farmer.image = self.farmer.world.image_class.farmer_ru_img
        else:
            if self.farmer.location.get_xy()[1] < self.farmer.destination.get_xy()[1]:
                self.farmer.image = self.farmer.world.image_class.farmer_lb_img
            else:
                self.farmer.image = self.farmer.world.image_class.farmer_lu_img

    def check_condition(self):
        if self.farmer.forest_id:
            if abs(self.farmer.location - self.farmer.destination) < 10:
                return "cutting"
        return None

    def entry_action(self):
        self.farmer.speed = 60
        forest = self.farmer.world.get_nearest_entity(self.farmer.location, "forest")
        if forest:
            self.farmer.destination = forest.location + Vector2(randint(-50, 50), randint(-20, 50))
            self.farmer.forest_id = forest.id


class FarmerStateCutting(State):

    def __init__(self, farmer):
        State.__init__(self, "cutting")
        self.farmer = farmer

    def do_action(self):
        if self.farmer.forest_id in self.farmer.world.entity_group:
            self.farmer.bear_load -= 1 * (self.farmer.time_passed / 1000)
            self.farmer.world.entity_group[self.farmer.forest_id].wood -= 1 * (self.farmer.time_passed / 1000)
            if self.farmer.world.entity_group[self.farmer.forest_id].wood <= 0:
                self.farmer.world.remove(self.farmer.forest_id)

    def check_condition(self):
        if self.farmer.bear_load <= 0:
            return "returning"
        if self.farmer.forest_id not in self.farmer.world.entity_group and self.farmer.bear_load > 0:
            return "goCutting"
        return None

    def entry_action(self):
        self.farmer.destination = self.farmer.location
        self.farmer.image = self.farmer.world.image_class.farmer_work_img


class FarmerStateReturning(State):

    def __init__(self, farmer):
        State.__init__(self, "returning")
        self.farmer = farmer

    def do_action(self):
        # Set Farmer Walk Image
        if self.farmer.location.get_xy()[0] < self.farmer.destination.get_xy()[0]:
            if self.farmer.location.get_xy()[1] < self.farmer.destination.get_xy()[1]:
                self.farmer.image = self.farmer.world.image_class.farmer_rb_full_img
            else:
                self.farmer.image = self.farmer.world.image_class.farmer_ru_full_img
        else:
            if self.farmer.location.get_xy()[1] < self.farmer.destination.get_xy()[1]:
                self.farmer.image = self.farmer.world.image_class.farmer_lb_full_img
            else:
                self.farmer.image = self.farmer.world.image_class.farmer_lu_full_img

    def check_condition(self):
        if abs(self.farmer.location - self.farmer.main_tower.location) < 50:
            return "goCutting"

    def entry_action(self):
        self.farmer.destination = self.farmer.main_tower.location
        self.farmer.speed = 30

    def exit_action(self):
        self.farmer.bear_load = self.farmer.max_bear_load
        self.farmer.main_tower.wood += self.farmer.max_bear_load
