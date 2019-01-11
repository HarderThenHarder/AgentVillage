from GameEntity import GameEntity
from Pencil import Pencil
from Trigger import Trigger


class MainTower(GameEntity):

    def __init__(self, world, tree_image, location):
        GameEntity.__init__(self, "main_tower", world, tree_image)
        self.location = location
        self.color = (200, 0, 200)
        self.people_list = []
        self.building_list = []
        self.wood = 1000
        self.mine = 1000
        self.food = 200
        self.territory_up = 300
        self.territory_bottom = 300
        self.territory_left = 300
        self.territory_right = 300

    def add(self, entity):
        self.people_list.append(entity)
        entity.main_tower = self

    def add_building(self, entity):
        self.building_list.append(entity)
        entity.main_tower = self

    def get_building_entity_number(self, name):
        number = 0
        for entity in self.building_list:
            if entity.name == name:
                number += 1
        return number

    def get_building_entity_list(self, name):
        entity_list = []
        for entity in self.building_list:
            if entity.name == name:
                entity_list.append(entity)
        return entity_list

    def get_nearest_people(self, location):
        location = location.copy()
        nearest_entity = None
        min_d = 9999999
        for entity in self.people_list:
            distance = abs(entity.location - location)
            if distance < min_d:
                min_d = distance
                nearest_entity = entity
        return nearest_entity

    def process(self, time_passed):
        GameEntity.process(self, time_passed)
        # reduce the food (1 people consume 0.1 food per second)
        self.food -= 0.1 * len(self.people_list) * time_passed / 1000
        if self.food < 0:
            self.food = 0
        # People Add
        Trigger.strike_add_people_event(self, self.world)
        # People Die
        Trigger.strike_hungry_people_event(self, self.world)
        # Remove redundant farmland
        Trigger.strike_remove_farmland_event(self, self.world)
        # Random Generate Wolf
        Trigger.strike_generate_wolf_event(self, self.world)

    def render(self, surface, start_draw_pos):
        GameEntity.render(self, surface, start_draw_pos)
        x, y = self.location.x + start_draw_pos[0], self.location.y + start_draw_pos[1]
        w, h = self.image.get_size()
        text_x = x + w // 2
        text_y = y - h // 2
        Pencil.write_text(surface, "wood:%d" % self.wood, [text_x, text_y], 13, color=(200, 200, 200))
        Pencil.write_text(surface, "food:%d" % self.food, [text_x, text_y + 13], 13, color=(200, 200, 200))
        Pencil.write_text(surface, "mine:%d" % self.mine, [text_x, text_y + 26], 13, color=(200, 200, 200))
        # Write State of Main Tower
        Pencil.write_text(surface, "wood:%d" % self.wood, [0, 0], 15, color=(255, 255, 255))
        Pencil.write_text(surface, "food:%d" % self.food, [0, 15], 15, color=(255, 255, 255))
        Pencil.write_text(surface, "mine:%d" % self.mine, [0, 30], 15, color=(255, 255, 255))
        Pencil.write_text(surface, "farmland:%d" % self.get_building_entity_number("planting"), [0, 45], 15, color=(255, 255, 255))
        Pencil.write_text(surface, "population:%d" % len(self.people_list), [0, 60], 15, color=(255, 255, 255))
        Pencil.write_text(surface, "[%02d:%02d:%02d]" % (self.world.timer.get_hour(), self.world.timer.get_minute(), self.world.timer.get_second()),
                          [0, 75], 15, color=(255, 255, 255))
        # Pencil.draw_rect(surface, [start_draw_pos[0] + self.location.get_xy()[0] - self.territory_left,
        #                            start_draw_pos[1] + self.location.get_xy()[1] - self.territory_up,
        #                            self.territory_left + self.territory_right, self.territory_up * self.territory_bottom],
        #                           (150, 150, 150), 1)
