import pygame
import button
from game import Game


#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rock_Paper_Scissor_Lizard_Spock')

#load button images
start_img = pygame.image.load('Menu\start_btn.png').convert_alpha()
exit_img = pygame.image.load('Menu\exit_btn.png').convert_alpha()
help_img = pygame.image.load('Menu\help_btn.png').convert_alpha()

#create button instances
start_button = button.Button(50, 200, start_img, 0.8)
help_button = button.Button(300, 200, help_img, 0.8)
exit_button = button.Button(550, 200, exit_img, 0.8)


#game loop
run = True
game = Game()
while run:

	screen.fill((202, 228, 241))

	if start_button.draw(screen):
		print('START')
		game.start()

	if help_button.draw(screen):
		print('Help')

		
	if exit_button.draw(screen):
		print('EXIT')
		pygame.quit()

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()