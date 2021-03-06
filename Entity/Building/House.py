"""
@author: P_k_y
"""
from GameEntity import GameEntity


class House(GameEntity):

    def __init__(self, world, house_img, location, house_type):
        GameEntity.__init__(self, "house", world, house_img)
        self.location = location
        self.color = None
        self.capacity = 10
        self.house_type = house_type

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)


