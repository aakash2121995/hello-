import pygame,time
import random
pygame.init()

display_width = 800
display_height = 600

FPS = 30

DISPLAY = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Slithher")


red = (0,255,255) # colour has been changed
white =  (255,255,255)
black = (0,0,0)
green = (0,255,0)


blocksize = 10



clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

def message(msg,color):
	length = len(msg)
	DISPLAY.fill(white)
	text = font.render(msg, True , color)
	DISPLAY.blit(text , [display_width/2-length*25/4,display_height/2])
	pygame.display.update()	


def snake(blocksize,snakelist):
	for XnY in snakelist:
		pygame.draw.rect(DISPLAY,green,[XnY[0],XnY[1],blocksize,blocksize])
	



def gameloop():
	gamexit = False
	gameover = False
	lead_x = display_width/2
	lead_y = display_height/2
	
	lead_x_change = 0
	lead_y_change = 0
	
	snakeList = []
	snakeLength = 1
	
	randAppleX = round(random.randrange(0,display_width-blocksize)/10.0)*10.0
	randAppleY = round(random.randrange(0,display_height-blocksize)/10.0)*10.0
	while not gamexit:

		while gameover == True:
			DISPLAY.fill(white)
			message("Game over ! Press C to play again or Q to quit",black)
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameover = False
						gamexit = True
					elif event.key == pygame.K_c:
						gameloop()
				elif event.type == pygame.QUIT:
						gamexit = True 
						gameover = False		


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gamexit = True 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -blocksize
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = blocksize
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = -blocksize
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = blocksize
					lead_x_change = 0

		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
			gameover = True 
		
		lead_x +=lead_x_change
		lead_y += lead_y_change			
			
		DISPLAY.fill(white)
		pygame.draw.rect(DISPLAY , red , [randAppleX,randAppleY,blocksize,blocksize])
		
		
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)
		snake(blocksize,snakeList)
		
		for segment in snakeList[:-1]:
			if snakeList[:-1] == snakeHead:
				gameover = True
		
		
		if len(snakeList) > snakeLength:
			del snakeList[0]
		pygame.display.update()
		
		if lead_x == randAppleX and lead_y == randAppleY:
			randAppleX = round(random.randrange(0,display_width-blocksize)/10.0)*10.0
			randAppleY = round(random.randrange(0,display_height-blocksize)/10.0)*10.0
			snakeLength+=1
			
		clock.tick(FPS)	

	message("Good Bye !!",black)
	time.sleep(1)

	pygame.quit()

	quit()

gameloop()
