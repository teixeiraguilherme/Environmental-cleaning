import pygame

class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1
        self.tick = 0

    def drawing(self,window):
        self.group.draw(window)

    def anima(self, image, tick, frames):
        self.tick += 1
        
        if self.tick >= tick:
            self.tick = 0
            self.frame += 1

        if self.frame > frames:
            self.frame = 1

        self.sprite.image = pygame.image.load("assets/" + image + str(self.frame) + ".png")


class Player(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound("assets/som/pontos.mp3")
        self.sound_dano = pygame.mixer.Sound("assets/som/dano.mp3")

        self.vida = 5
        self.pts = 0

    def move_player(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 32
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 32


    def colisao(self, group):
        colisao = pygame.sprite.spritecollide(self.sprite, group, True)
        if colisao:
            self.pts += 1          
            self.sound_pts.play()

    def colisao_dano(self, group):
        colisao = pygame.sprite.spritecollide(self.sprite, group, True)
        if colisao:
            self.vida -= 1          
            self.sound_dano.play()

class Texto:
    def __init__(self, size, text):
        self.font = pygame.font.SysFont("Press Start 2P", size)
        self.render = self.font.render(text, False, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update_texto(self, text):
        self.render = self.font.render(text, False, (255, 255, 255))