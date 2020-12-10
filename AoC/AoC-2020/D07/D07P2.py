DEBUG_PRINT = True
DEBUG_PRINT = False
def debugPrint(thingToPrint):
	if DEBUG_PRINT:
		print(thingToPrint)

""" A Python Class
A simple Python graph class, demonstrating the essential 
facts and functionalities of graphs.
"""

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict


    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        # edge = set(edge)
        vertex1 = edge[0]
        vertex2 = edge[1]
        # if edge:
            # # not a loop
            # vertex2 = edge.pop()
        # else:
            # # a loop
            # vertex2 = vertex1
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A private method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_isolated_vertices(self):
        """ returns a list of isolated vertices. """
        graph = self.__graph_dict
        isolated = []
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

    def find_path(self, start_vertex, end_vertex, path=[]):
        """ find a path from start_vertex to end_vertex 
            in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, 
                                               end_vertex, 
                                               path)
                if extended_path: 
                    return extended_path
        return None
    

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph 
			Don't pass path when calling
		"""
        graph = self.__graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths

    def is_connected(self, 
                     vertices_encountered = None, 
                     start_vertex=None):
        """ determines if the graph is connected """
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__graph_dict        
        vertices = list(gdict.keys()) # "list" necessary in Python 3 
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False

    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted 
            double, i.e. every occurence of vertex in the list 
            of adjacent vertices. """ 
        adj_vertices =  self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def degree_sequence(self):
        """ calculates the degree sequence """
        seq = []
        for vertex in self.__graph_dict:
            seq.append(self.vertex_degree(vertex))
        seq.sort(reverse=True)
        return tuple(seq)

    @staticmethod
    def is_degree_sequence(sequence):
        """ Method returns True, if the sequence "sequence" is a 
            degree sequence, i.e. a non-increasing sequence. 
            Otherwise False is returned.
        """
        # check if the sequence sequence is non-increasing:
        return all( x>=y for x, y in zip(sequence, sequence[1:]))
  

    def delta(self):
        """ the minimum degree of the vertices """
        min = 100000000
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < min:
                min = vertex_degree
        return min
        
    def Delta(self):
        """ the maximum degree of the vertices """
        max = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max

    def density(self):
        """ method to calculate the density of a graph """
        g = self.__graph_dict
        V = len(g.keys())
        E = len(self.edges())
        return 2.0 * E / (V *(V - 1))

    def diameter(self):
        """ calculates the diameter of the graph """
        
        v = self.vertices() 
        pairs = [ (v[i],v[j]) for i in range(len(v)) for j in range(i+1, len(v)-1)]
        smallest_paths = []
        for (s,e) in pairs:
            paths = self.find_all_paths(s,e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        # longest path is at the end of list, 
        # i.e. diameter corresponds to the length of this path
        diameter = len(smallest_paths[-1]) - 1
        return diameter

    @staticmethod
    def erdoes_gallai(dsequence):
        """ Checks if the condition of the Erdoes-Gallai inequality 
            is fullfilled 
        """
        if sum(dsequence) % 2:
            # sum of sequence is odd
            return False
        if Graph.is_degree_sequence(dsequence):
            for k in range(1,len(dsequence) + 1):
                left = sum(dsequence[:k])
                right =  k * (k-1) + sum([min(x,k) for x in dsequence[k:]])
                if left > right:
                    return False
        else:
            # sequence is increasing
            return False
        return True
		
def readFileToListOfStrings():
	inList = []
	with open('input2.txt', 'r') as filehandle:  
		for line in filehandle:
			inList.append(line.rstrip())
	return inList

inList = readFileToListOfStrings()
debugPrint(inList)
newList = []
for row in inList:
	newLine = row.replace('bags','bag')
	newLine = newLine.replace(' bag','')
	newLine = newLine.replace(' contain','')
	newLine = newLine.replace(',','')
	newLine = newLine.replace('.','')
	spLine = newLine.split(' ')
	newList.append(spLine)
for row in newList:
	debugPrint(row)
combList = []
for row in newList:
	state = 'lookingForAdjective'
	combRow = []
	for word in row:
		if state == 'lookingForAdjective':
			adj = word
			state = 'lookingForColor'
		elif state == 'lookingForColor':
			col = word
			state = 'lookingForNumber'
			combRow.append(adj+' '+col)
		elif state == 'lookingForNumber':
			num = word
			if num == 'no':
				state = 'done'
			else:
				combRow.append(int(num))
				state = 'lookingForAdjective'
		debugPrint('combRow ' + str(combRow))
	combList.append(combRow)
	
for row in combList:
	debugPrint(row)

def printGraphText(linksList):
	debugPrint('\ndigraph G {')
	for pair in linksList:
		line = '"' + pair[0] + '" -> "' + pair[1]
		line += '"'
		debugPrint(line)
	debugPrint('}\n')

def printGraphTextBack(linksList):
	debugPrint('\ndigraph G {')
	for pair in linksList:
		line = '"'
		line += pair[1]
		line += '" -> "'
		line += pair[0]
		line += '"'
		debugPrint(line)
	debugPrint('}\n')

linksList = []
for row in combList:
	state = 'lookingForFirstColor'
	firstColor = ''
	for element in row:
		if state == 'lookingForFirstColor':
			firstColor = element
			state = 'lookingForNumber'
		elif state == 'lookingForNumber':
			state = 'lookingForOtherColors'
			number = element
		elif state == 'lookingForOtherColors':
			state = 'lookingForNumber'
			currentColor = element
			linksRow = []
			linksRow.append(firstColor)
			linksRow.append(currentColor)
			linksRow.append(number)
			linksList.append(linksRow)
debugPrint('linksList')
for row in linksList:
	print(row)

DEBUG_PRINT = True
printGraphText(linksList)
DEBUG_PRINT = False

# pointsList - list of the points (a stack)
pointsList = []
def addToPointsList(pointToAdd):
	debugPrint('added to points list'+pointToAdd)
	pointsList.append(pointToAdd)

def getFromPointsList():
	val = pointsList.pop()
	debugPrint('returning from points list' + val)
	return val
		
def isPointsListEmpty():
	return len(pointsList) == 0

# pairsList - list of the pairs
pairsList = []

def addToPairsList(pairToAdd):
	if pairToAdd not in pairsList:
		pairsList.append(pairToAdd)

print('pairsList',pairsList)

addToPointsList('shiny gold')

while not isPointsListEmpty():
	currentPoint = getFromPointsList()
	debugPrint('got out '+ currentPoint)
	for pairOfPoints in linksList:
		#debugPrint('comparing against ' + pairOfPoints[0])
		if pairOfPoints[0] == currentPoint:
			debugPrint('found')
			addToPairsList(pairOfPoints)
			addToPointsList(pairOfPoints[1])

debugPrint(pairsList)
printGraphTextBack(pairsList)

def findListOfEndpoints(pairsList,nodeNamesInGraph):
	endPoints = []
	for nodeName in nodeNamesInGraph:
		isDest = False
		for pair in pairsList:
			if pair[0] == nodeName:
				isDest = True
		if not isDest:
			endPoints.append(nodeName)
#	print('endPoints',endPoints)
	return endPoints

def findListOfStartpoints(pairsList,nodeNamesInGraph):
	endPoints = []
	for nodeName in nodeNamesInGraph:
		isDest = False
		for pair in pairsList:
			if pair[1] == nodeName:
				isDest = True
		if not isDest:
			endPoints.append(nodeName)
#	print('endPoints',endPoints)
	return endPoints

def findAllNodeNamesInGraph(pairsList):
	allNodeNames = []
	for pair in pairsList:
		if pair[0] not in allNodeNames:
			allNodeNames.append(pair[0])
		if pair[1] not in allNodeNames:
			allNodeNames.append(pair[1])
#	print('allNodeNames',allNodeNames)
	return allNodeNames

nodeNamesInGraph = findAllNodeNamesInGraph(pairsList)
print('nodeNamesInGraph',nodeNamesInGraph)
endPointsList = findListOfEndpoints(pairsList,nodeNamesInGraph)
print('endPointsList',endPointsList)
startPointsList = findListOfStartpoints(pairsList,nodeNamesInGraph)
print('startPointsList',startPointsList)
workingStack = []
for point in startPointsList:
	workingStack.append(point)
connections = []
while len(workingStack) > 0:
	currentPoint = workingStack.pop()
	connections.append(currentPoint)
	for pair in pairsList:
		if pair[0] == currentPoint:
			pass

graph = Graph()
for node in nodeNamesInGraph:
	print('adding vertex',node)
	graph.add_vertex(node)
for connection in pairsList:
	print('adding connection',connection)
	graph.add_edge([connection[0],connection[1]])
allPaths = []
for endPoint in endPointsList:
	paths = []
	print('finding path from','shiny gold to',endPoint)
	paths = graph.find_all_paths('shiny gold',endPoint)
	print('paths',paths)
	for path in paths:
		allPaths.append(path)
print('allPaths',allPaths)
