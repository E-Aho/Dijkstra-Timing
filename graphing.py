import numpy as np
from cycler import cycler
import matplotlib.pyplot as plt
import dill
from classes import Results, counter1Max

dillInput = open("output.dict","rb")
results_dict = dill.load(dillInput)

rawInput = open("raw.out", "rb")
raw_dict = dill.load(rawInput)

#Form font types

titleFont = {'family':'serif',
            'size':18,
            }

axesFont = {'family':'serif',
            'size':16
            }

labelFont = {'family':'serif',
            'size': 14,
            'color':'#202020'
            }

X = []
Y = []



for edge in results_dict[30]:
    i = results_dict[30][edge]
    X.append(edge)
    Y.append((i.mean)/1000)

X = np.array(X)
Y = np.array(Y)

plt.rcParams.update({'figure.autolayout': True})

#fig1: 30 vertex mean computational timings
fig1, ax = plt.subplots()
plt.scatter(X,Y,s=2,c='#202020')
plt.ylim(bottom=0)
plt.xlim(left=29,right=436)
ax.set_xlabel('Number of edges', fontdict=axesFont, labelpad=15)
ax.set_ylabel(r'Mean computation time /$\mu s$', fontdict=axesFont, labelpad=15)
plt.title('Mean computation time for each number \n of edges on a 30 vertex network',fontdict=titleFont)
plt.tight_layout()
plt.savefig('30vertices.png', bbox_inches = "tight")


X = []
Y = []


for run in range (len(raw_dict[30][190])):
    X.append(run)
    Y.append(raw_dict[30][190][run]/1000)

X = np.array(X)
Y = np.array(Y)

fig, ax = plt.subplots()
plt.scatter(X,Y,s=2,c='#202020')
plt.ylim(bottom=0)
plt.xlim(left=0, right = 2500)
ax.set_xlabel('i', fontdict=axesFont, labelpad=15)
ax.set_ylabel(r'Computational time /$\mu s$', fontdict=axesFont, labelpad=15)
plt.title('Computational time for each run \n with 30 vertices and 190 edges', fontdict = titleFont)
plt.tight_layout()
plt.savefig('30n190p.png', bbox_inches = 'tight')

X = []
Y = []


for run in range (len(raw_dict[30][195])):
    X.append(run)
    Y.append(raw_dict[30][195][run]/1000)

X = np.array(X)
Y = np.array(Y)

#linear plot 3; for 30 vertices, 195 edges 'anomalous' values
fig, ax = plt.subplots()
plt.scatter(X,Y,s=2,c='#202020')
plt.ylim(bottom=0)
plt.xlim(left=0, right = 2500)
ax.set_xlabel('i', fontdict=axesFont, labelpad=15)
ax.set_ylabel(r'Computational time /$\mu s$', fontdict=axesFont, labelpad=15)
plt.title('Computational time for each run \n with 30 vertices and 195 edges', fontdict = titleFont)
plt.tight_layout()
plt.savefig('30n195p.png', bbox_inches = 'tight')

#logarithmic plot 3
fig, ax = plt.subplots()
plt.scatter(X,Y,s=2,c='#202020')
plt.xlim(left=0, right = 2500)
ax.set_xlabel('i', fontdict=axesFont, labelpad=15)
ax.set_ylabel(r'Computational time /$ log(\mu s)$', fontdict=axesFont, labelpad=15)
plt.yscale('log')
plt.title('Computational time for each run \n with 30 vertices and 195 edges', fontdict = titleFont)
plt.tight_layout()
plt.savefig('30n195plog.png', bbox_inches = 'tight')

#Graph 4 raw
X = np.array([x for x in range (14,31)])
Y = np.array([results_dict[x][90].mean/1000 for x in X])

