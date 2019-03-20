import pygame
from Maze import Maze
import networkx as nx
import matplotlib.pyplot as plt

pygame.init()

#Colours
black = 0, 0, 0
white = 255, 255, 255

class Window:
	"""Class for display window and attributes associated with it such as size"""
	def __init__(self, display_width, display_height, window_title, cell_dimensions):
		self.display_width = display_width
		self.display_height = display_height
		self.window_title = window_title
		self.window = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
		self.window.fill(white)
		pygame.display.set_caption(window_title)
		self.clock = pygame.time.Clock()
		self.walls_dict = {}
		self.walls = pygame.sprite.Group()
		self.cell_dimensions = cell_dimensions
	def get_cell_center(self, cell):
		return (((cell.coord[0] * self.cell_dimensions) + self.cell_dimensions), ((cell.coord[1] * self.cell_dimensions) + self.cell_dimensions))
	def render_cell(self, cell, cell_dimensions, iteration):
		cell_centre = self.get_cell_center(cell)
		cell_deviation = cell_dimensions / 2
		if cell.shell['Top'] == True:
			var_name = "cell_" + str(iteration) + "_top"
			start_x = cell_centre[0] - cell_deviation
			end_x = cell_centre[0] + cell_deviation
			start_y = cell_centre[1] - cell_deviation
			end_y = cell_centre[1] - cell_deviation
			self.walls_dict[var_name] = Wall((start_x, start_y), (end_x, end_y), self.window, self.walls)
		else:
			pass
		if cell.shell['Bottom'] == True:
			var_name = "cell_" + str(iteration) + "_bottom"
			start_x = cell_centre[0] - cell_deviation
			end_x = cell_centre[0] + cell_deviation
			start_y = cell_centre[1] + cell_deviation
			end_y = cell_centre[1] + cell_deviation
			self.walls_dict[var_name] = Wall((start_x, start_y), (end_x, end_y), self.window, self.walls)
		else:
			pass
		if cell.shell['Left'] == True:
			var_name = "cell_" + str(iteration) + "_left"
			start_x = cell_centre[0] - cell_deviation
			end_x = cell_centre[0] - cell_deviation
			start_y = cell_centre[1] - cell_deviation
			end_y = cell_centre[1] + cell_deviation
			self.walls_dict[var_name] = Wall((start_x, start_y), (end_x, end_y), self.window, self.walls)
		else:
			pass
		if cell.shell['Right'] == True:
			var_name = "cell_" + str(iteration) + "_right"
			start_x = cell_centre[0] + cell_deviation
			end_x = cell_centre[0] + cell_deviation
			start_y = cell_centre[1] - cell_deviation
			end_y = cell_centre[1] + cell_deviation
			self.walls_dict[var_name] = Wall((start_x, start_y), (end_x, end_y), self.window, self.walls)
		else:
			pass
		# message_display(str(cell.cellNo), cell_centre, self.window, int(get_dimensions(self) / 2))
		return cell_centre
	# def render_end(self):

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
	def __init__(self, start, end, surface, group):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.draw.line(surface, black, start, end)
		group.add(self)

def get_dimensions(maze):
	if maze.width > maze.height:
		dimension = int(500 / maze.width)
	else:
		dimension = int(500 / maze.height)
	return dimension



def main():
	level_1 = Maze(10, 10)
	level_1.soft_main()
	cell_dimensions = get_dimensions(level_1)
	# draw_graph(level_1)
	window = Window(((level_1.width * cell_dimensions) + cell_dimensions), ((level_1.height * cell_dimensions) + cell_dimensions), "Yet Another Maze Game", cell_dimensions)
	for i in range(len(level_1.cells.values())):
		if i == 0:
			playerstart = window.render_cell(level_1.cells[i], cell_dimensions, i)
		else:
			window.render_cell(level_1.cells[i], cell_dimensions, i) #def render_cell(self, cell, cell_dimensions, iteration)
	while True: #game loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		# pygame.draw.circle(window.window, (255, 165, 0), playerstart, int(cell_dimensions / 3))
		pygame.display.update()
		window.clock.tick(60)


if __name__ == '__main__':
	main()