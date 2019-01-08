from GameEntity import GameEntity
from Pencil import Pencil


class Stone(GameEntity):

    def __init__(self, world, stone_image, location):
        GameEntity.__init__(self, "stone", world, stone_image)
        self.location = location
        self.color = (100, 100, 100)
        self.max_mine = 300
        self.mine = self.max_mine

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)
        if self.mine < self.max_mine:
            x, y = self.location.x + start_draw_pos[0], self.location.y + start_draw_pos[1]
            w, h = self.image.get_size()
            text_x = x - 20
            text_y = y + h // 2
            Pencil.write_text(surface, "%3d/%3d" % (self.mine, self.max_mine), [text_x, text_y], 10, color=(200, 200, 200))
