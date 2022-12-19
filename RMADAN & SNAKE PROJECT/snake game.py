import pygame as pyg
import sys
import random
import time

check_errors = pyg.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully initialized!")

    # Play surface
playSurface = pyg.display.set_mode((1280,720), vsync=1)
pyg.display.set_caption('RAMADAN & SNAKE')

# Colors
red = pyg.Color(255, 0, 0)  # gameover
green = pyg.Color(0, 255, 0)  # snake
black = pyg.Color(0, 0, 0)  # score
white= pyg.Color(255, 255, 255)  # background
brown = pyg.Color(165, 42, 42)  # food

# FPS controller
fpsController = pyg.time.Clock()

# Important varibles
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 40], [80, 30]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

score = 0

# Game over function


def gameOver():
    myFont = pyg.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (645,30)
    playSurface.blit(GOsurf, GOrect)
    showScore(0)
    pyg.display.flip()

    time.sleep(1)
    pyg.quit()  # pygame exit
    sys.exit()  # console exit


def showScore(choice=1):
    sFont = pyg.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score), True, white)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (8, 80)
    else:
        Srect.midtop = (645, 20)
        playSurface.blit(Ssurf, Srect)


     # Main Logic of the game
while True:
    
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pyg.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pyg.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pyg.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pyg.K_ESCAPE:
                pyg.event.post(pyg.event.Event(pyg.QUIT))

    # validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # Snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1 #to change score point
        foodSpawn = False
    else:
        snakeBody.pop()

    # Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    # Background
    playSurface.fill(black)

    # Draw Snake
    for pos in snakeBody:
        pyg.draw.rect(playSurface, white,pyg.Rect(pos[0], pos[1], 10, 10))

        pyg.draw.rect(playSurface, brown, pyg.Rect(foodPos[0], foodPos[1], 10, 10))

        # Bound
    if snakePos[0] > 1280 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 720 or snakePos[1] < 0:
        gameOver()

        # Self hit
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showScore()
    pyg.display.flip()

    fpsController.tick(20)
