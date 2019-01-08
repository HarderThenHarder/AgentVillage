from GameEntity import GameEntity


class Village(GameEntity):

    def __init__(self, world, tree_image, location):
        GameEntity.__init__(self, "village", world, tree_image)
        self.location = location
        self.color = (200, 0, 200)

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)
