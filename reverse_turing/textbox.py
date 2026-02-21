import pygame

class Textbox:
    def __init__(self, screen, text=None, x=25, y=500, width=750, size = 30, padding=10):
        self.screen = screen
        self.text = text
        self.x = x  # This is now the LEFT position
        self.y = y  # This is now the TOP position
        self.width = width
        self.size = size
        self.padding = padding
        
        self.font = pygame.font.Font(pygame.font.get_default_font(), size)
        
        # Calculate fixed height for exactly 3 lines
        self.line_height = self.font.get_linesize()
        self.fixed_height = (self.line_height * 3) + (self.padding * 2)
        
        # Define the fixed box area once
        self.textbox_rect = pygame.Rect(self.x, self.y, self.width, self.fixed_height)
        self.update_text(self.text)

    def update_text(self, text):
        # Split text and render each line
        self.text = text
        
        words = self.text.split(' ')
        self.surfaces = []
        
        line = ""
        for word in words:
            if len(word) + len(line) < 52:
                line = line + " " + word
            else:
                surf = self.font.render(line.strip(), True, (255, 255, 255))
                self.surfaces.append(surf)
                line = ""
        if len(line) != 0:
            surf = self.font.render(line.strip(), True, (255, 255, 255))
            self.surfaces.append(surf)

    def render(self):
        
        # Draw the fixed background box
        pygame.draw.rect(self.screen, (50,50,50), self.textbox_rect)
        # Optional: Add a border so the "fixed" shape is obvious
        pygame.draw.rect(self.screen, (150, 150, 150), self.textbox_rect, 2)
        
        # Start drawing at the top-left internal corner
        current_y = self.textbox_rect.top + self.padding
        left_margin = self.textbox_rect.left + self.padding
        
        for surf in self.surfaces:
            # Blit using topleft for "normal" left-aligned text
            self.screen.blit(surf, (left_margin, current_y))
            current_y += self.line_height