from Entity.Architect.ArchitectState import ArchitectStateFree, ArchitectStateGoBuilding, ArchitectStateBuilding
from GameEntity import GameEntity
from StateMachine import StateMachine


class Architect(GameEntity):

    def __init__(self, world, architect_image, location):
        GameEntity.__init__(self, "architect", world, architect_image)
        self.location = location
        self.color = (0, 0, 200)
        self.brain = StateMachine()
        stateFree = ArchitectStateFree(self)
        stateGoBuilding = ArchitectStateGoBuilding(self)
        stateBuilding = ArchitectStateBuilding(self)
        self.brain.add_state(stateFree)
        self.brain.add_state(stateGoBuilding)
        self.brain.add_state(stateBuilding)
        self.time_passed = 0
        self.main_tower = None
        self.new_house = None
        self.build_process = 0
        self.hp = 10

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)

    def process(self, time_passed):
        GameEntity.process(self, time_passed)
        self.time_passed = time_passed

    def bitten(self):
        self.hp -= 1
        if self.hp <= 0:
            self.world.remove(self.id)
            self.main_tower.people_list.remove(self)
            del self
