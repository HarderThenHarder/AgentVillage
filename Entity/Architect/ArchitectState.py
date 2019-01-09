from State import State
from random import randint

from Vector2 import Vector2


class ArchitectStateFree(State):

    def __init__(self, architect):
        State.__init__(self, "free")
        self.architect = architect

    def random_walk(self):
        x = randint(-50, 50)
        y = randint(-50, 50)
        self.architect.destination = self.architect.location + Vector2(x, y)

    def do_action(self):
        if abs(self.architect.location - self.architect.destination) < 5:
            if randint(1, 50) == 1:
                self.random_walk()
        # Set architect Walk Image
        if self.architect.location.get_xy()[0] < self.architect.destination.get_xy()[0]:
            if self.architect.location.get_xy()[1] < self.architect.destination.get_xy()[1]:
                self.architect.image = self.architect.world.image_class.architect_rb_img
            else:
                self.architect.image = self.architect.world.image_class.architect_ru_img
        else:
            if self.architect.location.get_xy()[1] <= self.architect.destination.get_xy()[1]:
                self.architect.image = self.architect.world.image_class.architect_lb_img
            else:
                self.architect.image = self.architect.world.image_class.architect_lu_img

    def check_condition(self):
        pass

    def entry_action(self):
        self.architect.speed = 30
        self.architect.destination = self.architect.location
