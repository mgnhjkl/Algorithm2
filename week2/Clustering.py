class Edge():
	"""docstring for edge"""
	vertex1 = 0
	vertex2 = 0
	cost = 0
	def __init__(self, edge_info):
		edge_info = edge_info.split()
		self.vertex1 = int(edge_info[0]) - 1 
		self.vertex2 = int(edge_info[1]) - 1
		self.cost = int(edge_info[2])
	def __str__(self):
		return str(self.cost)

class Vertex():
	number = 0
	parent_node = 0
	def __init__(self, number):
		self.number = number
		self.parent_node = number

class Union():
	vertices = []
	space = 0
	parent_node = 0
	def __init__(self, vertex):
		self.vertices = [vertex]
		self.space = 1
		self.parent_node = vertex.parent_node
	def unify(self, union2):
		for vertex in union2.vertices:
			vertex.parent_node = self.parent_node
		self.vertices += union2.vertices
		self.space += union2.space
		union2.clear()
	def clear(self):
		self.vertices = []
		self.space = 0
		self.parent_node = -1

def find(vertices, vertex_number):
	return vertices[vertex_number].parent_node

def fuse(union1, union2):
	if union1.space >= union2.space:
		union1.unify(union2)
	else:
		union2.unify(union1)

def comparator(edge1, edge2):
	if edge1.cost > edge2.cost:
		return 1
	elif edge1.cost < edge2.cost:
		return -1
	else:
		return 0

def run():
	text = open("clustering1.txt")
	line = text.readline()
	number_of_nodes = int(line)
	number_of_unions = number_of_nodes
	vertices = [Vertex(index) for index in range(number_of_nodes)]
	line = text.readline()
	edges = []
	while line:
		new_edge = Edge(line)
		edges.append(new_edge)
		line = text.readline()
	graph = (vertices, edges)
	unions = []
	for vertex in graph[0]:
		unions.append(Union(vertex))
	edges = sorted(edges, cmp = comparator)
	current_edge = 0
	while number_of_unions > 4:
		edge = edges[current_edge]
		union_number1 = find(vertices, edge.vertex1)
		union_number2 = find(vertices, edge.vertex2)
		print "union:" + str(union_number1) +" " +str(union_number2)
		if union_number1 != union_number2:
			fuse(unions[union_number1], unions[union_number2])
			number_of_unions -= 1
		current_edge += 1
	while 1:
		edge = edges[current_edge]
		union_number1 = find(vertices, edge.vertex1)
		union_number2 = find(vertices, edge.vertex2)
		if union_number1 != union_number2:
			print union_number1, union_number2
			print edge.cost
			break
		current_edge += 1
	for union in unions:
		if union.space > 1:
			print union.parent_node

	#print edges[current_edge].cost
run()
	