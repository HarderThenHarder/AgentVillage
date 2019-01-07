from Pencil import Pencil
import pygame


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

    def render(self, screen, start_draw_pos):
        screen.blit(self.world_bg, start_draw_pos)
        screen.blit(self.sub_map_surface, (0, self.WIDTH_HEIGHT[1] - self.sub_map_width_height[1]))
        Pencil.draw_rect(screen, [*self.rect_in_sub_map_pos, *self.rect_in_sub_map_width_height], (200, 200, 200), 1)

    def process(self, start_draw_pos):
        self.rect_in_sub_map_width_height = [self.WIDTH_HEIGHT[0] / 9600 * self.sub_map_width_height[0],
                                             self.WIDTH_HEIGHT[1] / 5400 * self.sub_map_width_height[1]]
        self.rect_in_sub_map_pos = [int(abs(start_draw_pos[0]) / 9600 * self.sub_map_width_height[0]),
                                    int(abs(start_draw_pos[1]) / 5400 * self.sub_map_width_height[1])]
