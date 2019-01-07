import pygame


class Pencil:

    @staticmethod
    def draw_line(screen, start_pos, end_pos, color=(0, 0, 0), width=1):
        pygame.draw.line(screen, color, start_pos, end_pos, width)

    @staticmethod
    def draw_rect(screen, rect, color=(0, 0, 0), width=0):
        """
        If width != 0, then the rect won't be filled, it will be stroked!

        """
        pygame.draw.rect(screen, color, rect, width)

    @staticmethod
    def draw_alpha_rect(screen, rect, color=(0, 0, 0), alpha=0.8):
        alpha_rect = pygame.Surface([rect[2], rect[3]])
        alpha_rect.fill(color)
        alpha_rect.set_alpha(int(alpha * 255))
        screen.blit(alpha_rect, (rect[0], rect[1]))

    @staticmethod
    def draw_poly_rect(screen, color, pointlist, width=0):
        pygame.draw.polygon(screen, color, pointlist, width)

    @staticmethod
    def draw_circle(screen, pos,  radius, color=(0, 0, 0), width=0):
        pygame.draw.circle(screen, color, pos, radius, width)

    @staticmethod
    def draw_arc(screen, rect, start_angle, end_angle, color=(0, 0, 0), width=0):
        pygame.draw.arc(screen, color, rect, start_angle, end_angle, width)

    @staticmethod
    def write_text(screen, content, font_pos, font_size, color=(0, 0, 0)):
        my_font = pygame.font.SysFont("consolas", font_size)
        text_image = my_font.render(content, True, color)
        screen.blit(text_image, font_pos)
