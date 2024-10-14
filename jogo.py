import pygame
import pymunk

# Classe Tela
class Tela:
    def __init__(self, cor_de_fundo, indice_tela, indice_proxima_tela):
        self.cor_de_fundo = cor_de_fundo
        self.indice_tela = indice_tela
        self.indice_proxima_tela = indice_proxima_tela

    def desenha(self, window):
        window.fill(self.cor_de_fundo)
        pygame.display.update()

    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

# Classe Jogo
class Jogo:
    def __init__(self):
        pygame.init()
        self.largura_janela = 1000
        self.altura_janela = 650
        self.window = pygame.display.set_mode((self.largura_janela, self.altura_janela))
        self.clock = pygame.time.Clock()
        self.raposa_principal = pygame.image.load()

        # Define as telas
        self.tela_inicial = Tela((0, 0, 0), 0, 1)  # Tela verde
        
        # Lista de telas
        self.telas = [self.tela_inicial]
        self.indice_tela_atual = 0

    def roda(self):
        rodando = True
        while rodando:
            tela_atual = self.telas[self.indice_tela_atual]
            
            rodando = tela_atual.atualiza()  # Atualiza eventos e verifica se ainda deve rodar
            tela_atual.desenha(self.window)  # Desenha a tela atual

            self.clock.tick(60)  # Mantém o jogo rodando a 60 FPS

# Classe Pássaro
class Passaro:
    def __init__(self, x, y):
        self.body = pymunk.Body(1, 1666)  # Massa e momento de inércia
        self.body.position = (x, y)
        self.shape = pymunk.Circle(self.body, 15)  # Define o pássaro como um círculo com raio 15

# Classe Monstro
class Monstro:
    def __init__(self, x, y):
        self.body = pymunk.Body(1, 1666)
        self.body.position = (x, y)
        self.shape = pymunk.Circle(self.body, 20)

# Classe Madeira
class Madeira:
    def __init__(self, x1, y1, x2, y2, largura):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.shape = pymunk.Segment(self.body, (x1, y1), (x2, y2), largura)

if __name__ == '__main__':
    Jogo().roda()