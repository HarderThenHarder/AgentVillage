from Entity.Wolf.WolfState import WolfStateHiding, WolfStateRetreating, WolfStateAttacking, WolfStateGoAttacking
from GameEntity import GameEntity
from StateMachine import StateMachine


class Wolf(GameEntity):

    def __init__(self, world, location, forest):
        GameEntity.__init__(self, "wolf", world, image=None)
        self.location = location
        self.color = (200, 0, 0)
        self.brain = StateMachine()
        stateHiding = WolfStateHiding(self)
        stateGoAttacking = WolfStateGoAttacking(self)
        stateAttacking = WolfStateAttacking(self)
        stateRetreating = WolfStateRetreating(self)
        self.brain.add_state(stateHiding)
        self.brain.add_state(stateGoAttacking)
        self.brain.add_state(stateAttacking)
        self.brain.add_state(stateRetreating)
        self.time_passed = 0
        self.forest = forest
        self.hp = 20
        self.attack_main_tower = None
        self.attack_people = None

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)

    def process(self, time_passed):
        GameEntity.process(self, time_passed)
        self.time_passed = time_passed
        if self.forest.id not in self.world.entity_group:
            self.forest = self.world.get_nearest_entity(self.location, "forest")

    def bitten(self):
        self.hp -= 1
        if self.hp <= 0:
            if self.id in self.world.entity_group:
                self.world.remove(self.id)
            del self
