import pygame
from obj import Obj


class Menu:

    def __init__(self, image):

        self.bg = Obj(image, 0, 0)

        self.change_scene = False

    def draw(self, window):
        self.bg.group.draw(window)

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            self.change_scene = True

class Gameover(Menu):
    def __init__(self, image):
        super().__init__(image)

class Vitoria(Menu):
    def __init__(self, image):
        super().__init__(image)

class Level(Menu):
    def __init__(self, image):
        super().__init__(image)
        self.escolha = None
        self.btn_easy = pygame.Rect(84, 258, 230, 30)
        self.btn_medium = pygame.Rect(84, 338, 230, 30)
        self.btn_hard = pygame.Rect(84, 423, 230, 30)

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse= pygame.mouse.get_pos()
            print (f"A posição do mouse é: {pos_mouse}")
            
            if self.btn_easy.collidepoint(pos_mouse):
                self.escolha = "easy"
                self.change_scene = True

            elif self.btn_medium.collidepoint(pos_mouse):
                self.escolha= "medium"
                self.change_scene = True

            elif self.btn_hard.collidepoint(pos_mouse):
                self.escolha = "hard"
                self.change_scene = True