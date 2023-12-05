import pygame
import sys
import pygame.mixer
import time

pygame.init()
pygame.mixer.init()

#colors
WHITE = pygame.Color(255, 255, 255, 0)
BLACK = (0, 0, 0)

#size
WIDTH, HEIGHT = 800, 600

#display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("avinash and arnur are watching you")

#bg
background_image = pygame.image.load('back.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

#music
pygame.mixer.music.load('sound.mp3')  
pygame.mixer.music.set_volume(0.5) 
pygame.mixer.music.play(-1) #infinite replay

#characteristics of proctors
proctor_width, proctor_height = 44, 44

#ватафак
proctor_avinash = [
    {'x': WIDTH - proctor_width - 420, 'y': 250, 'speed': 2.2, 'direction': 'up', 'image': pygame.image.load('avi.png')},
]
#ватафак
proctor_arnee = [
    {'x': WIDTH - proctor_width - 160, 'y': 250, 'speed': 2.2, 'direction': 'down', 'image': pygame.image.load('avi.png')},
]

desk_size = 30
num_desks_length = 5
num_desks_width = 5

#ватафак
desk_spacing_length = WIDTH // (num_desks_length + 1)
desk_spacing_width = int(HEIGHT * 0.6) // (num_desks_width + 1)  # Уменьшаем высоту периметра на 40%

# Загрузка изображения студента
student_image = pygame.image.load('parta.png')
student_image = pygame.transform.scale(student_image, (80, 80))

#ватафак
desks = [{'x': i * desk_spacing_length, 'y': j * desk_spacing_width + 225, 'occupied': False} for i in
         range(1, num_desks_length + 1) for j in range(1, num_desks_width + 1)]


clock = pygame.time.Clock()
running = True


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
    #ватафак
    font = pygame.font.Font(None, 100)
    timer_text = font.render(str(int(10 - (time.time() - start_time))), True, WHITE)
    screen.blit(timer_text, (WIDTH // 2 - 50, HEIGHT // 2 - 50))

    pygame.display.flip()
    clock.tick(60)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Движение учителей по измененному периметру прямоугольника
    for proctor in proctor_avinash:
        if proctor['direction'] == 'up':
            proctor['y'] -= proctor['speed']
            if proctor['y'] <= 230:  # сверху
                proctor['direction'] = 'right'
        elif proctor['direction'] == 'right':
            proctor['x'] += proctor['speed']
            if proctor['x'] >= WIDTH - proctor_width - 420:  # справа
                proctor['direction'] = 'down'
        elif proctor['direction'] == 'down':
            proctor['y'] += proctor['speed']
            if proctor['y'] >= HEIGHT - proctor_height - 10:  # от низа
                proctor['direction'] = 'left'
        elif proctor['direction'] == 'left':
            proctor['x'] -= proctor['speed']
            if proctor['x'] <= 210:  # слева
                proctor['direction'] = 'up'

    for proctor in proctor_arnee:
        if proctor['direction'] == 'up':
            proctor['y'] -= proctor['speed']
            if proctor['y'] <= 230:  # сверху
                proctor['direction'] = 'right'
        elif proctor['direction'] == 'right':
            proctor['x'] += proctor['speed']
            if proctor['x'] >= WIDTH - proctor_width - 160:  # справа
                proctor['direction'] = 'down'
        elif proctor['direction'] == 'down':
            proctor['y'] += proctor['speed']
            if proctor['y'] >= HEIGHT - proctor_height - 10:  # от низа
                proctor['direction'] = 'left'
        elif proctor['direction'] == 'left':
            proctor['x'] -= proctor['speed']
            if proctor['x'] <= 450:  # слева
                proctor['direction'] = 'up'

    # Отрисовка заднего фона
    screen.blit(background_image, (0, 0))

    # Отрисовка игровых объектов
    #ватафак
    for desk in desks:
        pygame.draw.rect(screen, background_image.get_at((desk['x'], desk['y'])), (desk['x'], desk['y'], desk_size, desk_size))
        # Отображение студента в партe, если она не занята
        if not desk['occupied']:
            screen.blit(student_image, (desk['x'], desk['y']))

#ватафак
    for proctor in proctor_avinash:
        screen.blit(pygame.transform.scale(proctor['image'], (proctor_width, proctor_height)),
                    (proctor['x'], proctor['y']))

#ватафак
    for proctor in proctor_arnee:
        screen.blit(pygame.transform.scale(proctor['image'], (proctor_width, proctor_height)),
                    (proctor['x'], proctor['y']))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
