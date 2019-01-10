"""
@author: P_k_y
"""
from GameEntity import GameEntity


class Plantings(GameEntity):

    def __init__(self, world, plantings_image, location, plant_type):
        GameEntity.__init__(self, "planting", world, plantings_image)
        self.location = location
        self.color = None
        self.food = 200
        self.plant_type = plant_type

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)



