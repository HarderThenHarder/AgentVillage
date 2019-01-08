from GameEntity import GameEntity
from StateMachine import StateMachine


class Soldier(GameEntity):

    def __init__(self, world, soldier_image, location):
        GameEntity.__init__(self, "soldier", world, soldier_image)
        self.location = location
        self.color = (200, 0, 0)
        self.brain = StateMachine()
        self.time_passed = 0
        self.main_tower = None

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)

    def process(self, time_passed):
        GameEntity.process(self, time_passed)
        self.time_passed = time_passed
