"""
@author: P_k_y
"""
from GameEntity import GameEntity


class Berry(GameEntity):

    def __init__(self, world, berry_image, location):
        GameEntity.__init__(self, "berry", world, berry_image)
        self.location = location
        self.color = None

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)



