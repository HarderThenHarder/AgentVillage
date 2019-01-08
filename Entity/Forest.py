from GameEntity import GameEntity
from Pencil import Pencil


class Forest(GameEntity):

    def __init__(self, world, tree_image, location):
        GameEntity.__init__(self, "forest", world, tree_image)
        self.location = location
        self.color = (0, 200, 0)
        self.max_wood = 500
        self.wood = self.max_wood

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)
        if self.wood < self.max_wood:
            x, y = self.location.x + start_draw_pos[0], self.location.y + start_draw_pos[1]
            w, h = self.image.get_size()
            # bar_w = 40
            # bar_h = 4
            # bar_x = x - bar_w // 2
            # bar_y = y + h // 2 + 10
            # surface.fill((150, 0, 0), (bar_x, bar_y, bar_w, 4))
            # surface.fill((0, 150, 0), (bar_x, bar_y, self.wood / self.max_wood * bar_w, bar_h))
            text_x = x - 20
            text_y = y + h // 2
            Pencil.write_text(surface, "%3d/500" % self.wood, [text_x, text_y], 10, color=(200, 200, 200))