fig, ax = plt.subplots()
plt.plot(X,Y)
plt.yscale('linear')
plt.xlim(left=10)
plt.ylim(bottom = 100)
plt.title('Mean computational time for \n 90 edges with varying vertex counts', fontdict = titleFont)
ax.set_xlabel('Number of vertices in network (V)', fontdict=axesFont, labelpad=15)
ax.set_ylabel(r'Mean computational time/ $\mu s)$', fontdict=axesFont, labelpad=15)
r2 = str((np.corrcoef(X, Y)[0, 1])**2)
plt.text(18,150,(str('R\u00b2 = ')+r2[:6]),fontdict=axesFont)

plt.savefig('vertexcountraw.png', bbox_inches = 'tight')

#Graph 4, but corrected for xlogx speed

Y = np.array([((results_dict[x][90].mean)*np.log(x))/(1000) for x in X]) 

fig,ax = plt.subplots()
plt.plot(X,Y)
plt.xlim(left = 10)
plt.ylim(bottom = 300)
plt.title('Adjusted mean computational time for \n 90 edges with varying vertex counts', fontdict = titleFont)
ax.set_xlabel('Number of vertices in network (V)', fontdict=axesFont, labelpad=15)
r2 = str((np.corrcoef(X, Y)[0, 1])**2)
plt.text(23,500,(str('R\u00b2 = ')+r2[:6]),fontdict=axesFont)
ax.set_ylabel(r'Mean computational time/ $\mu s/log(V)$', fontdict=axesFont, labelpad=15)
plt.savefig('vertexcountadjusted.png', bbox_inches = 'tight')


#Graph 5
X = np.array([x for x in range (40,105)])

graph5Dict = {}
legendSet = []

for countNodes in range(15,31):
    graph5Dict[countNodes] = []
    for Xi in X:
        try:
            graph5Dict[countNodes].append(results_dict[countNodes][Xi].mean/1000) 
            pass
        except KeyError:
            pass
fig,ax = plt.subplots()

colorSet = ['DarkRed','Red','LightSalmon',
'DarkOrange','Orange','Gold','GreenYellow','LimeGreen','ForestGreen',
'Aquamarine','Aqua','DeepSkyBlue','DarkBlue','BlueViolet',
'Indigo','Thistle']

lines = []
for countNodes in range(30,14,-1):
    lines += plt.plot(X, graph5Dict[countNodes],color = colorSet[countNodes-15], label ='V= '+str(countNodes))

plt.legend(loc ='upper left', bbox_to_anchor=(1,1,0,0.02), edgecolor = 'White')

plt.title('Mean computational time for \n varying edge and vertex count', fontdict = titleFont)
ax.set_xlabel('Number of edges (E)', fontdict=axesFont, labelpad=15)
ax.set_ylabel(r'Mean computational time/ $\mu s$', fontdict=axesFont, labelpad=15)

plt.savefig('15to30vertexcount.png', bbox_inches = 'tight')



fig,ax = plt.subplots()

#Graph 6
colorSet = ['Pink','DarkRed','Red','LightSalmon',
'DarkOrange','Orange','Gold','Khaki','GreenYellow','LimeGreen',
'ForestGreen','LightSeaGreen','Aquamarine','Aqua','DeepSkyBlue',
'SkyBlue','DarkBlue','BlueViolet','Indigo','Thistle','Lavender',
'MediumVioletRed']

lines = []
for countNodes in range(30,9,-1):
    X = np.array([x for x in range(countNodes, int((countNodes *(countNodes-1))/2))])
    lines += ax.plot(X, [(results_dict[countNodes][x].mean)/1000 for x in X]
    ,color = colorSet[countNodes-10], label ='V= '+str(countNodes))

plt.legend(loc ='upper left', bbox_to_anchor=(1,1,0,0.02), edgecolor = 'White',fontsize = 'x-small')
plt.xlim(left = 10, right = 190)
plt.ylim(top = 400)
plt.title('Mean computational time for \n varying edge and vertex count', fontdict = titleFont)
ax.set_xlabel('Number of edges (E)', fontdict=axesFont, labelpad=15)
ax.set_ylabel(r'Mean computational time/ $\mu s$', fontdict=axesFont, labelpad=15)

