def show_you_won_window():
    
    # Создаем поверхность с белым цветом
    won_surface = pygame.Surface((WIDTH, HEIGHT))
    won_surface.fill(WHITE)

    # Загружаем изображение "won_image"
    won_image = pygame.image.load('photo/win.png')
    won_image = pygame.transform.scale(won_image, (WIDTH, HEIGHT))

    show_won = True
    
    while show_won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                show_won = False

        # Отображаем белую поверхность
        screen.blit(won_surface, (0, 0))

        # Отображаем изображение "won_image" поверх белой поверхности
        screen.blit(won_image, (0, 0))

        pygame.display.flip()