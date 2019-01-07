from GameEntity import GameEntity


class Stone(GameEntity):

    def __init__(self, world, stone_image, location):
        GameEntity.__init__(self, "Stone", world, stone_image)
        self.location = location
        self.color = (100, 100, 100)

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)
