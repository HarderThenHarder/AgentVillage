import pygame


class ImageClass:

    def __init__(self):
        # world
        self.world_bg = pygame.transform.scale(pygame.image.load(r"img\world.png"), (9600, 5400))

        # resource
        self.forest_img = pygame.transform.scale(pygame.image.load(r"img\forest.png"), (200, 150))
        self.stone_img = pygame.transform.scale(pygame.image.load(r"img\stone.png"), (80, 60))
        self.flower_img = pygame.transform.scale(pygame.image.load(r"img\flower.png"), (30, 30))
        self.berry_img = pygame.transform.scale(pygame.image.load(r"img\berry.png"), (50, 50))

        # house
        self.house_img = pygame.transform.scale(pygame.image.load(r"img\building\house.png"), (150, 120))
        self.house_unfinished_img = pygame.transform.scale(pygame.image.load(r"img\building\house_unfinished.png"), (150, 120))
        self.house2_img = pygame.transform.scale(pygame.image.load(r"img\building\house2.png"), (150, 120))
        self.house2_unfinished_img = pygame.transform.scale(pygame.image.load(r"img\building\house2_unfinished.png"), (150, 120))

        # farmer
        self.farmer_lb_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_lb.png"), (30, 30))
        self.farmer_lu_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_lu.png"), (30, 30))
        self.farmer_ru_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_ru.png"), (30, 30))
        self.farmer_rb_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_rb.png"), (30, 30))
        self.farmer_lb_full_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_lb_full.png"), (30, 30))
        self.farmer_rb_full_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_rb_full.png"), (30, 30))
        self.farmer_lu_full_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_lu_full.png"), (30, 30))
        self.farmer_ru_full_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_ru_full.png"), (30, 30))
        self.farmer_work_img = pygame.transform.scale(pygame.image.load(r"img\farmer\farmer_work.png"), (30, 30))

        # soldier
        self.soldier_lb_img = pygame.transform.scale(pygame.image.load(r"img\soldier\soldier_lb.png"), (40, 40))
        self.soldier_lu_img = pygame.transform.scale(pygame.image.load(r"img\soldier\soldier_lu.png"), (40, 40))
        self.soldier_rb_img = pygame.transform.scale(pygame.image.load(r"img\soldier\soldier_rb.png"), (40, 40))
        self.soldier_ru_img = pygame.transform.scale(pygame.image.load(r"img\soldier\soldier_ru.png"), (40, 40))

        # architect
        self.architect_lb_img = pygame.transform.scale(pygame.image.load(r"img\architect\architect_lb.png"), (30, 30))
        self.architect_lu_img = pygame.transform.scale(pygame.image.load(r"img\architect\architect_lu.png"), (30, 30))
        self.architect_rb_img = pygame.transform.scale(pygame.image.load(r"img\architect\architect_rb.png"), (30, 30))
        self.architect_ru_img = pygame.transform.scale(pygame.image.load(r"img\architect\architect_ru.png"), (30, 30))
        self.architect_work_img = pygame.transform.scale(pygame.image.load(r"img\architect\architect_work.png"), (30, 30))

        # chef
        self.chef_lb_img = pygame.transform.scale(pygame.image.load(r"img\chef\chef_lb.png"), (30, 30))
        self.chef_lu_img = pygame.transform.scale(pygame.image.load(r"img\chef\chef_lu.png"), (30, 30))
        self.chef_rb_img = pygame.transform.scale(pygame.image.load(r"img\chef\chef_rb.png"), (30, 30))
        self.chef_ru_img = pygame.transform.scale(pygame.image.load(r"img\chef\chef_ru.png"), (30, 30))
        self.chef_work_img = pygame.transform.scale(pygame.image.load(r"img\chef\chef_work.png"), (30, 30))

        # main tower
        self.main_tower_img = pygame.transform.scale(pygame.image.load(r"img\building\tower.png"), (60, 100))

        # Wheats
        self.wheats_unfinished_img = pygame.transform.scale(pygame.image.load(r"img\plants\wheats_unfinished.png"), (100, 100))
        self.wheats_img = pygame.transform.scale(pygame.image.load(r"img\plants\wheats.png"), (100, 100))

        # Carrots
        self.carrots_unfinished_img = pygame.transform.scale(pygame.image.load(r"img\plants\carrots_unfinished.png"), (100, 100))
        self.carrots_img = pygame.transform.scale(pygame.image.load(r"img\plants\carrots.png"), (100, 100))
