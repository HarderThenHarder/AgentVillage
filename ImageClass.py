import pygame


class ImageClass:

    def __init__(self):
        self.world_bg = pygame.transform.scale(pygame.image.load(r"img\world3.png"), (9600, 5400))
        self.forest_img = pygame.transform.scale(pygame.image.load(r"img\forest.png"), (200, 150))
        self.stone_img = pygame.transform.scale(pygame.image.load(r"img\stone.png"), (80, 60))
        self.flower_img = pygame.transform.scale(pygame.image.load(r"img\flower.png"), (30, 30))
        self.berry_img = pygame.transform.scale(pygame.image.load(r"img\berry.png"), (50, 50))
        self.house_img = pygame.transform.scale(pygame.image.load(r"img\house.png"), (120, 100))

        self.farmer_lb_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_lb.png"), (30, 30))
        self.farmer_lu_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_lu.png"), (30, 30))
        self.farmer_ru_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_ru.png"), (30, 30))
        self.farmer_rb_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_rb.png"), (30, 30))
        self.farmer_lb_full_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_lb_full.png"), (30, 30))
        self.farmer_rb_full_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_rb_full.png"), (30, 30))
        self.farmer_lu_full_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_lu_full.png"), (30, 30))
        self.farmer_ru_full_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_ru_full.png"), (30, 30))
        self.farmer_work_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_work.png"), (30, 30))

        self.main_tower_img = pygame.transform.scale(pygame.image.load(r"img\tower.png"), (60, 100))


