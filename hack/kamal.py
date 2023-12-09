import pygame
import sys
import pygame.mixer
import time

pygame.init()
pygame.mixer.init()

# Определение цветов
WHITE = pygame.Color(255, 255, 255, 0)
BLACK = (0, 0, 0)

# Размеры экрана
WIDTH, HEIGHT = 800, 600
FPS = 60
SCALE_WIDTH = 250
SCALE_HEIGHT = 40
SCALE_COLOR = (100, 255, 70)
FPS_CLOCK = pygame.time.Clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpisMan")

# Загрузка изображения заднего фона
background_image = pygame.image.load('photo/back.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# шкала
flag = False
shkala = SCALE_WIDTH // 2  # Start the progress bar at half its width
progress = shkala / SCALE_WIDTH
font = pygame.font.Font(None, 30)
text_surface = font.render("cheated successfully", True, (0, 0, 0))
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 12.5))
# Загрузка и воспроизведение музыки на заднем фоне
pygame.mixer.music.load('sounds/sound.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Игровые объекты
teacher_width, teacher_height = 150, 100

proctor_avinash = [
    {'x': WIDTH - teacher_width - 435, 'y': 150, 'speed': 2, 'direction': 'up',
     'image': pygame.image.load('photo/avi1.png')},
]

proctor_arnurka = [
    {'x': WIDTH - teacher_width - 700, 'y': 150, 'speed': 2, 'direction': 'down',
     'image': pygame.image.load('photo/arni1.png')},
]
desk_size = 30
num_desks_length = 5
num_desks_width = 5
desk_spacing_length = WIDTH // (num_desks_length + 1)
desk_spacing_width = int(HEIGHT * 0.6) // (num_desks_width + 1)

move_amount = 100
move_amount_pairs = {'x': 50, 'y': 50}

# Загрузка изображения студента
student_image = pygame.image.load('photo/parta1.png')
student_image = pygame.transform.scale(student_image, (150, 100))

# Обновление координат для всех ячеек столов
desks = [{'x': i * desk_spacing_length - move_amount + move_amount_pairs['x'],
          'y': j * desk_spacing_width + 225 - move_amount + move_amount_pairs['y'],
          'occupied': False} for i in range(1, num_desks_length + 1) for j in range(1, num_desks_width + 1)]

# Игровой цикл
clock = pygame.time.Clock()
running = True
clicked_desk = None

def show_menu():
    pygame.mixer.music.load('sounds/menu.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    play_image = pygame.image.load('photo/start.png')
    play_image = pygame.transform.scale(play_image, (100, 50))
    play_rect = play_image.get_rect()
    play_rect.center = (WIDTH // 2, HEIGHT // 2 - 75)

    quit_image = pygame.image.load('photo/exit.png')
    quit_image = pygame.transform.scale(quit_image, (100, 50))
    quit_rect = quit_image.get_rect()
    quit_rect.center = (WIDTH // 2, HEIGHT // 2 + 35)

    rules_image = pygame.image.load('photo/rules.png')
    rules_image = pygame.transform.scale(rules_image, (100, 100))
    rules_rect = rules_image.get_rect()
    rules_rect.center = (WIDTH // 2, HEIGHT // 2 - 20)

    menu_back = pygame.image.load('photo/menu.png')
    menu_back = pygame.transform.scale(menu_back, (WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()  # Stop the menu music
                    return
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif rules_rect.collidepoint(event.pos):
                    show_rules_window()

        screen.blit(menu_back, (0, 0))
        screen.blit(play_image, play_rect)
        screen.blit(quit_image, quit_rect)
        screen.blit(rules_image, rules_rect)

        pygame.display.flip()
def show_rules_window():
    rules_window_surface = pygame.Surface((WIDTH, HEIGHT))
    rules_window_image = pygame.image.load('photo/rules_window.png')
    rules_window_image = pygame.transform.scale(rules_window_image, (WIDTH, HEIGHT))
    rules_window_surface.blit(rules_window_image, (0, 0))

    rules_text = ["*                                                   *",
                "*                                                   *",
                "*                                                   *",
                "*                                                   *",
                "You have to help students cheat on the end-term test.",
                "To do this, you must click and hold on any of the students.",
                "As soon as you click and hold, the scale on top of the",
                "window will start to increase. Note that as soon as you ",
                "stop pressing on to a student, your scale will begin to ",
                "decrease (you can press and hold on any student, even if",
                "you click on all those sitting in turn). When the proctor",
                "approaches the desk of the student you are helping to",
                "cheat, you lose. Your goal is not to let this scale ",
                "reach zero and not getting caught by proctors.",
                "Time to fill the scale: 30 seconds"]
        
    # Добавим кнопку "В главное меню"
    font = pygame.font.Font(None, 30)
    text_surfaces = [font.render(line, True, BLACK) for line in rules_text]
    text_rects = [text_surface.get_rect(center=(WIDTH // 2, 50 + i * 30)) for i, text_surface in enumerate(text_surfaces)]
    back_to_menu_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 50, 200, 40)
    back_to_menu_color = (100, 100, 100)
    font = pygame.font.Font(None, 30)
    button_text = font.render("EXIT", True, (255, 255, 255))
    button_text_rect = button_text.get_rect(center=back_to_menu_button.center)

    show_rules = True  # Объявляем переменную show_rules перед циклом

    while show_rules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_to_menu_button.collidepoint(event.pos):
                    show_rules = False

        screen.blit(rules_window_surface, (0, 0))

        # Отображаем текстовую поверхность с правилами
        for text_surface, text_rect in zip(text_surfaces, text_rects):
            screen.blit(text_surface, text_rect)

        # Отрисовываем кнопку "В главное меню"
        pygame.draw.rect(screen, back_to_menu_color, back_to_menu_button)
        screen.blit(button_text, button_text_rect)

        pygame.display.flip()

    # Отображаем текстовую поверхность с правилами
    for text_surface, text_rect in zip(text_surfaces, text_rects):
        screen.blit(text_surface, text_rect)

    # Отрисовываем кнопку "В главное меню"
    pygame.draw.rect(screen, back_to_menu_color, back_to_menu_button)
    screen.blit(button_text, button_text_rect)

    pygame.display.flip()

def show_game_over_window():
    # Создаем поверхность с белым цветом
    game_over_surface = pygame.Surface((WIDTH, HEIGHT))
    game_over_surface.fill(WHITE)

    # Загружаем изображение "game_over_image"
    game_over_image = pygame.image.load('photo/gameover.png')
    game_over_image = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

    show_game_over = True
    
    while show_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                show_game_over = False

        # Отображаем белую поверхность
        screen.blit(game_over_surface, (0, 0))

        # Отображаем изображение "game_over_image" поверх белой поверхности
        screen.blit(game_over_image, (0, 0))
        pygame.display.flip()

# Call the show_menu function
show_menu()
# Set up the game music after returning from the menu
pygame.mixer.music.load('sounds/sound.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Таймер на 10 секунд перед началом игры
start_time = time.time()
end_time = start_time + 30  # 30 секунд на заполнение шкалы

while time.time() - start_time < 10:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.blit(background_image, (0, 0))
    font = pygame.font.Font(None, 100)
    timer_text = font.render(str(int(10 - (time.time() - start_time))), True, WHITE)
    screen.blit(timer_text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))

    pygame.display.flip()
    clock.tick(60)

# Основной цикл после таймера
while running and 0 <= progress <= 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for desk in desks:
                if desk['x'] < event.pos[0] < desk['x'] + 150 and desk['y'] < event.pos[1] < desk['y'] + 100:
                    clicked_desk = desk
                    break
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            clicked_desk = None

    for teacher in proctor_avinash:
        if teacher['direction'] == 'up':
            teacher['y'] -= teacher['speed']
            if teacher['y'] <= 160:
                teacher['direction'] = 'right'
                teacher['image'] = pygame.image.load('photo/avi4.png')
        elif teacher['direction'] == 'right':
            teacher['x'] += teacher['speed']
            if teacher['x'] >= WIDTH - teacher_width - 365:
                teacher['direction'] = 'down'
                teacher['image'] = pygame.image.load('photo/avi1.png')
        elif teacher['direction'] == 'down':
            teacher['y'] += teacher['speed']
            if teacher['y'] >= HEIGHT - teacher_height - 0:
                teacher['direction'] = 'left'
                teacher['image'] = pygame.image.load('photo/avi3.png')
        elif teacher['direction'] == 'left':
            teacher['x'] -= teacher['speed']
            if teacher['x'] <= 145:
                teacher['direction'] = 'up'
                teacher['image'] = pygame.image.load('photo/avi2.png')
        if clicked_desk and (
            clicked_desk['x'] - teacher_width < teacher['x'] < clicked_desk['x'] + 150 and
            clicked_desk['y'] - teacher_height < teacher['y'] < clicked_desk['y'] + 100
        ):
            show_game_over_window()
            running = False  # Завершение игры, если учитель проходит рядом с партой
        for teacher in proctor_arnurka:
            if teacher['direction'] == 'up':
                teacher['y'] -= teacher['speed']
            if teacher['y'] <= 160:
                teacher['direction'] = 'right'
                teacher['image'] = pygame.image.load('photo/arni4.png')
            elif teacher['direction'] == 'right':
                teacher['x'] += teacher['speed']
            if teacher['x'] >= WIDTH - teacher_width - 100:
                teacher['direction'] = 'down'
                teacher['image'] = pygame.image.load('photo/arni1.png')
            elif teacher['direction'] == 'down':
                teacher['y'] += teacher['speed']
            if teacher['y'] >= HEIGHT - teacher_height - 0:
                teacher['direction'] = 'left'
                teacher['image'] = pygame.image.load('photo/arni3.png')
            elif teacher['direction'] == 'left':
                teacher['x'] -= teacher['speed']
            if teacher['x'] <= 420:
                teacher['direction'] = 'up'
                teacher['image'] = pygame.image.load('photo/arni2.png')
        if clicked_desk and (
            clicked_desk['x'] - teacher_width < teacher['x'] < clicked_desk['x'] + 150 and
            clicked_desk['y'] - teacher_height < teacher['y'] < clicked_desk['y'] + 100
        ):
            show_game_over_window()

   

            running = False  # Завершение игры, если учитель проходит рядом с партой

    if clicked_desk and shkala < SCALE_WIDTH:
        shkala += (5 / 30)
        progress = shkala / SCALE_WIDTH
    elif shkala > 0:
        shkala -= (2 / 30)
        progress = shkala / SCALE_WIDTH

    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, SCALE_COLOR,
                     (WIDTH // 2 - SCALE_WIDTH // 2, HEIGHT // 12.5 - SCALE_HEIGHT // 2, shkala, SCALE_HEIGHT))
    for desk in desks:
        if not desk['occupied']:
            if desk == clicked_desk:
                screen.blit(pygame.image.load('photo/parta2.png'), (desk['x'], desk['y']))
            else:
                screen.blit(student_image, (desk['x'], desk['y']))

    for teacher in proctor_avinash:
        screen.blit(pygame.transform.scale(teacher['image'], (teacher_width, teacher_height)),
                    (teacher['x'], teacher['y']))

    for teacher in proctor_arnurka:
        screen.blit(pygame.transform.scale(teacher['image'], (teacher_width, teacher_height)),
                    (teacher['x'], teacher['y']))
    if shkala >= SCALE_WIDTH:
        screen.blit(text_surface, text_rect)

    if progress == 0:
        print("Game Over: Progress bar is empty!")
        running = False
    elif progress == 1:
        print("Congratulations! You cheated successfully!")
        running = False

    pygame.display.flip()
    clock.tick(60)

if progress == 1:
    # Stop the music
    pygame.mixer.music.stop()
    # Display winning image
    final_won = pygame.image.load('photo/win.png')
    screen.blit(final_won, (0, 0))
elif progress == 0:
    # Stop the music
    pygame.mixer.music.stop()
    # Display losing image
    final_lost = pygame.image.load('photo/gameover.png')
    screen.blit(final_lost, (0, 0)) # Replace with the actual image path



pygame.quit()
sys.exit()