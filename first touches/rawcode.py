import pygame
import sys
import pygame.mixer
import time

pygame.init()
pygame.mixer.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Размеры экрана
WIDTH, HEIGHT = 800, 600

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpisMan")

# Загрузка изображения заднего фона
background_image = pygame.image.load('back.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Загрузка и воспроизведение музыки на заднем фоне
pygame.mixer.music.load('sound.mp3')  # Замените 'background_music.mp3' на путь к вашему аудиофайлу
pygame.mixer.music.set_volume(0.5)  # Устанавливаем громкость (от 0.0 до 1.0)
pygame.mixer.music.play(-1)  # -1 означает бесконечное воспроизведение

# Игровые объекты
teacher_width, teacher_height = 44, 44

teachers_male = [
    {'x': WIDTH - teacher_width - 420, 'y': 250, 'speed': 4, 'direction': 'up', 'image': pygame.image.load('avi.png')},
]

teachers_female = [
    {'x': WIDTH - teacher_width - 160, 'y': 250, 'speed': 4, 'direction': 'down', 'image': pygame.image.load('avi.png')},
]

desk_size = 30
num_desks_length = 5
num_desks_width = 5
desk_spacing_length = WIDTH // (num_desks_length + 1)
desk_spacing_width = int(HEIGHT * 0.6) // (num_desks_width + 1)  # Уменьшаем высоту периметра на 40%

# Загрузка изображения студента
student_image = pygame.image.load('parta.png')
student_image = pygame.transform.scale(student_image, (50, 50))

desks = [{'x': i * desk_spacing_length, 'y': j * desk_spacing_width + 225, 'occupied': False} for i in
         range(1, num_desks_length + 1) for j in range(1, num_desks_width + 1)]

# Игровой цикл
clock = pygame.time.Clock()
running = True

# Таймер на 10 секунд перед началом игры
start_time = time.time()
while time.time() - start_time < 10:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Отрисовка заднего фона
    screen.blit(background_image, (0, 0))

    # Отрисовка таймера в центре экрана
    font = pygame.font.Font(None, 100)
    timer_text = font.render(str(int(10 - (time.time() - start_time))), True, WHITE)
    screen.blit(timer_text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))

    pygame.display.flip()
    clock.tick(60)

# Основной цикл после таймера
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Движение учителей по измененному периметру прямоугольника
    for teacher in teachers_male:
        if teacher['direction'] == 'up':
            teacher['y'] -= teacher['speed']
            if teacher['y'] <= 230:  # сверху
                teacher['direction'] = 'right'
        elif teacher['direction'] == 'right':
            teacher['x'] += teacher['speed']
            if teacher['x'] >= WIDTH - teacher_width - 420:  # справа
                teacher['direction'] = 'down'
        elif teacher['direction'] == 'down':
            teacher['y'] += teacher['speed']
            if teacher['y'] >= HEIGHT - teacher_height - 10:  # от низа
                teacher['direction'] = 'left'
        elif teacher['direction'] == 'left':
            teacher['x'] -= teacher['speed']
            if teacher['x'] <= 210:  # слева
                teacher['direction'] = 'up'

    for teacher in teachers_female:
        if teacher['direction'] == 'up':
            teacher['y'] -= teacher['speed']
            if teacher['y'] <= 230:  # сверху
                teacher['direction'] = 'right'
        elif teacher['direction'] == 'right':
            teacher['x'] += teacher['speed']
            if teacher['x'] >= WIDTH - teacher_width - 160:  # справа
                teacher['direction'] = 'down'
        elif teacher['direction'] == 'down':
            teacher['y'] += teacher['speed']
            if teacher['y'] >= HEIGHT - teacher_height - 10:  # от низа
                teacher['direction'] = 'left'
        elif teacher['direction'] == 'left':
            teacher['x'] -= teacher['speed']
            if teacher['x'] <= 450:  # слева
                teacher['direction'] = 'up'

    # Отрисовка заднего фона
    screen.blit(background_image, (0, 0))

    # Отрисовка игровых объектов
    for desk in desks:
        pygame.draw.rect(screen, WHITE, (desk['x'], desk['y'], desk_size, desk_size))
        # Отображение студента в партe, если она не занята
        if not desk['occupied']:
            screen.blit(student_image, (desk['x'], desk['y']))

    for teacher in teachers_male:
        screen.blit(pygame.transform.scale(teacher['image'], (teacher_width, teacher_height)),
                    (teacher['x'], teacher['y']))

    for teacher in teachers_female:
        screen.blit(pygame.transform.scale(teacher['image'], (teacher_width, teacher_height)),
                    (teacher['x'], teacher['y']))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
