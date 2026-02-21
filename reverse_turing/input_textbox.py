import pygame

class Input_textbox:
    def __init__(self, screen, text="", x=25, y=660, width=750, size=30, padding=10):
        self.screen = screen
        self.text = text
        self.x = x 
        self.y = y 
        self.width = width
        self.size = size
        self.padding = padding
        
        self.font = pygame.font.Font(pygame.font.get_default_font(), size)
        
        # Calculate fixed height for exactly 3 lines
        self.line_height = self.font.get_linesize()
        
        # This rect defines the physical box on the screen
        self.textbox_rect = pygame.Rect(self.x, self.y, self.width, self.line_height + self.padding)
        
        self.update_text(self.text)

    def update_text(self, text):
        self.text = text
        # Render the text surface
        self.font_surface = self.font.render(self.text, True, (255, 255, 255)) # Changed to white for visibility

        # Position the text rect at the top-left of our box, offset by padding
        # We use .topleft instead of .center to keep it left-aligned
        self.text_rect = self.font_surface.get_rect(
            topleft=(self.textbox_rect.x + self.padding, self.textbox_rect.y + self.padding)
        )

    def render(self):
        # 1. Draw the background box (dark gray)
        pygame.draw.rect(self.screen, (50, 50, 50), self.textbox_rect)
        
        # 2. Draw the border (light gray)
        pygame.draw.rect(self.screen, (150, 150, 150), self.textbox_rect, 2)

        # 3. Draw the text surface at its calculated position
        self.screen.blit(self.font_surface, self.text_rect)
        