import math
import numpy as np
import random as rnd
import copy
import time
import dill
import datetime
from classes import counter1Max, nodePair, edge, Results


#Create 'dictionary of dictionaries' structure to store timings of runs
#timingDictionary[Nodes][Paths] is a list of all timings for that number of nodes and paths.


timingDictionary = {}
for countNodes in range (10,31):

        print('Starting ', countNodes)

        timingDictionary[countNodes] = {}

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


        #Run for each number of possible paths
        pathMax = countNodePair
        pathMin = (countNodes - 1)

        for countPaths in range(pathMin, pathMax+1):
                timingDictionary[countNodes][countPaths] = []

                currentTime = datetime.datetime.now()
                print("run:", countPaths, "             ", currentTime, "\n")


                #Generate list of distances, randomly giving an integer between 1 and 20 for each path.
                #Makes number of paths as input above
                counter1 = 0
                while counter1 < counter1Max:

                        counter1 +=1    
                        distanceList = []
                        i = 0
                        while i < countNodePair:
                                if i < countPaths:
                                        distanceList.append(int(rnd.randint(1,21))) #Arbitrarily chosen 20 as maximum
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
                        tempList = [] #reset temp var, save memory



                        #Djikstra function
                        
                        while True: #try/except used to exclude non connected graphs
                                try:
                                        t_Start = time.perf_counter_ns()
                                        n0 = 0

                                        minDistances = {}
                                        prevNode = {}

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


                                                unvisitedList.remove(currentNode)

                                                for k in range (len(connections[currentNode])):
                                                        node = ((connections[currentNode])[k]).end
                                                        edgeLength = ((connections[currentNode])[k]).distance
                                                        newDistance = edgeLength + minDistances[currentNode]
                                                        if newDistance < minDistances[node]:
                                                                minDistances[node] = newDistance
                                                                prevNode[node] = v

                                        #timing stuff
                                        t_End = time.perf_counter_ns()
                                        t_Completed = t_End - t_Start
                                        timingDictionary[countNodes][countPaths].append(t_Completed)
                                        break
                                except ValueError: #If value error occurs, network was non connected
                                        break
        
#Write data into new file
with open("raw.out","wb") as dillRaw:
        dill.dump(timingDictionary, dillRaw)
        dillRaw.close()


#Write results dictionary with mean as a new file
avgDict = {}

for nodes in timingDictionary:
        avgDict[nodes] = {}
        for paths in timingDictionary[nodes]:
                tList = timingDictionary[nodes][paths]
                CT = len(tList)
                NT = (counter1Max - CT)
                if CT > 0:
                        mn = int((sum(tList))/CT)
                else:
                        mn = 0 
                avgDict[nodes][paths] = Results(nodes,paths,mn,NT)

with open("output.dict","wb") as dillOutput: 
        dill.dump(avgDict, dillOutput)
        dillOutput.close()

print ('Script Finished!')