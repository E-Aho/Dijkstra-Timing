from string import ascii_lowercase as alphabet
import math
import random as rnd
import copy




#This script is a self contained script which demonstrates how a single run works.

#Prompt countNodes
while True:
        countNodes = int(input('How many nodes will be in the network? For this demonstration, the number must between 4 and 50\n'))
        if isinstance(countNodes,int) == True:
                if countNodes < 4: 
                        print ('That is too small.\n')
                elif countNodes > 50:
                        print ('That is too large.\n')
                else:
                        break
        else:
                print ('Please enter an integer value for the number of nodes.\n')

vertexList =[]
nodePairList = []

i = 0
L0 = 'a'


#Generate list of vertices from lower case ascii strings.
#Also generates node pair list, includes all unique & ordered pairings of vertices
while i < countNodes:
        L1Val = ord(L0) + i
        for L2Val in range(i+1, countNodes):
                tempPath = [chr(L1Val),chr((ord(L0)+L2Val))]
                nodePairList.append(tempPath)
        vertexList.append(chr(L1Val))
        i+=1        
countNodePair = len(nodePairList)



#Define node pair. To be used as initial proxy to edge.
class nodePair:
        def __init__(self, nodes, distance):
                self.nodes = nodes
                self.node1 = nodes[0]
                self.node2 = nodes[1]
                self.distance = distance


#Take sanitized input integer number of paths to randomly make
while True:
        
        countPaths = int((input(str('How many paths shall be made? Must be greater than {bottom} and less than {top} \n').format(
                bottom=(countNodes-1),top=countNodePair)))) ##TBD: CHECK LIMITS
        if countPaths >= (countNodes-1):
                if countPaths <= countNodePair:
                        break
                else:
                        print('That is too large.\n')
        else:
                print('That is too small.\n')

#Generate list of distances, randomly giving an integer between 1 and 20 for each path.
#Makes number of paths as input above

print(str('Now assigning {paths} paths randomly between nodes, with lengths assigned randomly between 1 and 20 A.U.\n').format(paths=countPaths))

distanceList = []
i = 0
while i < countNodePair:
        if i < countPaths:
                distanceList.append(int(rnd.randint(1,20)))
                i+=1
                pass
        else:
                distanceList.append('null')
                i+=1
                pass
        
rnd.shuffle(distanceList,)   #randomises order of distance list so that random node pairs are assigned edges


#Generate list of all edges in the form of nodePairs. 
#nodePairs will be later altered to be class 'edge'
tempEdgeList = [nodePair(nodePairList[i], distanceList[i]) for i in range(countNodePair)] #NB: can optimise by removing need for this temporary list
edgeList = []
i = 0
while i < len(tempEdgeList):
        if isinstance(tempEdgeList[i].distance, str) == True:
                i+=1
                pass
        else:
                edgeList.append(tempEdgeList[i])
                i+=1
                pass

tempEdgeList = []


#define new classes that will be used for the actual analysis
class edge:
        def __init__ (self, end, distance):
                self.end = end
                self.distance = distance

class vertex:
        def __init__ (self, edges):
                self.edges = edges
                self.connectivity = len(edges)

connections = {} #Dictionary where key is vertex str to list of edges
for i in vertexList:
        tempList = []
        for j in range(len(edgeList)):
                J = edgeList[j]
                if J.node1 == i:
                        tempList.append(edge(J.node2, J.distance))
                elif J.node2 == i:
                        tempList.append(edge(J.node1, J.distance))
        
        connections[i] = tempList
tempList = [] #reset temp var


for i in range(len(vertexList)):
        print('connectivity to node', vertexList[i], '=', len(connections[vertexList[i]]))
#Have currently each node's connectivity

totConnectivity = 0
for i in range(len(vertexList)):
        totConnectivity = totConnectivity + len(connections[vertexList[i]])

print('\n--------------------\n Now running Dijkstra function.\n--------------------\n')

#Dijkstra function

print('Starting at node "a"')

pathingDict = {}
try:
        for n0 in range(1): #May be altered to vary starting positions

                
                minDistances = {}
                prevNode = {}
                prevNode['a']=['a']

                #initialize
                unvisitedList = copy.deepcopy(vertexList)
                u = unvisitedList[n0]
                for v in unvisitedList:
                        minDistances[v] = math.inf
                minDistances[u] = 0          #same node
                
                while len(unvisitedList) > 0:
                        tempDist = math.inf
                        for v in unvisitedList:
                                if minDistances[v] < tempDist:
                                        tempDist = minDistances[v]
                                        currentNode = v

                        print("List of unvisited nodes:", unvisitedList)
                        print("Current node:", currentNode)
                        unvisitedList.remove(currentNode)

                        for k in range (len(connections[currentNode])):
                                node = ((connections[currentNode])[k]).end
                                edgeLength = ((connections[currentNode])[k]).distance
                                print (str('{curnode}{node} has edge length = {len}').format(curnode=currentNode,node=node,len=edgeLength))
                                newDistance = edgeLength + minDistances[currentNode]
                                print (str('Shortest distance via {curnod} ={len}').format(curnod=currentNode,len=newDistance))
                                if newDistance < minDistances[node]:
                                        minDistances[node] = newDistance
                                        prevNode[node] = currentNode
                                        print('New shortest path to',node)
                        if len(unvisitedList) > 0:
                                print('Select new node; unvisited node with shortest distance to a. \n')
                        else:
                                print('All nodes visited. Shortest distances from a to each node below.\n \n---------------\n')

        

        for v in vertexList:
                pathingDict[v] = [v]
                while True:
                        if pathingDict[v][-1] == 'a':
                                break
                        else:
                                pathingDict[v].append(prevNode[pathingDict[v][-1]])
                route = pathingDict[v][-1::-1]
                print (str('Shortest path from a to {v} = {minD} :         Route = {r}').format(v=v,minD=minDistances[v],r=''.join(route)))

except ValueError:
        print('This randomized network is not connected. Try choosing more paths in the next run.')




