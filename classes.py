counter1Max = 2500 #number of runs for each number of paths

class nodePair: #used to construct network
        def __init__(self, nodes, distance):
                self.nodes = nodes
                self.node1 = nodes[0]
                self.node2 = nodes[1]
                self.distance = distance

class edge: #used in dictionary, with one vertex as key, to give all connected nodes to that vertex and their distances
        def __init__ (self, end, distance):
                self.end = end
                self.distance = distance

class Results: #used to present outputs and be interpreted in graphing script
        def __init__ (self, nodes, paths, mean, countNT):
                self.nodes = nodes
                self.paths = paths
                self.mean = mean
                self.countNT = countNT
                self.countT = counter1Max - countNT