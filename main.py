import random
import pygame
from const import WIDTH, HEIGHT, BG, FPS, MAIN_FONT, LOST_FONT, ENEMY_VEL, PLAYER_VEL, LASER_VEL, ENEMY_SCORE, FONT, BOSS_SCORE
from ship import Boss, Player, Enemy
from helpers import collide

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooters")

def main():
    global ENEMY_VEL
    ENEMY_VEL = 0.5

    score = 0
    level = 0
    lives = 8
    enemies = []
    num_enemy = 0
    player = Player(300, 500)
    clock = pygame.time.Clock()
    lost = False
    wave_length = 5

    def redraw_window():
        WIN.blit(BG, (0, 0))

        if lost:
            lost_label = LOST_FONT.render("Game Over!", 1, (255, 255, 255))
            score_label = LOST_FONT.render(f"Your Score: {score}", 1, (255, 255, 255))
            restart_label = MAIN_FONT.render(f"Press ESC To Restart...", 1, (255, 255, 255))
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
            WIN.blit(score_label, (WIDTH / 2 - score_label.get_width() / 2, 450))
            WIN.blit(restart_label, (WIDTH / 2 - restart_label.get_width() / 2, 550))
        else:
            # draw text
            lives_label = MAIN_FONT.render(f"Lives: {lives}", 1, (255, 255, 255))
            score_label = MAIN_FONT.render(f"SCORE: {score}", 1, (255, 255, 255))
            level_label = MAIN_FONT.render(f"Level: {level}", 1, (255, 255, 255))

            WIN.blit(lives_label, (10, 10))
            WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
            WIN.blit(score_label, (level_label.get_width() + 50, 10))

            for enemy in enemies:
                enemy.draw(WIN)

            player.draw(WIN)

        pygame.display.update()

    while True:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
        if lost:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                return

        if len(enemies) == 0:
            level += 1
            num_enemy += wave_length

            if level % 3 == 0:
                ENEMY_VEL = max(ENEMY_VEL*1.05, 2.2)
                wave_length += 1
                lives += 1
                num_enemy = 0
                boss_time = Boss(random.randrange(50, WIDTH - 150),
                                 random.randrange(-100, -50))
                enemies.append(boss_time)

            player.health = max(100, player.health)

            for i in range(num_enemy):
                enemy = Enemy(random.randrange(50, WIDTH - 150),
                              random.randrange(-1500, -100),
                              random.choice(["red", "blue", "purple"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VEL > 0:  # left
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.get_width(
        ) < WIDTH:  # right
            player.x += PLAYER_VEL
        if keys[pygame.K_w] and player.y - PLAYER_VEL > 0:  # up
            player.y -= PLAYER_VEL
        if keys[pygame.K_s] and player.y + PLAYER_VEL + player.get_height(
        ) + 15 < HEIGHT:  # down
            player.y += PLAYER_VEL
        if keys[pygame.K_SPACE]:
            player.shoot()

        for boss_time in enemies[:]:
            if isinstance(boss_time, Enemy):
                continue

            boss_time.move(ENEMY_VEL)
            boss_time.move_lasers(LASER_VEL, player)

            if random.randrange(0, 2 * 20) == 1:
                boss_time.shoot()

            if collide(boss_time, player):
                player.health -= 20
                boss_time.health -= 10

                if boss_time.health < 0:
                    if not lost:
						score += BOSS_SCORE
                    enemies.remove(boss_time)

            elif boss_time.y + boss_time.get_height() > HEIGHT:
                lives -= 5
                enemies.remove(boss_time)

        for enemy in enemies[:]:
            if isinstance(enemy, Boss):
                continue

            enemy.move(ENEMY_VEL)
            enemy.move_lasers(LASER_VEL, player)

            if random.randrange(0, 80) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemy.health -= 10

                if enemy.health < 0:
                    if not lost:
						score += ENEMY_SCORE
                    enemies.remove(enemy)

            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        hit = player.move_lasers(-LASER_VEL, enemies)
        for h in hit:
			if lost: 
				break
            if isinstance(h, Enemy):
                score += ENEMY_SCORE
            if isinstance(h, Boss):
                score += BOSS_SCORE



def main_menu():
    title_font = pygame.font.SysFont(FONT, 50)
    WIN.blit(BG, (0, 0))
    title_label = title_font.render("Press the mouse to begin...", 1,
                                    (255, 255, 255))
    WIN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 350))
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
                return
        


if __name__ == "__main__":
    pygame.init()
    while True:
        main_menu()
