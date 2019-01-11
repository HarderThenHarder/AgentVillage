from Entity.Sodier.SoldierState import SoldierStatePatrol, SoldierStateHunting
from GameEntity import GameEntity
from StateMachine import StateMachine


class Soldier(GameEntity):

    def __init__(self, world, soldier_image, location):
        GameEntity.__init__(self, "soldier", world, soldier_image)
        self.location = location
        self.color = (0, 0, 200)
        self.brain = StateMachine()
        statePatrol = SoldierStatePatrol(self)
        stateHunting = SoldierStateHunting(self)
        self.brain.add_state(statePatrol)
        self.brain.add_state(stateHunting)
        self.time_passed = 0
        self.main_tower = None
        self.hp = 20
        self.hunting_target = None

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
