import arff
import numpy as numpy
from matplotlib import pyplot as plt
from scipy.spatial import distance

arffFileName = input("Insert ARFF file name: ")
loadedArff = arff.load(open(arffFileName, 'r'))
k = int(input("Insert K-dist: "))

# list of points
pointsOriginal = loadedArff.get('data')
print("Found: " + str(len(pointsOriginal)) + " points")
print("Calculating Euclidean Distances...")
distances = []
pointsCopy = pointsOriginal[:]
for point in pointsOriginal:
    point1 = point
    point1Distances = []
    distances.append(point1Distances)
    for point2 in pointsCopy:
        point1Distances.append(distance.euclidean(point1, point2))
    point1Distances.sort()

print("Filtering K-Nearest-Neighbors...")
pointsToPlot = []
for distancesOfPoint in distances:
    pointsToPlot.append([0, distancesOfPoint[k]])

print("Sorting Euclidean Distances descending...")
pointsToPlot.sort(reverse=True, key=lambda p: p[1])
fakeXAxis = 1
for p in pointsToPlot:
    p[0] = fakeXAxis
    fakeXAxis += 1

print("Building Scatter plot...")
plotData = numpy.array(pointsToPlot)
x, y = plotData.T
plt.scatter(x, y)
plt.ylabel(str(k) + '-dist')
plt.xlabel('points')
plt.show()
