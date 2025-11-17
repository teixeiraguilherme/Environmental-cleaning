import pygame
from menu import Menu, Gameover, Vitoria
from game import Game

class Main:

    def __init__(self, sizex, sizey, title):

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/som/musica.mp3")
        pygame.mixer.music.play(-1)

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu("assets/png/menu.png")
        self.game = Game()
        self.gameover = Gameover("assets/png/gameover.png")
        self.winner = Vitoria("assets/png/win.png")

        self.loop = True
        self.fps = pygame.time.Clock()

    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        elif self.game.scene_type == "gameover" and not self.gameover.change_scene:
            self.gameover.draw(self.window)
        elif self.game.scene_type == "win" and not self.winner.change_scene:
            self.winner.draw(self.window)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.winner.change_scene = False
            self.game.player.vida = 20
            self.game.player.pts = 0
            self.game.scene_type = None

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if not self.menu.change_scene:
                self.menu.events(events)
            elif not self.game.change_scene:
                self.game.player.move_player(events)
            elif not self.winner.change_scene:
                self.winner.events(events)
            else:
                self.gameover.events(events)

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()


game = Main(400, 566, "Environmental cleaning")
game.update()

