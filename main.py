import pygame
import random
pygame.init()

x = 1280
y = 720

# Tela


screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Jogo")

# Characters Images 

transparent = (0, 0, 0, 0)

bg = pygame.image.load("Images/bg.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

alien = pygame.image.load("Images/huntt.png").convert_alpha()
alien = pygame.transform.scale(alien, (50,50))

alien2 = pygame.image.load("Images/huntt.png").convert_alpha()
alien2 = pygame.transform.scale(alien, (50,50))

alien3 = pygame.image.load("Images/huntt.png").convert_alpha()
alien3 = pygame.transform.scale(alien, (50,50))

playerImg = pygame.image.load("Images/nave.png").convert_alpha()
playerImg = pygame.transform.scale(playerImg, (50,50))

missil = pygame.image.load("Images/missil.png").convert_alpha()
missil = pygame.transform.scale(missil, (25,25))

health = pygame.image.load("Images/health.png")
health = pygame.transform.scale(health, (50,50))

health2 = pygame.image.load("Images/health.png")
health2 = pygame.transform.scale(health2, (50,50))

health3 = pygame.image.load("Images/health.png")
health3 = pygame.transform.scale(health3, (50,50))

unhealth = pygame.image.load("Images/unhealth.png")
unhealth = pygame.transform.scale(unhealth, (50,50))

unhealth2 = pygame.image.load("Images/unhealth.png")
unhealth2 = pygame.transform.scale(unhealth2, (50,50))

unhealth3 = pygame.image.load("Images/unhealth.png")
unhealth3 = pygame.transform.scale(unhealth3, (50,50))

pontos = 3
life = 6

# Characters X/Y

pos_alien_x = 700
pos_alien_y= 800

pos_alien2_x = 700
pos_alien2_y= 800

pos_alien3_x = 700
pos_alien3_y= 800

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 218
pos_missil_y = 315

triggered = False
running = True

# Font and Music

font = pygame.font.Font("PixelGameFont.ttf", 50)
music = pygame.mixer.Sound("Musics/shot.wav")


# Rectangle

player_rect = playerImg.get_rect()
alien_rect = alien.get_rect()
alien2_rect = alien2.get_rect()
alien3_rect = alien3.get_rect()
missil_rect = missil.get_rect()



#Functions

def respawn():
  x = random.randint(1350,1370)
  y = random.randint(1,640)
  return [x,y]

def respawn_missil():
    triggered = False
    respawn_missil_x = (pos_player_x + 20)
    respawn_missil_y = (pos_player_y + 15)
    vel_x_missil = 0
    return [respawn_missil_x, respawn_missil_y, triggered, vel_x_missil]

def colisions():
  global pontos
  global life
  if player_rect.colliderect(alien_rect):
    pontos -= 1
    life -= 1
    return True
  elif missil_rect.colliderect(alien_rect) and pos_missil_x == (pos_player_x + 20):
    pontos -= 1
    life -= 1
    return True
  elif missil_rect.colliderect(alien_rect):
    pontos += 1
    return True
  else:
    return False

def colisions2():
  global pontos
  global life
  if player_rect.colliderect(alien2_rect):
    pontos -= 1
    life -= 1
    return True
  elif missil_rect.colliderect(alien2_rect) and pos_missil_x == (pos_player_x + 20):
    pontos -= 1
    life -= 1
    return True
  elif missil_rect.colliderect(alien2_rect):
    pontos += 1

    return True
  else:
    return False

def colisions3():
  global pontos
  global life
  if player_rect.colliderect(alien3_rect):
    pontos -= 1
    life -= 1
    return True
  elif missil_rect.colliderect(alien3_rect) and pos_missil_x == (pos_player_x + 20):
    pontos -= 1
    life -= 1
    return True
  elif missil_rect.colliderect(alien3_rect):
    pontos += 1
    return True
  else:
    return False


while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    screen.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0))
    if rel_x < 1280:
      screen.blit(bg, (rel_x, 0))

  #Keywords
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 0:
      pos_player_y -= 2
      if not triggered:
        pos_missil_y -= 2

    if tecla[pygame.K_DOWN] and pos_player_y < 630:
      pos_player_y += 2
      if not triggered:
        pos_missil_y += 2

    if tecla[pygame.K_RIGHT] and pos_player_x < 1200:
      pos_player_x += 2
      if not triggered:
        pos_missil_x += 2

    if tecla[pygame.K_LEFT] and pos_player_x > 0:
      pos_player_x -= 2
      if not triggered:
        pos_missil_x -= 2

    if tecla[pygame.K_SPACE]:
      triggered = True
      vel_missil_x = 3

    if tecla[pygame.K_SPACE] and pos_missil_x == (pos_player_x + 20):
      music.play(0)

  #Game Over

    if life == -1:
      pygame.quit()

  #Respawn
    if pos_alien_x == 0:
      pos_alien_x = respawn()[0]
      pos_alien_y = respawn()[1]

    if pos_alien2_x == 0:
      pos_alien2_x = respawn()[0]
      pos_alien2_y = respawn()[1]

    if pos_alien3_x == 0:
      pos_alien3_x = respawn()[0]
      pos_alien3_y = respawn()[1]

    if pos_missil_x >= 1300:
      pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()

    if pos_alien_x == 0 or colisions():
      pos_alien_x = respawn()[0]
      pos_alien_y = respawn()[1]

    if pos_alien2_x == 0 or colisions2():
      pos_alien2_x = respawn()[0]
      pos_alien2_y = respawn()[1]

    if pos_alien3_x == 0 or colisions3():
      pos_alien3_x = respawn()[0]
      pos_alien3_y = respawn()[1]

  #Reload

    if missil_rect.colliderect(alien_rect) or missil_rect.colliderect(alien2_rect) or missil_rect.colliderect(alien3_rect):
          pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()

  #Losing Life

    if life == 2:
      health3.fill(transparent)
    if life == 1:
      health2.fill(transparent)
    if life == 0:
      health.fill(transparent)
  
  #Position

    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    missil_rect.y = pos_missil_y
    missil_rect.x = pos_missil_x

    alien_rect.y = pos_alien_y
    alien_rect.x = pos_alien_x

    alien2_rect.y = pos_alien2_y
    alien2_rect.x = pos_alien2_x

    alien3_rect.y = pos_alien3_y
    alien3_rect.x = pos_alien3_x

  #Moviment

    x -= 1
    pos_alien_x -= 1
    pos_alien2_x -= 1
    pos_alien3_x -= 1
    pos_missil_x += vel_missil_x

    score = font.render(f'Points: {int(pontos)} ', True, (0,0,0))
    screen.blit(score, (1030,10))
    screen.blit(health, (0,0))
    screen.blit(health2, (50,0))
    screen.blit(health3, (100,0))

  #Images on Screen
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(alien2, (pos_alien2_x, pos_alien2_y))
    screen.blit(alien3, (pos_alien3_x, pos_alien3_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    print(pontos)
    pygame.display.update()

