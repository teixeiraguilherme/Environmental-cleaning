import pygame
from ranking import load_ranking
from obj import Obj, Texto


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
        self.btn_easy = pygame.Rect(84, 227, 230, 30)
        self.btn_medium = pygame.Rect(84, 296, 230, 30)
        self.btn_hard = pygame.Rect(84, 368, 230, 30)
        self.btn_free = pygame.Rect(84, 437, 230, 30)

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse= pygame.mouse.get_pos()
            
            if self.btn_easy.collidepoint(pos_mouse):
                self.escolha = "easy"
                self.change_scene = True

            elif self.btn_medium.collidepoint(pos_mouse):
                self.escolha= "medium"
                self.change_scene = True

            elif self.btn_hard.collidepoint(pos_mouse):
                self.escolha = "hard"
                self.change_scene = True
            
            elif self.btn_free.collidepoint(pos_mouse):
                self.escolha = "free"
                self.change_scene = True

class NameScreen(Menu):
    def __init__(self, image):
        super().__init__(image)
        self.input_name = ""
        self.text_display = Texto(30, "", (255,255,255))

    def draw(self, window):
        self.bg.group.draw(window)
        self.text_display.draw(window, 124, 285) 
        
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.input_name.strip() != "":
                    self.change_scene = True
            elif event.key == pygame.K_BACKSPACE:
                self.input_name = self.input_name[:-1]
            else:
                if len(self.input_name) < 10:
                    if event.unicode.isalnum() or event.unicode in ('_', '-'):
                        self.input_name += event.unicode.upper()
            self.text_display.update_texto(self.input_name)

class ScoreScreen(Menu):
    def __init__(self, image):
        super().__init__(image)
        self.final_score = 0
        self.ranking_position = "..."
        self.name = ""
        self.score_text = Texto(40, "0", (255,255,255))
        self.position_text = Texto(40, "POSITION: ...", (255,255,255))
        self.next_action = None

        self.btn_ranking = pygame.Rect(101, 371, 200, 25) 
        self.btn_play = pygame.Rect(101, 418, 200, 25) 

        self.next_action = None 

    def draw(self, window):
        self.bg.group.draw(window)
        
        self.position_text.draw(window, 206,177)
        self.score_text.draw(window, 185, 256)

    def update_data(self, score, name, position="..."):
        self.final_score = score
        self.name = name
        self.ranking_position = position
        self.score_text.update_texto(f"{self.final_score}")
        self.position_text.update_texto(f"{self.ranking_position}")

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.next_action = "reset"
                self.change_scene = True
                self.ranking_position = "..."
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()

            if self.btn_play.collidepoint(pos_mouse):
                self.next_action = "play_free"
                self.change_scene = True
                self.ranking_position = "..."

            elif self.btn_ranking.collidepoint(pos_mouse):
                self.next_action = "view_ranking"
                self.change_scene = True
                self.ranking_position = "..."

class RankingScreen(Menu):
    def __init__(self, image):
        super().__init__(image)
        self.ranking_data = None 
        self.text_entries = []  
        self.start_x = 60
        self.start_y = 130
        self.line_height = 35

    def load_ranking_data(self):

        self.ranking_data = load_ranking()
        self.text_entries.clear()
        
        if not self.ranking_data:
            self.text_entries.append(Texto(22, "NENHUM JOGADOR NO RANKING", (255,255,255)))
            return

        for i, entry in enumerate(self.ranking_data):
            pos = i + 1
            name = entry['name'][:12] 
            score = entry['score']
            text_line = f"{pos:2}. {name:<12} {score:>5}"
            self.text_entries.append(Texto(35, text_line, (0, 0, 0)))
            
    def draw(self, window):
        self.bg.group.draw(window)
        
        for i, text_obj in enumerate(self.text_entries):
            y_pos = self.start_y + (i * self.line_height)
            text_obj.draw(window, self.start_x, y_pos)

    def events(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.change_scene = True
            self.ranking_data = None 
            self.text_entries.clear()