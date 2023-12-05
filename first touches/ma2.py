import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 600
FPS = 60
SCALE_WIDTH = 400
SCALE_HEIGHT = 50
SCALE_COLOR = (0, 255, 0)
BACKGROUND_COLOR = (255, 255, 255)
FPS_CLOCK = pygame.time.Clock()
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("лялялялялял я усталь")

flag = False
shkala = 0
progress = 0 
font = pygame.font.Font(None, 36)
text_surface = font.render("читед саксесфулльи", True, (0, 0, 255))
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            flag = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            flag = False
            
           


    if flag and shkala < SCALE_WIDTH:
        shkala += 5  
        progress = shkala / SCALE_WIDTH
    
    
 
    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(screen, SCALE_COLOR, (WIDTH // 2 - SCALE_WIDTH // 2, HEIGHT // 2 - SCALE_HEIGHT // 2, shkala, SCALE_HEIGHT))
    if shkala >= SCALE_WIDTH:
        screen.blit(text_surface, text_rect)

    if progress >= 1:  
        screen.blit(text_surface, text_rect)
        screen.blit(text_surface, text_rect)
    pygame.display.flip()
    FPS_CLOCK.tick(FPS)
