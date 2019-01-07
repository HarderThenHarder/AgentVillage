"""
@author: P_k_y
"""
from GameEntity import GameEntity


class Flower(GameEntity):

    def __init__(self, world, flower_image, location):
        GameEntity.__init__(self, "flower", world, flower_image)
        self.location = location
        self.color = None

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)


