import pygame

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width* scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.soundClick = pygame.mixer.Sound("assets/sound/clickHover.mp3")

    def draw(self, screen):
        action = False
        #Obtener la posicion del mouse
        pos = pygame.mouse.get_pos()
        #Verificar si el mouse esta en condicione de click
        if self.rect.collidepoint(pos):

            """if pygame.mouse.get_cursor() == pygame.cursors.diamond:
                pass
            else:
                pygame.mouse.set_cursor(pygame.cursors.diamond)
            """
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.soundClick.play()
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            #Dibujar Boton en pantalla
        """else:
            if pygame.mouse.get_cursor() == pygame.cursors.arrow:
                pass
            else:
                pygame.mouse.set_cursor(pygame.cursors.arrow)
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action