from obj import Obj, Player, Texto
import random

class Game:

    def __init__(self):
        
        self.bg = Obj("assets/png/background.png", 0, 0)

        self.papel = Obj("assets/png/papel.png", random.randrange(150, 330), -50)
        self.metal = Obj("assets/png/metal.png", random.randrange(0, 330), -50)
        self.garrafa = Obj("assets/png/garrafa.png", random.randrange(0, 330), -50)
        self.vidro = Obj("assets/png/vidro.png", random.randrange(0, 130), -50)
        self.maca = Obj("assets/png/maca.png", random.randrange(0, 130), -50)
        self.peixe_um = Obj("assets/png/peixe1.png", random.randrange(0, 130), -50)
        self.peixe_dois = Obj("assets/png/peixe2.png", random.randrange(0, 130), -50)
        self.player = Player("assets/png/lixeira.png", 250, 670)

        self.change_scene = False
        self.scene_type = None

        self.score = Texto(120, "0")
        self.vidas = Texto(60, "5")

    def draw(self, window):
        self.bg.drawing(window)
        self.vidro.drawing(window)
        self.papel.drawing(window)
        self.metal.drawing(window)
        self.maca.drawing(window)
        self.peixe_um.drawing(window)
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
        self.move_peixe_um()
        self.move_peixe_dois()
        self.player.colisao(self.metal.group)
        self.player.colisao(self.vidro.group)
        self.player.colisao(self.papel.group)
        self.player.colisao(self.maca.group)
        self.player.colisao(self.garrafa.group)
        self.player.colisao_dano(self.peixe_dois.group)
        self.player.colisao_dano(self.peixe_um.group)
        self.game_over()
        self.winner()
        self.score.update_texto(str(self.player.pts))
        self.vidas.update_texto(str(self.player.vida))

    def move_peixe_um(self):
        if not self.peixe_um.group:
            self.peixe_um = Obj("assets/png/peixe_um.png", random.randrange(0, 330), -50)
        else:
            self.peixe_um.sprite.rect[1] += 8
            if self.peixe_um.sprite.rect[1] >= 700:
                self.peixe_um.sprite.kill()
                self.peixe_um = Obj("assets/png/peixe_um.png", random.randrange(0, 330), -50)

    def move_peixe_dois(self):
        if not self.peixe_dois.group:
            self.peixe_dois = Obj("assets/png/peixe_dois.png", random.randrange(0, 330), -50)
        else:
            self.peixe_dois.sprite.rect[1] += 8
            if self.peixe_dois.sprite.rect[1] >= 700:
                self.peixe_dois.sprite.kill()
                self.peixe_dois = Obj("assets/png/peixe_dois.png", random.randrange(0, 330), -50)

    def move_maca(self):
        # Primeiro, checa se o grupo da maçã está vazio (foi coletada)
        if not self.maca.group:
            # Se sim, cria uma nova maçã no topo
            self.maca = Obj("assets/png/maca.png", random.randrange(150, 330), -50)
        else:
            # Se não, o objeto ainda existe. Movemos ele.
            self.maca.sprite.rect[1] += 8
            # E checamos se ele saiu da tela (foi perdido)
            if self.maca.sprite.rect[1] >= 700:
                self.player.vida -= 1
                self.player.sound_dano.play()
                self.maca.sprite.kill()
                # Cria uma nova maçã no topo
                self.maca = Obj("assets/png/maca.png", random.randrange(150, 330), -50)

    def move_vidro(self):
        # Checa se foi coletado
        if not self.vidro.group:
            self.vidro = Obj("assets/png/vidro.png", random.randrange(150, 330), -50)
        else:
            # Move e checa se foi perdido
            self.vidro.sprite.rect[1] += 8
            if self.vidro.sprite.rect[1] >= 700:
                self.player.vida -= 1
                self.player.sound_dano.play()
                self.vidro.sprite.kill()
                self.vidro = Obj("assets/png/vidro.png", random.randrange(150, 330), -50)

    def move_garrafa(self):
        # Checa se foi coletado
        if not self.garrafa.group:
            self.garrafa = Obj("assets/png/garrafa.png", random.randrange(0, 330), -50)
        else:
            # Move e checa se foi perdido
            self.garrafa.sprite.rect[1] += 8
            if self.garrafa.sprite.rect[1] >= 700:
                self.player.vida -= 1
                self.player.sound_dano.play()
                self.garrafa.sprite.kill()
                self.garrafa = Obj("assets/png/garrafa.png", random.randrange(0, 330), -50)

    def move_metal(self):
        # Checa se foi coletado
        if not self.metal.group:
            self.metal = Obj("assets/png/metal.png", random.randrange(0, 330), -50)
        else:
            # Move e checa se foi perdido
            self.metal.sprite.rect[1] += 8
            if self.metal.sprite.rect[1] >= 700:
                self.player.vida -= 1
                self.player.sound_dano.play()
                self.metal.sprite.kill()
                self.metal = Obj("assets/png/metal.png", random.randrange(0, 330), -50)

    def move_papel(self):
        if not self.papel.group:
            self.papel = Obj("assets/png/papel.png", random.randrange(0, 130), -50)
        else:
            self.papel.sprite.rect[1] += 8
            if self.papel.sprite.rect[1] >= 700:
                self.player.vida -= 1
                self.player.sound_dano.play()
                self.papel.sprite.kill()
                self.papel = Obj("assets/png/papel.png", random.randrange(0, 130), -50)

    def game_over(self):
        if self.player.vida <= 0:
            self.change_scene = True
            self.scene_type = "gameover"

    def winner(self):
        if self.player.pts >= 15:
            self.change_scene = True
            self.scene_type = "win"