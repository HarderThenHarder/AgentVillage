from Pencil import Pencil
import pygame
from Timer import Timer
from Vector2 import Vector2
import matplotlib.pyplot as plt


class World:

    def __init__(self, world_bg, WIDTH_HEIGHT, image_class, WHOLE_MAP_SIZE):
        self.world_bg = world_bg
        self.entity_group = {}
        self.entity_id = 0
        self.WIDTH_HEIGHT = WIDTH_HEIGHT
        self.sub_map_width_height = [400, 270]
        self.sub_map_surface = self.set_sub_map()
        self.rect_in_sub_map_width_height = []
        self.rect_in_sub_map_pos = []
        self.image_class = image_class
        self.WHOLE_MAP_SIZE = WHOLE_MAP_SIZE
        self.timer = Timer()
        self.wood_history = []
        self.mine_history = []
        self.population_history = []
        self.food_history = []
        self.update_state_window_frequency = 100
        self.update_state_window_step = 0
        self.set_plt()

    def set_plt(self):
        plt.ion()
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['lines.linewidth'] = 1
        plt.style.use("ggplot")
        plt.rcParams['figure.figsize'] = (5, 5)
        fig = plt.gcf()
        fig.canvas.set_window_title("Stone Age State History")

    def update_state_window(self):
        plt.clf()
        plt.suptitle("World State")
        gragh = plt.subplot(1, 1, 1)
        gragh.set_xlabel("Time Elapsed(ticks)")
        gragh.set_ylabel("Values")
        gragh.plot(self.food_history, label="Food", linestyle='--', color='orange')
        gragh.plot(self.wood_history, label="Wood", linestyle='--', color='purple')
        gragh.plot(self.mine_history, label="Mine", linestyle='--', color='c')
        gragh.plot(self.population_history, label="Population", color='r')
        self.update_state_window_step = 0
        plt.legend(loc='upper left')
        plt.pause(0.001)

    def set_sub_map(self):
        sub_map_surface = pygame.Surface(self.sub_map_width_height)
        sub_map_surface.fill(color=(100, 100, 100))
        sub_map_surface.set_alpha(100)
        return sub_map_surface

    def add(self, entity):
        self.entity_group[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove(self, entity_id):
        del self.entity_group[entity_id]

    def render(self, screen, start_draw_pos):
        screen.blit(self.world_bg, start_draw_pos)
        # Draw Entity && sort the entity by their y position
        for tuple_element in sorted(self.entity_group.items(), key=lambda item: item[1].location.get_xy()[1]):
            entity = tuple_element[1]
            entity.render(screen, start_draw_pos)
        # Draw Sub Map
        screen.blit(self.sub_map_surface, (0, self.WIDTH_HEIGHT[1] - self.sub_map_width_height[1]))
        Pencil.draw_rect(screen, [*self.rect_in_sub_map_pos, *self.rect_in_sub_map_width_height], (200, 200, 200), 1)
        # Draw entity on Sub Map
        for entity in self.entity_group.values():
            if entity.color:
                x, y = entity.location.get_xy()
                entity_in_sub_map_rect = [int(x / 9600 * self.sub_map_width_height[0]),
                                          self.WIDTH_HEIGHT[1] - self.sub_map_width_height[1] + int(
                                              y / 5400 * self.sub_map_width_height[1]), 3, 3]
                Pencil.draw_rect(screen, entity_in_sub_map_rect, entity.color)

        # Write State of Main Tower.
        main_tower = self.get_nearest_entity(Vector2(0, 0), "main_tower")
        Pencil.write_text(screen, "wood:%d" % main_tower.wood, [0, 0], 15, color=(255, 255, 255))
        Pencil.write_text(screen, "food:%d" % main_tower.food, [0, 15], 15, color=(255, 255, 255))
        Pencil.write_text(screen, "mine:%d" % main_tower.mine, [0, 30], 15, color=(255, 255, 255))
        Pencil.write_text(screen, "farmland:%d" % main_tower.get_building_entity_number("planting"), [0, 45], 15,
                          color=(255, 255, 255))
        Pencil.write_text(screen, "population:%d" % len(main_tower.people_list), [0, 60], 15,
                          color=(255, 255, 255))
        Pencil.write_text(screen, "[%02d:%02d:%02d]" % (self.timer.get_hour(), self.timer.get_minute(), self.timer.get_second()), [0, 75], 15, color=(255, 255, 255))

        # Update the World State Window
        if self.update_state_window_step % self.update_state_window_frequency == 0:
            self.food_history.append(main_tower.food)
            self.wood_history.append(main_tower.wood)
            self.mine_history.append(main_tower.mine)
            self.population_history.append(len(main_tower.people_list))
            self.update_state_window()

        self.update_state_window_step += 1


    def process(self, start_draw_pos, WIDTH_HEIGHT, time_passed):
        # Update the rect pos in sub map
        self.rect_in_sub_map_width_height = [self.WIDTH_HEIGHT[0] / 9600 * self.sub_map_width_height[0],
                                             self.WIDTH_HEIGHT[1] / 5400 * self.sub_map_width_height[1]]
        self.rect_in_sub_map_pos = [int(abs(start_draw_pos[0]) / 9600 * self.sub_map_width_height[0]),
                                    self.WIDTH_HEIGHT[1] - self.sub_map_width_height[1] + int(
                                        abs(start_draw_pos[1]) / 5400 * self.sub_map_width_height[1])]
        self.WIDTH_HEIGHT = WIDTH_HEIGHT
        time_passed = time_passed
        for entity in list(self.entity_group.values()):
            entity.process(time_passed)
        self.timer.update_timer(time_passed)

    def get_nearest_entity(self, location, name):
        location = location.copy()
        nearest_entity = None
        min_d = 9999999
        for entity in self.entity_group.values():
            if entity.name == name:
                distance = abs(entity.location - location)
                if distance < min_d:
                    min_d = distance
                    nearest_entity = entity
        return nearest_entity

    def get_entity_number(self, name):
        number = 0
        for entity in self.entity_group.values():
            if entity.name == name:
                number += 1
        return number
