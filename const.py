import os
import pygame

pygame.font.init()

WIDTH, HEIGHT = 750, 750
FPS = 60
MAIN_FONT = pygame.font.SysFont("comicsans", 50)
LOST_FONT = pygame.font.SysFont("comicsans", 60)
ENEMY_VEL = 0.5
PLAYER_VEL = 5
LASER_VEL = 2
ENEMY_SCORE = 10
BOSS_SCORE = 100

# Load images
boi1 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "boi1.png")), (128, 128))
boi2 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "boi2.png")), (128, 128))
boi3 = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "boi3.png")), (128, 128))

# Player player
player_ship = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "player.png")), (128, 128))

# Lasers
red = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "red.png")), (128, 128))
purple = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "porpol.png")), (128, 128))
blue = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "blue.png")), (128, 128))
orange = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "orange.png")), (128, 128))

#space crab
boss_img = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "SPACECRAB.png")), (256, 256))

# Background
BG = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "background.png")),
    (WIDTH, HEIGHT))