plt.savefig('10to30v_left.png', bbox_inches = 'tight')

plt.xlim(left = 190,right = 436)
plt.ylim(bottom=200, top = 1000)
plt.savefig('10to30v_right.png', bbox_inches = 'tight')

plt.xlim(left = 10, right = 436)
plt.ylim(bottom = 0, top = 1000)
plt.savefig('10to30v_all.png', bbox_inches = 'tight')

X = []
Y = []

for edge in results_dict[30]:
    i = results_dict[30][edge]
    X.append(edge)
    Y.append(i.countNT)

X = np.array(X)
Y = np.array(Y)

#Graph 7, show how many non connected counts occur for 30 vertices for each count edges
fig1, ax = plt.subplots()
plt.scatter(X,Y,s=2,c='#202020')
plt.ylim(bottom=0)
plt.xlim(left=29,right=436)
ax.set_xlabel('Number of edges', fontdict=axesFont, labelpad=15)
ax.set_ylabel('Count of disconnected networks', fontdict=axesFont, labelpad=15)
plt.title('How many disconnected networks were \n generated for 30 vertex networks',fontdict=titleFont)
plt.tight_layout()
plt.savefig('30vNT.png', bbox_inches = "tight")

#Graph 8; Adjusted variant of Graph 6 to show how it looks upon removing timings over 20ms
fig,ax = plt.subplots()
graph8dict = {}


for countNodes in range (30,9,-1):
    graph8dict[countNodes]={}
    for paths in (results_dict[countNodes]):
        tempList = []
        for timing in raw_dict[countNodes][paths]:
            if paths > 330:
                if timing < 2000000:
                    tempList.append(timing)
            elif paths == 195:
                if countNodes > 24:
                    if timing < 1000000:
                        tempList.append(timing)
                else:
                    if timing < 700000:
                        tempList.append(timing)
            else:
                if timing < 1000000:
                    tempList.append(timing)

        if len(tempList) > 0:
            meanTiming = (sum(tempList)/len(tempList))
        else:
            meanTiming = 0
        graph8dict[countNodes][paths] = meanTiming

lines = []
for countNodes in range(30,9,-1):
    X = np.array([x for x in range(countNodes, int((countNodes *(countNodes-1))/2))])
    lines += ax.plot(X, [(graph8dict[countNodes][x])/1000 for x in X]
    ,color = colorSet[countNodes-10], label ='V= '+str(countNodes))

plt.legend(loc ='upper left', bbox_to_anchor=(1,1,0,0.02), edgecolor = 'White',fontsize = 'x-small')
plt.xlim(left = 10, right = 436)
plt.ylim(top = 800)
plt.title('Mean (corrected) computational time for \n varying edge and vertex count', fontdict = titleFont)
ax.set_xlabel('Number of edges (E)', fontdict=axesFont, labelpad=15)
ax.set_ylabel(r'Mean computational time/ $\mu s$', fontdict=axesFont, labelpad=15)
plt.savefig('10to30vCOR1.png', bbox_inches = "tight")


#linear plot 9; for 24 vertices, 195 edges 'anomalous' values
X = []
Y = []


for run in range (len(raw_dict[23][208])):
    X.append(run)
    Y.append(raw_dict[23][208][run]/1000)

X = np.array(X)
Y = np.array(Y)


fig, ax = plt.subplots()
plt.scatter(X,Y,s=2,c='#202020')
plt.ylim(bottom=0)
plt.xlim(left=0, right = 2500)
ax.set_xlabel('i', fontdict=axesFont, labelpad=15)
ax.set_ylabel(r'Computational time /$\mu s$', fontdict=axesFont, labelpad=15)
plt.title('Computational time for each run \n with 23 vertices and 208 edges', fontdict = titleFont)
plt.tight_layout()
plt.savefig('23n228p.png', bbox_inches = 'tight')

