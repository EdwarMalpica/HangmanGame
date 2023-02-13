import pygame, sys

from view.Player import Player

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class MainView:

    """
    game: inicializa Pygame.
    screen: establece el tamaño de la ventana del juego en 700x512 píxeles.
    clock: controla la tasa de refresco del juego.
    player: un objeto de la clase Player que se utiliza para dibujar el jugador.
    game_over: una bandera que indica si el juego ha terminado.
    background: la imagen de fondo que se muestra en la ventana del juego.
    sounBack: el sonido de fondo que se reproducirá mientras el juego esté en curso.
    """
    def __init__(self):
        self.game = pygame.init()
        self.screen = pygame.display.set_mode((700,512))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.game_over = False
        self.background = pygame.image.load("assets/img/FondoJuego.png").convert()
        self.sounBack = pygame.mixer.Sound("assets/sound/Back.mp3")


    """ 
         este es el bucle principal del juego. Mientras la bandera "game_over"
          sea falsa, se llamarán los métodos eventsControl y "initComponents.
    """
    def mainLoop(self):
        self.sounBack.play(loops=20)
        while not self.game_over:
            self.eventsControl()
            self.initComponents()
            print(pygame.mouse.get_pos())
        pygame.quit()

    """
    controla los eventos que ocurren en el juego, como cerrar la ventana o presionar una tecla.
    """
    def eventsControl(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.addArm()

    """
    dibuja la imagen de fondo y el jugador en la pantalla y actualiza el juego.
    """
    def initComponents(self):
        self.screen.blit(self.background, [0, 0])
        self.player.drawPlayer(self.screen)
        pygame.display.flip()
        self.clock.tick(30)



mainVies = MainView()
mainVies.mainLoop()

