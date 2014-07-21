from poc_queue import Queue

def gen_all_neighbors(str1):
	neighbors = []
	for index in range(len(str1)):
		new_str = str1[0:index] + reverse_char(str1[index]) + str1[index+1:]
		neighbors.append(int(new_str, 2))
	for index_i in range(len(str1)):
		for index_j in range(index_i + 1, len(str1)):
			new_str = str1[0:index_i] + reverse_char(str1[index_i]) + str1[index_i+1: index_j] + reverse_char(str1[index_j]) + str1[index_j+1:]
			neighbors.append(int(new_str, 2))
	return neighbors

def reverse_char(char):
	if char == '0':
		char = '1'
	else:
		char = '0'
	return char

class Vertex():
	"""docstring for Vertex"""
	key = 0
	string = ""
	visited = 0
	def __init__(self, line):
		line = line.replace(" ", "")
		line = line.replace("\n", "")
		self.string = line
		self.key = int(line, 2)
		self.visited = 0

def run():
	vertices = {}
	text = open("clustering_big.txt")
	line = text.readline()
	scale = 200000
	line = text.readline()
	scale_ctr = 0
	while line and scale_ctr < scale:
		new_vertex = Vertex(line)
		vertices[new_vertex.key] = new_vertex
		line = text.readline()
		scale_ctr += 1
	num_of_components = 0
	print vertices[15616112].string
	for index in vertices:
		vertex = vertices[index]
		if vertex.visited:
			continue
		num_of_components += 1
		vertex.visited = 1
		print num_of_components
		queue = Queue()
		for neighbor in gen_all_neighbors(vertex.string):
			if vertices.has_key(neighbor) == 0 or vertices[neighbor].visited:
				continue
			queue.enqueue(neighbor)
		while len(queue):
			key = queue.dequeue()
			if vertices.has_key(key) == 0 or vertices[key].visited == 1:
				continue
			vertices[key].visited = 1
			for neighbor in gen_all_neighbors(vertices[key].string):
				if vertices.has_key(neighbor) == 0 or vertices[neighbor].visited == 1:
					continue
				queue.enqueue(neighbor)

run()