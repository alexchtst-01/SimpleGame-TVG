import sys
import random
import pygame

pygame.init()

W, H = 800, 600
GRID_SIZE = 25

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, GREEN]

def main():
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Tugas TVG")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        
        pygame.draw.rect(screen, GREEN, (W // 2 - 50, H // 2 - 50, 100, 100))
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()