from poc_queue import Queue

def distance(vertex1, vertex2, bits=24):
	"""
	return hamming distance between integer a and b
	"""
	x = vertex1.value ^ vertex2.value
	return sum((x >> i & 1) for i in xrange(bits))

class Vertex():
	"""docstring for Vertex"""
	value = 0
	index = 0
	edges = []
	def __init__(self, value, index):
		self.value = value
		self.index = index
	def add_edge(self, edge):
		if len(self.edges) == 0:
			self.edges = [edge]
		else:
			self.edges.append(edge)
	def find_connected_vertices(self):
		connected_vertices = []
		for edge in self.edges:
			if edge.vertex1.index == self.index:
				connected_vertices.append(edge.vertex2)
			else:
				connected_vertices.append(edge.vertex1)
		return connected_vertices

class Edge():
	"""docstring for edge"""
	vertex1 = None
	vertex2 = None
	def __init__(self, vertex1, vertex2):
		self.vertex1 = vertex1
		self.vertex2 = vertex2
	def __str__(self):
		return str((self.vertex1.index, self.vertex2.index))

class Graph():
	"""docstring for Graph"""
	vertices = []
	edges = []
	def __init__(self, vertices, edges):
		self.vertices = vertices[:]
		self.edges = edges[:]

def write_edges():
	text = open("clustering_big.txt")
	line = text.readline()
	num_of_nodes = line.split()[0]
	scale = int(line.split()[0])
	vertices = []
	edges = []
	line = text.readline()
	test_scale = 500
	test_control = 1
	while line and test_control <= test_scale:
		line = line.replace(" ", "")
		vertices.append(Vertex(int(line, 2), test_control-1))
		test_control += 1
		line = text.readline()

	output = open("edges", "w")

	for index_i in range(test_scale):
		current_vertex = vertices[index_i]
		for index_j in range(index_i + 1, test_scale):
			vertex_cmp = vertices[index_j]
			dist = distance(current_vertex, vertex_cmp)
			if dist < 3:
				new_edge = Edge(current_vertex, vertex_cmp)
				edges.append(new_edge)
				#output.write(str(current_vertex.index) + " " + str(vertex_cmp.index) + "\n")
	return edges

def run():
	text = open("clustering_big.txt")
	line = text.readline()
	#num_of_nodes = line.split()[0]
	#scale = int(line.split()[0])
	scale = 500
	vertices = []
	edges = write_edges()
	print len(edges)
	for edge in edges:
		print edge.vertex1.value, edge.vertex2.value
	line = text.readline()
	test_scale = scale
	test_control = 1
	while line and test_control <= test_scale:
		line = line.replace(" ", "")
		vertices.append(Vertex(int(line, 2), test_control-1))
		test_control += 1
		line = text.readline()

	"""
	text = open("edges_test")
	line = text.readline()
	
	while line:
		vertex1_index = int(line.split()[0])
		vertex2_index = int(line.split()[1])
		vertex1 = vertices[vertex1_index]
		vertex2 = vertices[vertex2_index]
		edge = Edge(vertex1, vertex2)
		edges.append(edge)
		vertex1.add_edge(edge)
		vertex2.add_edge(edge)
		line = text.readline()
	"""
	for edge in edges:
		vertex1 = vertices[edge.vertex1.index]
		vertex2 = vertices[edge.vertex2.index]
		vertex1.add_edge(edge)
		vertex2.add_edge(edge)
	visited_vertices = [0 for index in range(scale)]
	current_vertex_index = 0
	num_of_components = 0
	while current_vertex_index < scale:
		if visited_vertices[current_vertex_index]:
			# print vertices[current_vertex_index].value
			current_vertex_index += 1
			continue
		num_of_components += 1
		current_vertex = vertices[current_vertex_index]
		tmp_queue = Queue()
		tmp_queue.enqueue(current_vertex)
		while len(tmp_queue):
			v = tmp_queue.dequeue()
			if visited_vertices[v.index] == 0:
				visited_vertices[v.index] = 1
				connected_vertices = v.find_connected_vertices()
				for connected_vertex in connected_vertices:
					tmp_queue.enqueue(connected_vertex)
				
	print num_of_components

run()

