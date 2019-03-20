import pygame
from Maze import Maze
from GraphGraphics import render_graph

pygame.init()

#Colours
black = 0, 0, 255
white = 255, 255, 50
orange = 255, 165, 0

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
	def render_cell(self, cell, cell_dimensions, iteration, nums):
		cell_centre = self.get_cell_center(cell)
		cell_deviation = cell_dimensions / 2
		if cell.shell['Top'] == True:
			var_name = "cell_" + str(iteration) + "_top"
			start_x = cell_centre[0] - cell_deviation
			end_x = cell_centre[0] + cell_deviation
			start_y = cell_centre[1] - cell_deviation
			end_y = cell_centre[1] - cell_deviation
			self.walls_dict[var_name] = Wall((start_x, start_y), (end_x, end_y), self.window, self.walls, self.sprite_list)
		else:
			pass
		if cell.shell['Bottom'] == True:
			var_name = "cell_" + str(iteration) + "_bottom"
			start_x = cell_centre[0] - cell_deviation
			end_x = cell_centre[0] + cell_deviation
			start_y = cell_centre[1] + cell_deviation
			end_y = cell_centre[1] + cell_deviation
			self.walls_dict[var_name] = Wall((start_x, start_y), (end_x, end_y), self.window, self.walls, self.sprite_list)
		else:
			pass
		if cell.shell['Left'] == True:
			var_name = "cell_" + str(iteration) + "_left"
			start_x = cell_centre[0] - cell_deviation
			end_x = cell_centre[0] - cell_deviation
			start_y = cell_centre[1] - cell_deviation
			end_y = cell_centre[1] + cell_deviation
			self.walls_dict[var_name] = Wall((start_x, start_y), (end_x, end_y), self.window, self.walls, self.sprite_list)
		else:
			pass
		if cell.shell['Right'] == True:
			var_name = "cell_" + str(iteration) + "_right"
			start_x = cell_centre[0] + cell_deviation
			end_x = cell_centre[0] + cell_deviation
			start_y = cell_centre[1] - cell_deviation
			end_y = cell_centre[1] + cell_deviation
			self.walls_dict[var_name] = Wall((start_x, start_y), (end_x, end_y), self.window, self.walls, self.sprite_list)
		else:
			pass
		if nums:
			message_display(str(cell.cellNo), cell_centre, self.window, int(get_dimensions(self.maze) / 2))
		return cell_centre
	def render_end(self):
		pass

def message_display(text, center, window, size):
	largeText = pygame.font.Font("freesansbold.ttf", size)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = center
	window.blit(TextSurf, TextRect)
	pygame.display.update()

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

class Wall(pygame.sprite.Sprite):
	"""Class for each wall of each cell, cell class to be passed in along with the specific wall of the cell being rendered, passed in as it's relative position to the centre of the cell"""
	def __init__(self, start, end, surface, group, sprite_list):
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.draw.line(surface, black, start, end, 3)
		group.add(self)
		sprite_list.add(self)

class Player(pygame.sprite.Sprite):
	change_x = 0
	change_y = 0

	def __init__(self, x, y, sprite_list):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([15, 15])
		self.image.fill(black)

		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

		sprite_list.add(self)

	def changespeed(self, x, y):
		self.change_x += x
		self.change_y += y

	def update(self, walls):
		self.rect.x += self.change_x

		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			else:
				self.rect.left = block.rect.right

		self.rect.y += self.change_y

		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom

def get_dimensions(maze):
	if maze.width > maze.height:
		dimension = int(500 / maze.width)
	else:
		dimension = int(500 / maze.height)
	return dimension



def main(width, height, walls, nums = False):
	level_1 = Maze(width, height)
	level_1.soft_main(walls)
	cell_dimensions = get_dimensions(level_1)
	window = Window(((level_1.width * cell_dimensions) + cell_dimensions), ((level_1.height * cell_dimensions) + cell_dimensions), "Yet Another Maze Game", cell_dimensions, level_1)
	# startCell = window.get_cell_center(level_1.cells[0])
	# print("Start:", startCell)
	player = Player(50, 50, window.sprite_list)
	for i in range(len(level_1.cells.values())):
		if i == 0:
			playerstart = window.render_cell(level_1.cells[i], cell_dimensions, i, nums)
		else:
			window.render_cell(level_1.cells[i], cell_dimensions, i, nums) #def render_cell(self, cell, cell_dimensions, iteration)
	while True: #game loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.changespeed(-3, 0)
				elif event.key == pygame.K_RIGHT:
					player.changespeed(3, 0)
				elif event.key == pygame.K_UP:
					player.changespeed(0, -3)
				elif event.key == pygame.K_DOWN:
					player.changespeed(0, 3)

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					player.changespeed(3, 0)
				elif event.key == pygame.K_RIGHT:
					player.changespeed(-3, 0)
				elif event.key == pygame.K_UP:
					player.changespeed(0, 3)
				elif event.key == pygame.K_DOWN:
					player.changespeed(0, -3)

		player.update(window.walls_dict.values())
		# window.window.blit(window.window, player)
		pygame.display.update()
		window.clock.tick(60)


if __name__ == '__main__':
	main(10, 10, 0)