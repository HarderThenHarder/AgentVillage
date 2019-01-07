from State import State
from random import randint

from Vector2 import Vector2


class FarmerStateGoCutting(State):

    def __init__(self, farmer):
        State.__init__(self, "goCutting")
        self.farmer = farmer

    def do_action(self):
        pass

    def check_condition(self):
        if self.farmer.forest_id:
            if abs(self.farmer.location - self.farmer.world.entity_group[self.farmer.forest_id].location) < 75:
                return "cutting"
        return None

    def entry_action(self):
        self.farmer.speed = 100
        forest = self.farmer.world.get_nearest_entity(self.farmer.location, "forest")
        if forest:
            self.farmer.destination = forest.location + Vector2(randint(-75, 75), randint(-50, 50))
            self.farmer.forest_id = forest.id


class FarmerStateCutting(State):

    def __init__(self, farmer):
        State.__init__(self, "cutting")
        self.farmer = farmer

    def do_action(self):
        self.farmer.bear_load -= 1 * (self.farmer.time_passed / 1000)
        if self.farmer.forest_id in self.farmer.world.entity_group:
            self.farmer.world.entity_group[self.farmer.forest_id].wood -= 1 * (self.farmer.time_passed / 1000)
            if self.farmer.world.entity_group[self.farmer.forest_id].wood <= 0:
                self.farmer.world.remove(self.farmer.forest_id)

    def check_condition(self):
        if self.farmer.bear_load <= 0:
            return "returning"
        return None
