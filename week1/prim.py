import heapq
import random

class Edge:
	"""docstring for edge"""
	vertices = [0, 0]
	cost = 0
	def __init__(self, edge_info):
		edge_info = edge_info.split()
		tmp = [0, 0]
		self.vertices = tmp
		self.vertices[0] = int(edge_info[0]) - 1 
		self.vertices[1] = int(edge_info[1]) - 1
		self.cost = int(edge_info[2])
	def __str__(self):
		return str(self.cost)
	def __lt__(self, other):
		return self.cost < other.cost
	def __eq__(self, other):
		return self.cost == other.cost
	def __gt__(self, other):
		return self.cost > other.cost

class Vertex:
	index = 0
	edges = list()
	def __init__(self, index):
		self.index = index
	def add_edge(self,edge):
		if len(self.edges) == 0:
			self.edges = [edge]
		else:
			self.edges.append(edge)
class Graph:
	edges = []
	vertices = {}
	def __init__(self, edges):
		self.edges = edges[:]
		for edge in self.edges:
			for vertex in edge.vertices:
				if not self.vertices.has_key(vertex):
					new_vertex = Vertex(vertex)
					new_vertex.add_edge(edge)
					self.vertices[vertex] = new_vertex
				else:
					self.vertices[vertex].add_edge(edge)

def prim(graph):
	mst = []
	edge_heap = []
	visited_vertices = {}
	unvisited_vertices = graph.vertices

	seed_vertex = unvisited_vertices[random.randint(0, len(unvisited_vertices) - 1)]
	visit_vertex(seed_vertex, visited_vertices, unvisited_vertices, edge_heap)
	while len(edge_heap):
		least_cost_edge = heapq.heappop(edge_heap)
		if not (visited_vertices.has_key(least_cost_edge.vertices[0]) and visited_vertices.has_key(least_cost_edge.vertices[1])):
			mst.append(least_cost_edge)
			if visited_vertices.has_key(least_cost_edge.vertices[0]):
				visit_vertex(graph.vertices[least_cost_edge.vertices[1]], visited_vertices, unvisited_vertices, edge_heap)
			else:
				visit_vertex(graph.vertices[least_cost_edge.vertices[0]], visited_vertices, unvisited_vertices, edge_heap)
	return mst

def visit_vertex(vertex, visited_vertices, unvisited_vertices, heap):
	visited_vertices[vertex.index] = vertex
	del(unvisited_vertices[vertex.index])
	for edge in vertex.edges:
		heapq.heappush(heap, edge)

def run():
	edges = []
	text = open("edges.txt")
	line = text.readline()
	line = text.readline()
	while line:
		edges.append(Edge(line))
		line = text.readline()
	heapq.heapify(edges)
	graph = Graph(edges)
	mst = prim(graph)
	cost_sum = 0
	for edge in mst:
		cost_sum += edge.cost
	print cost_sum

run()

