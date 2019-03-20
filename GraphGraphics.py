import networkx as nx
import matplotlib.pyplot as plt
from Maze import Maze

def render_graph(maze):
	G = nx.Graph()
	G.add_nodes_from(maze.graph.keys())
	for i in maze.graph:
		for j in maze.graph[i]:
			G.add_edge(i, j)
	nx.draw(G, with_labels = True)
	plt.show()