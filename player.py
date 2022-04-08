import pygame


class Helicopter(pygame.sprite.Sprite):
    def __init__(self, xy, screen):
        pygame.sprite.Sprite.__init__(self)
        """
        self.image = pygame.Surface([72, 48])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        """
        self.skin = 1
        self.image = pygame.image.load(f"data/helicopters/{1}.gif")
        self.image.set_colorkey((0, 254, 0))
        self.image = pygame.transform.scale(self.image, (120, 80))
        self.rect = self.image.get_rect(center=(0, 0))

        self.rect.center = xy

    def coords(self):
        return self.rect.center

    def update(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 10
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 10
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= 6
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += 6
