from obj import Obj, Player, Texto
import random

class Game:

    def __init__(self, level = "easy"):
        
        self.bg = Obj("assets/png/background.png", 0, 0)
        self.level = level
        if level == "easy":
            self.velocidade = 7
            self.meta_pontos = 20
            self.tem_peixe_um = False
            self.tem_peixe_dois = False

        if level == "medium":
            self.velocidade = 8
            self.meta_pontos = 40
            self.tem_peixe_um = True
            self.tem_peixe_dois= False
        
        if level == "hard":
            self.velocidade = 9.5
            self.meta_pontos = 60
            self.tem_peixe_um = True
            self.tem_peixe_dois = True


        self.papel = Obj("assets/png/papel.png", random.randrange(0, 330), random.randrange (-100,-50))
        self.metal = Obj("assets/png/metal.png", random.randrange(0, 330), random.randrange (-100,-50))
        self.garrafa = Obj("assets/png/garrafa.png", random.randrange(0, 330),random.randrange (-100,-50))
        self.vidro = Obj("assets/png/vidro.png", random.randrange(0, 130), random.randrange (-100,-50))
        self.maca = Obj("assets/png/maca.png", random.randrange(0, 130), random.randrange (-100,-50))
        self.peixe_um = Obj("assets/png/peixe1.png", random.randrange(0, 130),random.randrange (-100,-50))
        self.peixe_dois = Obj("assets/png/peixe2.png", random.randrange(0, 130), random.randrange (-100,-50))
        self.player = Player("assets/png/lixeira.png", 250, 670)

    
        self.change_scene = False
        self.scene_type = None

        self.score = Texto(110, "0")
        self.vidas = Texto(50, "5")

    def draw(self, window):
        self.bg.drawing(window)
        self.vidro.drawing(window)
        self.papel.drawing(window)
        self.metal.drawing(window)
        self.maca.drawing(window)
        if self.tem_peixe_um:
            self.peixe_um.drawing(window)
        if self.tem_peixe_dois:
            self.peixe_dois.drawing(window)
        self.garrafa.drawing(window)
        self.player.drawing(window)
        self.score.draw(window, 150, 50)
        self.vidas.draw(window, 50, 50)

    def update(self):
        self.move_maca()
        self.move_garrafa()
        self.move_metal()
        self.move_papel()
        self.move_vidro()
        if self.tem_peixe_um:
            self.move_peixe_um()
            self.player.colisao_dano(self.peixe_um.group)
        if self.tem_peixe_dois:
            self.move_peixe_dois()
            self.player.colisao_dano(self.peixe_dois.group)
        self.player.colisao(self.metal.group)
        self.player.colisao(self.vidro.group)
        self.player.colisao(self.papel.group)
        self.player.colisao(self.maca.group)
        self.player.colisao(self.garrafa.group)
        
        self.game_over()
        self.winner()
        self.score.update_texto(str(self.player.pts))
        self.vidas.update_texto(str(self.player.vida))

    def move_peixe_um(self):
        if not self.peixe_um.group:
            self.peixe_um = Obj("assets/png/peixe1.png", random.randrange(0, 330), random.randrange (-100,-50))
        else:
            self.peixe_um.sprite.rect[1] += self.velocidade + 1
            if self.peixe_um.sprite.rect[1] >= 700:
                self.peixe_um.sprite.kill()
                self.peixe_um = Obj("assets/png/peixe1.png", random.randrange(0, 330), random.randrange (-100,-50))

    def move_peixe_dois(self):
        if not self.peixe_dois.group:
            self.peixe_dois = Obj("assets/png/peixe2.png", random.randrange(0, 330), random.randrange (-100,-50))
        else:
            self.peixe_dois.sprite.rect[1] += self.velocidade + 1
            if self.peixe_dois.sprite.rect[1] >= 700:
                self.peixe_dois.sprite.kill()
                self.peixe_dois = Obj("assets/png/peixe2.png", random.randrange(0, 330), random.randrange (-100,-50))

    def move_maca(self):
        if not self.maca.group:
            self.maca = Obj("assets/png/maca.png", random.randrange(150, 330), random.randrange (-100,-50))
        else:
            self.maca.sprite.rect[1] += self.velocidade
            if self.maca.sprite.rect[1] >= 700:
                self.player.vida -= 1
                self.player.sound_dano.play()
                self.maca.sprite.kill()
                self.maca = Obj("assets/png/maca.png", random.randrange(150, 330), random.randrange (-100,-50))

    def move_vidro(self):
        if not self.vidro.group:
            self.vidro = Obj("assets/png/vidro.png", random.randrange(150, 330), random.randrange (-100,-50))
        else:
            self.vidro.sprite.rect[1] += self.velocidade
            if self.vidro.sprite.rect[1] >= 700:
                self.player.vida -= 1
                self.player.sound_dano.play()
                self.vidro.sprite.kill()
                self.vidro = Obj("assets/png/vidro.png", random.randrange(150, 330), random.randrange (-100,-50))

    def move_garrafa(self):
        if not self.garrafa.group:
            self.garrafa = Obj("assets/png/garrafa.png", random.randrange(0, 330), random.randrange (-100,-50))
        else:
            self.garrafa.sprite.rect[1] += self.velocidade
            if self.garrafa.sprite.rect[1] >= 700:
                self.player.vida -= 1
                self.player.sound_dano.play()
                self.garrafa.sprite.kill()
                self.garrafa = Obj("assets/png/garrafa.png", random.randrange(0, 330), random.randrange (-100,-50))

    def move_metal(self):
        if not self.metal.group:
            self.metal = Obj("assets/png/metal.png", random.randrange(0, 330), random.randrange (-100,-50))
        else:
            self.metal.sprite.rect[1] += self.velocidade
            if self.metal.sprite.rect[1] >= 700:
                self.player.vida -= 1
                self.player.sound_dano.play()
                self.metal.sprite.kill()
                self.metal = Obj("assets/png/metal.png", random.randrange(0, 330), random.randrange (-100,-50))

    def move_papel(self):
        if not self.papel.group:
            self.papel = Obj("assets/png/papel.png", random.randrange(0, 130), random.randrange (-100,-50))
        else:
            self.papel.sprite.rect[1] += self.velocidade
            if self.papel.sprite.rect[1] >= 700:
                self.player.vida -= 1
                self.player.sound_dano.play()
                self.papel.sprite.kill()
                self.papel = Obj("assets/png/papel.png", random.randrange(0, 130), random.randrange (-100,-50))

    def game_over(self):
        if self.player.vida <= 0:
            self.change_scene = True
            self.scene_type = "gameover"

    def winner(self):
        if self.player.pts >= self.meta_pontos:
            self.change_scene = True
            self.scene_type = "win"