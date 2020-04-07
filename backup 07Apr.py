import pygame
import os
import sys

pygame.init()
# # intro screen # # 
def intro():
	win = pygame.display.set_mode((1139,639))
	pygame.display.set_caption('where are  y o u  ?')

	end = False
	while not end:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
	#	pygame.time.delay(100)
		bg = pygame.image.load('yellow1.jpg')
		win.blit(bg,(0,0))

		font = pygame.font.SysFont("monospace",25)
		label = font.render("Let's go on a trip.",1,(206,118,118))
		win.blit(label,(410,100))
		label = font.render("You will need:",1,(232,126,126))
		win.blit(label,(440,160))
		label = font.render("1. sanity",1,(232,126,126))
		win.blit(label,(440,220))
		label = font.render("2. insanity",1,(232,126,126))
		win.blit(label,(440,280))
		
		font = pygame.font.SysFont("monospace",45)

		label = font.render('PLAY',1,(255,255,255))
		win.blit(label,(505,500))
		win.blit(label,(506,500))
		label = font.render('PLAY',1,(206,118,118))
		win.blit(label,(508,500))
		label = font.render('PLAY',1,(25,29,129))
		win.blit(label,(503,500))
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if (mouse[0] > 499 and mouse[0] < 617) and (mouse[1] > 511 and mouse[1] < 541):
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					
					level.SpaceLevel()
					
					pygame.display.update()
					end = True
		pygame.display.update()

class players:
	def __init__(self,x,y):
		pass

class levels:
	def __init__(self,levelNo):
		pass

class Platform:
	pass

class gameOvers:
	def __init__(self,levelNo):
		pass

class endingScreens:
	def __init__(self):
		pass

# screen controls #
def screenControl(player):

	run = True
	bgX = 0
	bgX2 = 1139
	while run:
		clock.tick(27)
		bgX -= 1.4
		bgX2 -= 1.4
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				exit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and player.x > player.vel:
			player.x -= player.vel
			player.left = True
			player.right = False
			if bgX < bg.get_width() * -1:
				bgX = bg.get_width()
			if bgX2 < bg.get_width() * -1:
				bgX2 = bg.get_width()
			# platform goes back by the distance we're walking forward
			

		elif keys[pygame.K_RIGHT] and player.x < 1130 - player.width - player.vel:
			player.x += player.vel
			player.right = True
			player.left = False
			if bgX < bg.get_width() * -1:
				bgX = bg.get_width()
			if bgX2 < bg.get_width() * -1:
				bgX2 = bg.get_width()
		else:
			player.right = False
			player.left = False
			walkCount = 0
			
		if not(player.isJump):
			if keys[pygame.K_SPACE]:
				player.isJump = True
				player.right = False
				player.left = False
				player.walkCount = 0
		else:
			if player.jumpCount >= -10:
				neg = 1
				if player.jumpCount < 0:
					neg = -1
				player.y -= (player.jumpCount ** 2) * 0.5 * neg
				player.jumpCount -= 1

			else:
				player.isJump = False
				player.jumpCount = 10

intro()