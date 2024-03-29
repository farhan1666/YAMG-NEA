from Cells import Cell
from random import choice, randint
from sys import setrecursionlimit
class Maze:
	def __init__(self, width, height, difficulty = 0):
		self.cells = dict()
		self.graph = dict()
		self.distances = dict()
		self.height = height
		self.width = width
		self.size = self.width * self.height
		self.dfs_stack = list()
		self.i = 1
		self.difficulty = difficulty
		self.end = None
		setrecursionlimit(30001)
		self.generate_cells()
		self.get_adjacent_cells()
		self.init_graph()
		self.generate_maze(self.cells[0])
		self.extra_paths(self.difficulty)
		self.get_distances()
	def generate_cells(self):
		for i in range(self.size):
			self.cells[i] = Cell(i)
			self.cells[i].coord = self.cells[i].cellNo % self.width, int(self.cells[i].cellNo / self.width)
	def get_adjacent_cells(self):
		for i in range(self.size):
			if self.cells[i].cellNo - self.width >= 0:
				self.cells[i].adjacent_cells[self.cells[i].cellNo - self.width] = 'Top'
			if self.cells[i].cellNo + self.width <= (self.size) - 1:
				self.cells[i].adjacent_cells[self.cells[i].cellNo + self.width] = 'Bottom'
			if (self.cells[i].cellNo - 1) % self.width <= self.cells[i].cellNo % self.width:
				self.cells[i].adjacent_cells[self.cells[i].cellNo - 1] = 'Left'
			if (self.cells[i].cellNo + 1) % self.width >= self.cells[i].cellNo % self.width:
				self.cells[i].adjacent_cells[self.cells[i].cellNo + 1] = 'Right'
			else:
				pass

	def break_wall(self, cell_1, cell_2, post_generation = False):
		if cell_2.cellNo in cell_1.adjacent_cells.keys():
			relPosition = cell_1.adjacent_cells[cell_2.cellNo]
			if not post_generation:
				if cell_2.visited == False:
					cell_1.shell[relPosition] = False
					if relPosition == 'Top':
						cell_2.shell['Bottom'] = False
					elif relPosition == 'Bottom':
						cell_2.shell['Top'] = False
					elif relPosition == 'Right':
						cell_2.shell['Left'] = False
					elif relPosition == 'Left':
						cell_2.shell['Right'] = False
					else:
						pass
			else:
				cell_1.shell[relPosition] = False
				if relPosition == 'Top':
					cell_2.shell['Bottom'] = False
				elif relPosition == 'Bottom':
					cell_2.shell['Top'] = False
				elif relPosition == 'Right':
					cell_2.shell['Left'] = False
				elif relPosition == 'Left':
					cell_2.shell['Right'] = False
				else:
					pass
		else:
			pass
		self.graph[cell_1.cellNo].add(cell_2.cellNo)
		self.graph[cell_2.cellNo].add(cell_1.cellNo)

	def init_graph(self):
		for i in range(self.size):
			self.graph[i] = set()

	def check_unvisited_adjacent_cells(self, Cell):
		output = []
		for i in Cell.adjacent_cells.keys():
			if self.cells[i].visited == False:
				output.append(i)
		return output

	def generate_maze(self, currentCell):
		currentCell.visited = True
		if len(self.dfs_stack) != 0:
			if self.dfs_stack[-1] is not currentCell.cellNo:
				self.dfs_stack.append(currentCell.cellNo)
			else:
				pass
		else:
			self.dfs_stack.append(currentCell.cellNo)
		if len(self.check_unvisited_adjacent_cells(currentCell)) != 0:
			newCell = choice(self.check_unvisited_adjacent_cells(currentCell))
			self.break_wall(currentCell, self.cells[newCell])
			self.generate_maze(self.cells[newCell])
		else:
			if len(self.dfs_stack) != 0:
				self.dfs_stack.pop()
				if len(self.dfs_stack) != 0:
					self.generate_maze(self.cells[self.dfs_stack[-1]])
				else:
					pass
			else:
				pass
			
	def extra_paths(self, n):
		for i in range(n):
			randCell = self.cells[randint(0, (self.size) - 1)]
			self.break_wall(randCell, self.cells[choice(list(randCell.adjacent_cells))], True)
	def get_distances(self):
		queue = [0]
		self.distances[0] = 0
		while queue:
			current = queue.pop()
			for node in self.graph[current]:
				if node not in self.distances:
					queue.append(node)
					self.distances[node] = self.distances[current] + 1
				else:
					if self.distances[current] + 1 < self.distances[node]:
						self.distances[node] = self.distances[current] + 1
						queue.append(node)
		self.end = self.cells[max(self.distances, key = self.distances.get)]

def main(width, height, walls):
	level_1 = Maze(width, height)

if __name__ == '__main__':
	main(5, 5, 0)