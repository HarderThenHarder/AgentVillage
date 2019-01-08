from GameEntity import GameEntity
from Pencil import Pencil


class MainTower(GameEntity):

    def __init__(self, world, tree_image, location):
        GameEntity.__init__(self, "village", world, tree_image)
        self.location = location
        self.color = (200, 0, 200)
        self.village_object_group_list = []
        self.wood = 0
        self.mine = 0
        self.food = 0

    def add(self, entity):
        self.village_object_group_list.append(entity)
        entity.main_tower = self

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)
        x, y = self.location.x + start_draw_pos[0], self.location.y + start_draw_pos[1]
        w, h = self.image.get_size()
        text_x = x + w // 2
        text_y = y - h // 2
        Pencil.write_text(surface, "wood:%d" % self.wood, [text_x, text_y], 13, color=(200, 200, 200))
        Pencil.write_text(surface, "food:%d" % self.food, [text_x, text_y + 13], 13, color=(200, 200, 200))
        Pencil.write_text(surface, "mine:%d" % self.mine, [text_x, text_y + 26], 13, color=(200, 200, 200))
