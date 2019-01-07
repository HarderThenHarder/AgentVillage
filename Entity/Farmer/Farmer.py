from Entity.Farmer.FarmerState import FarmerStateGoCutting, FarmerStateCutting
from GameEntity import GameEntity
from StateMachine import StateMachine


class Farmer(GameEntity):

    def __init__(self, world, farmer_image, location):
        GameEntity.__init__(self, "farmer", world, farmer_image)
        self.location = location
        self.color = (200, 0, 0)
        self.brain = StateMachine()
        self.forest_id = None
        self.bear_load = 15
        stateGoCutting = FarmerStateGoCutting(self)
        stateCutting = FarmerStateCutting(self)
        self.brain.add_state(stateGoCutting)
        self.brain.add_state(stateCutting)
        self.time_passed = 0

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)

    def process(self, time_passed):
        GameEntity.process(self, time_passed)
        self.time_passed = time_passed
