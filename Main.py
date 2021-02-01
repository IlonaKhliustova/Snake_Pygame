import pygame
from random import randrange

RES = 665
SIZE = 30
x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 32
dead = False
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
speed_count, snake_speed = 0, 10
pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_ad = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('iimg.jpg').convert()

pygame.mixer.music.load("8bit_buddy_holly.mp3")
pygame.mixer.music.play()

while True:
    sc.blit(img, (0, 0))

    [pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))

    speed_count += 1
    if not dead:
        if not speed_count % snake_speed:
            x += dx * SIZE
            y += dy * SIZE
            snake.append((x, y))
            snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)

    if score % 11 == 0 and score != 0:
        render_ad = font_ad.render('Играйте в новую игру "Dungeon Master"', 1, pygame.Color('yellow'))
        sc.blit(render_ad, (RES // 2 - 270, RES // 3))

    if score % 9 == 0 and score != 0 and not score % 11 == 0:
        render_ad = font_ad.render('Играйте в новую игру "VldTower"', 1, pygame.Color('yellow'))
        sc.blit(render_ad, (RES // 2 - 270, RES // 3))

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        render_end = font_end.render('GAME OVER', 1, pygame.Color('yellow'))
        sc.blit(render_end, (RES // 2 - 200, RES // 3))
        render_restart = font_ad.render('Press [R] to continue', 1, pygame.Color('yellow'))
        sc.blit(render_restart, (RES // 3, RES // 2))

        dead = True
        snake_speed = 0
        pygame.display.flip()

    pygame.display.flip()
    clock.tick(fps)

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }

    elif key[pygame.K_DOWN]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_LEFT]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }

    elif key[pygame.K_RIGHT]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
    elif key[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    elif key[pygame.K_r]:
        x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        score = 0
        length = 1

        dx, dy = 0, 0
        snake_speed = 10
        dead = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
