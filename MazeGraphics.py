import pygame
from Maze import Maze

#Colours
black = 0, 0, 0
white = 255, 255, 255
orange = 255, 165, 0
red = 255, 0, 0
green = 0, 255, 0

class Window:
	"""Class for display window and attributes associated with it such as size"""
	def __init__(self, display_width, display_height, window_title, cell_dimensions, maze):
		self.display_width = display_width
		self.display_height = display_height
		self.window_title = window_title
		self.window = pygame.display.set_mode((display_width, display_height))
		self.window.fill(white)
		pygame.display.set_caption(window_title)
		self.clock = pygame.time.Clock()
		self.walls_dict = {}
		self.walls = pygame.sprite.Group()
		self.cell_dimensions = cell_dimensions
		self.maze = maze
		self.sprite_list = pygame.sprite.Group()
	def get_cell_center(self, cell):
		return ((cell.coord[0] * self.cell_dimensions) + self.cell_dimensions), ((cell.coord[1] * self.cell_dimensions) + self.cell_dimensions)
	def render_cell(self, cell, cell_dimensions, iteration):
		cell_centre = self.get_cell_center(cell)
		cell_deviation = cell_dimensions / 2
		if cell.shell['Top'] == True:
			var_name = "cell_" + str(iteration) + "_top"
			start_x = cell_centre[0] - cell_deviation
			start_y = cell_centre[1] - cell_deviation
			self.walls_dict[var_name] = Wall(start_x, start_y, cell_dimensions + 1, 1, self.window, self.walls, self.sprite_list, black)
		else:
			pass
		if cell.shell['Bottom'] == True:
			var_name = "cell_" + str(iteration) + "_bottom"
			start_x = cell_centre[0] - cell_deviation
			start_y = cell_centre[1] + cell_deviation
			self.walls_dict[var_name] = Wall(start_x, start_y, cell_dimensions + 1, 1, self.window, self.walls, self.sprite_list, black)

		else:
			pass
		if cell.shell['Left'] == True:
			var_name = "cell_" + str(iteration) + "_left"
			start_x = cell_centre[0] - cell_deviation
			start_y = cell_centre[1] - cell_deviation
			self.walls_dict[var_name] = Wall(start_x, start_y, 1, cell_dimensions + 1, self.window, self.walls, self.sprite_list, black)
		else:
			pass
		if cell.shell['Right'] == True:
			var_name = "cell_" + str(iteration) + "_right"
			start_x = cell_centre[0] + cell_deviation
			start_y = cell_centre[1] - cell_deviation
			self.walls_dict[var_name] = Wall(start_x, start_y, 1, cell_dimensions + 1, self.window, self.walls, self.sprite_list, black)
		else:
			pass
		return cell_centre
	def render_end(self, cell_dimensions):
		x, y = self.get_cell_center(self.maze.end)
		return Coin(x, y, int(cell_dimensions/2), self.window, self.sprite_list)

class Text(pygame.sprite.Sprite):
	def __init__(self, text, size, sprite_list, window):
		super().__init__()
		pygame.font.init()
		font = pygame.font.Font("freesansbold.ttf", size)
		self.image = font.render(text, True, black)
		self.rect = self.image.get_rect()
		sprite_list.add(self)
	def update(self):
		self.image.fill(white)

class Wall(pygame.sprite.Sprite):
	""" Wall the player can run into. """
	def __init__(self, x, y, width, height, surface, group, sprite_list, colour):
		""" Constructor for the wall that the player can run into. """
		# Call the parent's constructor
		super().__init__()

		# Make a wall, of the size specified in the parameters
		self.image = pygame.Surface([width, height])
		self.image.fill(colour)

		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
			
		group.add(self)
		sprite_list.add(self)
		
