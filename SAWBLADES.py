import pygame
import random

pygame.init()

width, height = 500, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sawblades")

#resimler
saw_img = pygame.image.load("sawblades.png").convert_alpha()
saw_img = pygame.transform.scale(saw_img, (60, 50))

arkaplan = pygame.image.load("gbforest.jpg").convert()
arkaplan = pygame.transform.scale(arkaplan, (width, height))

player_img = pygame.image.load("character.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 50))

player = pygame.Rect(width // 2 - 25, height - 80, 50, 50)
player_speed = 6

saw_count = 5
saws = []
for _ in range(saw_count):
    x = random.randint(0, width - 60)
    y = random.randint(-600, -40)
    saws.append(pygame.Rect(x, y, 60, 50))

saw_speed = 5
score = 0
font = pygame.font.SysFont("Times New Roman", 24, True)

clock = pygame.time.Clock()
running = True
game_over = False

while running:
    screen.blit(arkaplan, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += player_speed

        if player.x < 0:
            player.x = 0
        if player.x > width - player.width:
            player.x = width - player.width

        for saw in saws:
            saw.y += saw_speed


            if saw.top > height:
                saw.y = random.randint(-600, -40)
                saw.x = random.randint(0, width - 60)

                score += 1
                if score % 5 == 0:
                    saw_speed += 1

            if player.colliderect(saw):
                game_over = True

            screen.blit(saw_img, (saw.x, saw.y))

        screen.blit(player_img, (player.x, player.y))

        skor_yazi = font.render(f"Skor: {score}", True, (29, 115, 5))
        screen.blit(skor_yazi, (10, 10))

    else:
        bitis = font.render(f"Oyun Bitti! Skor: {score}", True, (255, 0, 0))
        screen.blit(bitis, (width // 2 - bitis.get_width() // 2, height // 2))

    pygame.display.flip()
    clock.tick(60)