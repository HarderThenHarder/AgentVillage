from Pencil import Pencil
import pygame
from Vector2 import Vector2


class World:

    def __init__(self, world_bg, WIDTH_HEIGHT):
        self.world_bg = world_bg
        self.entity_group = {}
        self.entity_id = 0
        self.WIDTH_HEIGHT = WIDTH_HEIGHT
        self.sub_map_width_height = [400, 270]
        self.sub_map_surface = self.set_sub_map()
        self.rect_in_sub_map_width_height = []
        self.rect_in_sub_map_pos = []

    def set_sub_map(self):
        sub_map_surface = pygame.Surface(self.sub_map_width_height)
        sub_map_surface.fill(color=(100, 100, 100))
        sub_map_surface.set_alpha(100)
        return sub_map_surface

    def add(self, entity):
        self.entity_group[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def render(self, screen, start_draw_pos):
        screen.blit(self.world_bg, start_draw_pos)
        # Draw Entity
        for entity in self.entity_group.values():
            entity.render(screen, start_draw_pos)
            # draw entity on sub map
            if entity.color:
                x, y = entity.location.get_xy()
                entity_in_sub_map_rect = [int(x / 9600 * self.sub_map_width_height[0]),
                                          self.WIDTH_HEIGHT[1] - self.sub_map_width_height[1] + int(y / 5400 * self.sub_map_width_height[1]), 3, 3]
                Pencil.draw_rect(screen, entity_in_sub_map_rect, entity.color)
        # Draw Sub Map
        screen.blit(self.sub_map_surface, (0, self.WIDTH_HEIGHT[1] - self.sub_map_width_height[1]))
        Pencil.draw_rect(screen, [*self.rect_in_sub_map_pos, *self.rect_in_sub_map_width_height], (200, 200, 200), 1)

    def process(self, start_draw_pos):
        # Update the rect pos in sub map
        self.rect_in_sub_map_width_height = [self.WIDTH_HEIGHT[0] / 9600 * self.sub_map_width_height[0],
                                             self.WIDTH_HEIGHT[1] / 5400 * self.sub_map_width_height[1]]
        self.rect_in_sub_map_pos = [int(abs(start_draw_pos[0]) / 9600 * self.sub_map_width_height[0]),
                                    self.WIDTH_HEIGHT[1] - self.sub_map_width_height[1] + int(abs(start_draw_pos[1]) / 5400 * self.sub_map_width_height[1])]

