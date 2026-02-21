import pygame

class fifthquestion:
    def __init__(self, controller):
    
        self.controller = controller
        self.screen = controller.screen
        self.done = False

        self.font = pygame.font.SysFont(None, 40)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # might change to button
                self.done = True
                self.is_done()

        

    def update(self, fr):
        pass

    def draw(self, screen):
        self._render_title(screen)

    def _render_title(self, screen):
        text = self.font.render("Fifth Question", True, (255,255,255))
        screen.blit(text, (250, 300))

    def is_done(self):
        return self.done