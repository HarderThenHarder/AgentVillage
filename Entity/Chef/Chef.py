from Entity.Chef.ChefState import ChefStateFree, ChefStateGoPlanting, ChefStatePlanting
from GameEntity import GameEntity
from StateMachine import StateMachine


class Chef(GameEntity):

    def __init__(self, world, chef_image, location):
        GameEntity.__init__(self, "chef", world, chef_image)
        self.location = location
        self.color = (200, 0, 0)
        self.brain = StateMachine()
        stateFree = ChefStateFree(self)
        stateGoPlanting = ChefStateGoPlanting(self)
        statePlanting = ChefStatePlanting(self)
        self.brain.add_state(stateFree)
        self.brain.add_state(stateGoPlanting)
        self.brain.add_state(statePlanting)
        self.time_passed = 0
        self.main_tower = None
        self.build_process = 0

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)

    def process(self, time_passed):
        GameEntity.process(self, time_passed)
        self.time_passed = time_passed
