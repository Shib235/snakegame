import pygame
import random
import time

pygame.init()

width = 800
height = 600

xchangeg = 0
ychangeg = 0
xposg = width/2
yposg = height/2
snakelg = []
snakelengthg = 1
scoreg = 0
snakesize = 25
snakespeed = 13
highscore = 0
limit = 10
foodxg = round(random.randrange(0,width-(snakesize*snakelengthg)) // snakesize) * snakesize
foodyg = round(random.randrange(0,height-(snakesize*snakelengthg))// snakesize) * snakesize
levelg = 1

white = (255,255,255)
black = (0,0,0)
green = (3,179,3)
green2 = (5,164,5)
red = (223,56,56)
blue = (0,76,153)
realblue = (0,0,255)
yellow = (255,255,0)
snakecolour = (2,105,2)
realgreen = (0,255,0)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Shihaabs Snake Game')

def drawGrid():
    global snakesize #Set the size of the grid block
    for x in range(0, width, snakesize):
        for y in range(0, height, snakesize):
            rect = pygame.Rect(x, y, snakesize, snakesize)
            pygame.draw.rect(screen, green2, rect, 1)
    pygame.display.update()



def message(msg,font,color,x,y):
	mesg = font.render(msg,True,color)
	screen.blit(mesg,[x,y])

scorefont = pygame.font.SysFont(None,30)
losefont = pygame.font.SysFont('arial',40)
winfont = pygame.font.SysFont('cartoon',60)

clock = pygame.time.Clock()



def createsnake(size,snakelist):
	for i in snakelist:
		pygame.draw.rect(screen,snakecolour,[i[0],i[1],size,size])


def game():
	global highscore
	global limit
	global snakelengthg
	global scoreg
	global snakelg
	global xposg
	global yposg
	global xchangeg
	global ychangeg
	global foodxg
	global foodyg
	global levelg

	snakel2 = []

	game_over = False
	game_close = False
	game_win = False

	xpos = xposg
	ypos = yposg

	xchange = xchangeg
	ychange = ychangeg


	snakel = snakelg
	snakelength = snakelengthg
	score = scoreg
	level = levelg


	foodx = foodxg
	foody = foodyg


	while game_over == False:


		while game_win == True:
			screen.fill(realgreen)
			message('Level Up!',winfont,realblue,300,200)
			message('Press C to continue',winfont,realblue,200,300)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_win = False
					elif event.key == pygame.K_c:
						limit += 10
						level+=1
						scoreg = score
						snakelengthg = snakelength
						snakelg = snakel
						snakel2 = snakel
						xposg = xpos
						yposg = ypos 
						xchangeg = xchange 
						ychangeg = ychange 
						foodxg = foodx
						foodyg = foody
						levelg = level
						game()
				elif event.type == pygame.QUIT:
					game_over = True
					game_win = False



		while game_close == True:
			screen.fill(black)
			message('You lose,will you Quit(Q) or Try Again(C)?',losefont,red,100,200)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					elif event.key == pygame.K_c:
						if limit == 10:
							xchangeg = 0
							ychangeg = 0
							xposg = width/2
							yposg = height/2
							snakelg = []
							snakelengthg = 1
							scoreg = 0
							levelg = 1
						else:
							del snakel
							snakelg = snakel2

						game()
				elif event.type == pygame.QUIT:
					game_over = True
					game_close = False




		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w and ychange ==0:
					xchange = 0
					ychange = -(snakesize)
				elif event.key == pygame.K_s and ychange ==0:
					xchange = 0
					ychange = snakesize
				elif event.key == pygame.K_d and xchange ==0:
					xchange = snakesize
					ychange = 0
				elif event.key == pygame.K_a and xchange == 0:
					xchange = -(snakesize)
					ychange = 0






		if xpos > width or xpos < 0 or ypos > height or ypos < 0:
			game_close = True


		if score == limit:
			game_win = True


		xpos += xchange
		ypos += ychange


		screen.fill(green)

		drawGrid()

		food = pygame.draw.rect(screen,red,[foodx,foody,snakesize,snakesize])

		snakehead = []
		snakehead.append(xpos)
		snakehead.append(ypos)
		snakel.append(snakehead)

		if len(snakel) > snakelength:
			del snakel[0]


		for i in snakel[:-1]:
			if i == snakehead:
				game_close = True   



		createsnake(snakesize,snakel)

		if highscore < score:
			highscore = score
		score = snakelength - 1
		message(f'Your score is {score}',scorefont,blue,10,10)
		message(f'Your highscore is {highscore}',scorefont,blue,580,10)	
		message(f'Level: {level}',scorefont,blue,10,575)	

		pygame.display.update()


		if xpos == foodx and ypos == foody:
			foodx = round(random.randrange(0,width-(snakesize))//snakesize)*snakesize
			foody = round(random.randrange(0,height-(snakesize))//snakesize)*snakesize
			snakelength += 1


		clock.tick(snakespeed)

	pygame.quit()
	quit()


game()