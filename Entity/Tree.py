from GameEntity import GameEntity


class Tree(GameEntity):

    def __init__(self, world, tree_image, location):
        GameEntity.__init__(self, "tree", world, tree_image)
        self.location = location
        self.color = (0, 200, 0)

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)
