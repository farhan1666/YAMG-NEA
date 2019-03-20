class Cell:
	def __init__(self, cellNo):
		self.cellNo = cellNo
		self.visited = False
		self.adjacent_cells = {}
		self.shell = {'Top':True, 'Right':True, 'Bottom':True, 'Left':True}
		self.coord = None
		self.rect = None