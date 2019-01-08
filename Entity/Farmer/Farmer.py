from Entity.Farmer.FarmerState import FarmerStateGoCutting, FarmerStateCutting, FarmerStateReturning
from GameEntity import GameEntity
from StateMachine import StateMachine


class Farmer(GameEntity):

    def __init__(self, world, farmer_image, location, village):
        GameEntity.__init__(self, "farmer", world, farmer_image)
        self.location = location
        self.color = (200, 0, 0)
        self.brain = StateMachine()
        self.forest_id = None
        self.bear_load = 15
        stateGoCutting = FarmerStateGoCutting(self)
        stateCutting = FarmerStateCutting(self)
        stateReturning = FarmerStateReturning(self)
        self.brain.add_state(stateGoCutting)
        self.brain.add_state(stateCutting)
        self.brain.add_state(stateReturning)
        self.time_passed = 0
        self.village = village

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)

    def process(self, time_passed):
        GameEntity.process(self, time_passed)
        self.time_passed = time_passed
