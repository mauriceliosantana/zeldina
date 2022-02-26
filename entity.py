import pygame
from math import sin

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direcao = pygame.math.Vector2()

    def mover(self, velocidade):
        if self.direcao.magnitude() != 0:
            self.direcao = self.direcao.normalize()

        self.hitbox.x += self.direcao.x * velocidade
        self.colisao('horizontal')
        self.hitbox.y += self.direcao.y * velocidade
        self.colisao('vertical')
        self.rect.center = self.hitbox.center

    def colisao(self, direcao):
        if direcao == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direcao.x > 0:  # mover à direita
                        self.hitbox.right = sprite.hitbox.left
                    if self.direcao.x < 0:  # mover à esquerda
                        self.hitbox.left = sprite.hitbox.right
        if direcao == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direcao.y > 0:  # mover para baixo
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direcao.y < 0:  # mover para cima
                        self.hitbox.top = sprite.hitbox.bottom

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0
