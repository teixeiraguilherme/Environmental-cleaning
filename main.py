import pygame
from menu import Menu, Gameover, Vitoria, Level, NameScreen, ScoreScreen, RankingScreen
from game import Game
from ranking import add_score_to_ranking

class Main:

    def __init__(self, sizex, sizey, title):

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/som/musica.mp3")
        pygame.mixer.music.play(-1)

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu("assets/png/menu.png")
        self.gameover = Gameover("assets/png/gameover.png")
        self.game = None
        self.winner = Vitoria("assets/png/win.png")
        self.level = Level("assets/png/level.png")
        self.name_screen = NameScreen("assets/png/name.png")
        self.score_screen = ScoreScreen("assets/png/score.png")
        self.ranking_screen = RankingScreen("assets/png/ranking.png")


        self.player_name = None
        self.level_choice = None

        self.loop = True
        self.fps = pygame.time.Clock()

    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)

        elif not self.level.change_scene:
            self.level.draw(self.window)

        elif self.level_choice == "free" and not self.name_screen.change_scene:
            self.name_screen.draw(self.window)

        elif self.game is not None and not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()

        elif self.game is not None and self.game.change_scene and self.level_choice == "free" and not self.score_screen.change_scene:
            if self.score_screen.ranking_position == "...":
                position = add_score_to_ranking(self.player_name, self.game.player.pts, self.level_choice)
                self.score_screen.update_data(self.game.player.pts, self.player_name, position)
            self.score_screen.draw(self.window)

        elif self.score_screen.next_action == "view_ranking" and not self.ranking_screen.change_scene:
            if self.ranking_screen.ranking_data is None: 
                self.ranking_screen.load_ranking_data() 
            self.ranking_screen.draw(self.window)

        elif self.ranking_screen.change_scene:
            self.ranking_screen.change_scene = False
            self.score_screen.next_action = None
            self.score_screen.change_scene = False

        elif self.level_choice == "free" and not self.score_screen.change_scene:
            pass

        elif self.game is not None and self.game.scene_type == "gameover" and self.level_choice != "free" and not self.gameover.change_scene:
            self.gameover.draw(self.window)

        elif self.game is not None and self.game.scene_type == "win" and self.level_choice != "free" and not self.winner.change_scene:
            self.winner.draw(self.window)
        else:
            if self.level_choice == "free" and self.score_screen.next_action == "play_free":
                self.game.player.vida = 5
                self.game.player.pts = 0
                self.game.scene_type = None
                self.game.change_scene = False
                self.ranking_screen.change_scene = False
                self.score_screen.change_scene = False
                self.score_screen.next_action = None
                self.game = Game("free", self.player_name)
                return

            self.menu.change_scene = False
            self.level.change_scene = False
            self.ranking_screen.change_scene = False
            self.name_screen.change_scene = False
            self.gameover.change_scene = False
            self.winner.change_scene = False
            self.score_screen.change_scene = False
            self.score_screen.next_action = None
            
            if self.game is not None:
                self.game.player.vida = 5
                self.game.player.pts = 0
                self.game.scene_type = None
            
            self.game = None
            self.player_name = None
            self.level_choice = None
            self.name_screen.input_name = ""
            self.name_screen.text_display.update_texto("")

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

            if not self.menu.change_scene:
                self.menu.events(events)

            elif not self.level.change_scene:
                self.level.events(events)
                if self.level.change_scene:
                    self.level_choice = self.level.escolha
                    if self.level_choice != "free":
                        self.game = Game(self.level_choice, self.player_name)

            elif self.level_choice == "free" and not self.name_screen.change_scene:
                self.name_screen.events(events)
                if self.name_screen.change_scene:
                    self.player_name = self.name_screen.input_name
                    self.game = Game(self.level_choice, self.player_name)

            elif self.score_screen.next_action == "view_ranking" and not self.ranking_screen.change_scene:
                self.ranking_screen.events(events)

            elif self.game is not None and not self.game.change_scene:
                self.game.player.move_player(events)

            elif self.game is not None and self.game.change_scene and self.level_choice == "free" and not self.score_screen.change_scene:
                self.score_screen.events(events)

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