class Player(pygame.sprite.Sprite):
	""" This class represents the bar at the bottom that the player
	controls. """

	# Constructor function
	def __init__(self, x, y, cell_dimensions):
		# Call the parent's constructor
		super().__init__()

		# Set height, width
		self.image = pygame.Surface([cell_dimensions * 0.5, cell_dimensions * 0.5])
		self.image.fill(orange)

		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

		# Set speed vector
		self.change_x = 0
		self.change_y = 0
		self.walls = None
		self.end_sprite = None

	def changespeed(self, x, y):
		""" Change the speed of the player. """
		self.change_x += x
		self.change_y += y
 
	def update(self):
		""" Update the player position. """
		# Move left/right
		self.rect.x += self.change_x
 
		# Did this update cause us to hit a wall?
		block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
		for block in block_hit_list:
			# print(block.rect.x, block.rect.y)
			# If we are moving right, set our right side to the left side of
			# the item we hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
			else:
				# Otherwise if we are moving left, do the opposite.
				self.rect.left = block.rect.right
 
		# Move up/down
		self.rect.y += self.change_y
 
		# Check and see if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
		for block in block_hit_list:
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom

		coin_coll = pygame.sprite.collide_rect(self, self.end_sprite)
		if coin_coll:
			self.end_sprite.image.fill(white)
			return True

class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y, radius, surface, sprite_list):
		super().__init__()

		# Make a wall, of the size specified in the parameters
		self.image = pygame.Surface([radius, radius])
		self.image.fill(green)
		# Make our top-left corner the passed-in location.
		self.rect = self.image.get_rect()
		self.rect.y = y - int(radius / 2)
		self.rect.x = x - int(radius / 2)
			
		sprite_list.add(self)

def get_dimensions(maze):
	if maze.width > maze.height:
		dimension = int(600 / maze.width)
	else:
		dimension = int(600 / maze.height)
	return dimension



def main(width, height, difficulty = 0):
	pygame.init()
	currentLevel = Maze(width, height, difficulty)
	currentLevel.init()
	cell_dimensions = get_dimensions(currentLevel)
	window = Window(((currentLevel.width * cell_dimensions) + cell_dimensions), ((currentLevel.height * cell_dimensions) + cell_dimensions), "Yet Another Maze Game", cell_dimensions, currentLevel)
	for i in range(len(currentLevel.cells.values())):
		if i == 0:
			playerstart = window.render_cell(currentLevel.cells[i], cell_dimensions, i)
		else:
			window.render_cell(currentLevel.cells[i], cell_dimensions, i)
	x, y = playerstart
	player = Player(x, y, cell_dimensions)
	score = 3 * int(currentLevel.size ** 2)
	player.walls = window.walls_dict.values()
	player.end_sprite = window.render_end(cell_dimensions)
	window.sprite_list.add(player)
	speed = int(cell_dimensions * 0.05) + 1
	gameEnd = False
	waitCount = False
	wait = 10
	while not gameEnd: #game loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.changespeed(-speed, 0)
				elif event.key == pygame.K_RIGHT:
					player.changespeed(speed, 0)
				elif event.key == pygame.K_UP:
					player.changespeed(0, -speed)
				elif event.key == pygame.K_DOWN:
					player.changespeed(0, speed)

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					player.changespeed(speed, 0)
				elif event.key == pygame.K_RIGHT:
					player.changespeed(-speed, 0)
				elif event.key == pygame.K_UP:
					player.changespeed(0, speed)
				elif event.key == pygame.K_DOWN:
					player.changespeed(0, -speed)
		window.window.fill(white)
		scoreDisplay = Text("Score: " + str(score), int(get_dimensions(currentLevel) / 2), window.sprite_list, window.window)
		score = int(score - score * 0.001)
		window.sprite_list.draw(window.window)
		window.sprite_list.update()
		window.sprite_list.remove(scoreDisplay)
		if player.update():
			waitCount = True
		if waitCount:
			wait -= 1
		if wait == 0:
			gameEnd = True
			pygame.quit()
			return
		pygame.display.flip()
		window.clock.tick(60)


if __name__ == '__main__':
	main(10, 10, 50)