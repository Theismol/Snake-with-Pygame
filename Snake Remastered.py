import pygame
import random
pygame.font.init()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
score = 0
scoreFont = pygame.font.Font("freesansbold.ttf",20)
scoreNumber = scoreFont.render(str(score),True,WHITE)
scoreText = scoreFont.render("Score:",True,WHITE)
clock = pygame.time.Clock()
FPS = 10
size = 20
x = [400]
y = [300]
foodx = round(random.randrange(10,100)/20)*20
foody = round(random.randrange(10,100)/20)*20
xChange = 0
yChange = 0
xyRect = []
#Draws the background, snake, food and score
def draw():
    WIN.fill(BLACK)
    pygame.Surface.blit(WIN,scoreText,(50,0))
    pygame.Surface.blit(WIN,scoreNumber,(115,0))
    for i in range(len(x)):
        pygame.draw.rect(WIN,GREEN,(x[i],y[i],size,size))
    pygame.draw.rect(WIN,RED,(foodx,foody,size,size))
    pygame.display.update()
def main():
    global x,y,xChange,yChange,foodx,foody,FPS,xyRect,scoreNumber,score
    run = True
    while run:
        clock.tick(FPS)  
#Checks if snake has hit the food
        if foodx == x[0] and foody == y[0]:
            x.append(-1)
            y.append(-1)
            score += 1
            scoreNumber = scoreFont.render(str(score),True,WHITE)
            foodInSnake = True
#while loop to make sure that food does not spawn on top of snake
            while foodInSnake:
                foodx = round(random.randrange(0,WIDTH)/20)*20
                foody = round(random.randrange(0,HEIGHT)/20)*20
                for i in range(len(x)):
                    if foodx == x[i] and foody == y[i]:
                        foodx = round(random.randrange(10,100)/20)*20
                        foody = round(random.randrange(10,100)/20)*20
                    elif foodx < 115 and foody == 0:
                        foodx = round(random.randrange(10,100)/20)*20
                        foody = round(random.randrange(10,100)/20)*20
                    else:
                        foodInSnake = False
#Makes the game faster(harder)
            FPS += 0.5
        for event in pygame.event.get():
#Checks if player has pressed X
            if event.type == pygame.QUIT:
                run = False
#Checks if snake hits border of screen
            if x[0] < 0 or x[0] > WIDTH or y[0] < 0 or y[0] > HEIGHT:
                run = False
#Makes the snake change direction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if xChange != 20:
                        xChange = -20
                        yChange = 0
                elif event.key == pygame.K_RIGHT:
                    if xChange != -20:
                        xChange = 20
                        yChange = 0
                elif event.key == pygame.K_UP:
                    if yChange != 20:
                        xChange = 0
                        yChange = -20
                elif event.key == pygame.K_DOWN:
                    if yChange != -20:
                        xChange = 0
                        yChange = 20
#Gives the snake new coordinates to move to
        for i in range(len(x)-1):
                    x[-i-1] = x[-i-2]
                    y[-i-1] = y[-i-2]
        x[0] += xChange
        y[0] += yChange
#Checks if snake has hit itself
        for i in range(len(x)-1):
            xyRect.append((x[i+1],y[i+1]))
        if (x[0],y[0]) in xyRect:
            run = False
        else:
            xyRect = []
        draw()
main()