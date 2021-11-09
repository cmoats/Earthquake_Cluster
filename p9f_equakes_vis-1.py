'''World-wide earthquake Watch CIS 210 W19 Project 9-1

Author: Cameron Moats

Credits: Prior programming experience and textbook

Uses file processing and data mining to find patterns of earthquake activity around the world and plots
those results onto a map
'''

from math import sqrt 
import random
import turtle

def readFile(filename):
    '''(str) -> dict

    reads a file of earthquake data and it returns a dictionary of
    the lattitude and longitude coordinates

    >>> readFile('equakes50f.txt')
    {1: [-125.815, 43.756, 5.2], 2: [-122.0086667, 42.2915, 5.1], 3: [-122.0583333, 42.3575, 6.0],
    4: [-122.0266667, 42.3161667, 5.9], 5: [-122.6065, 45.0351667, 5.6],
    6: [-122.188, 46.2073333, 5.7], 7: [-122.182, 46.2026667, 5.0], 8: [-122.1825, 46.208, 5.0], 9:[-122.1973333, 46.2035, 5.2],
    10: [-122.1958333, 46.2098333, 5.1], 11: [-125.603, 42.752, 5.4], 12: [-126.103, 43.687, 5.2], 13: [-125.774, 44.98, 5.6]}
    '''
    
    datafile = open(filename, encoding = 'utf-8',)
    datadict = {}

    
    key = 0
    next(datafile)
    
    for aline in datafile:
        items = aline.split(',')
        
        key = key + 1
        lat = float(items[1])-30 #If map was to scale you wouldn't need to subtract 30, but i'm calibrating it so it works for our points
        lon = float(items[2])-10 #subtracting again to calibrate
        mag = float(items[4]) #add magnitude now or it will be hard to plot size of each earhquake
        datadict[key] = [lon, lat,mag]
        
    return datadict


def euclidD(point1, point2):
    '''(tuple, tuple) -> float

    given two points (can also just be two ints instead of two tuples), it finds the distance
    between the two points and returns that distance between them

    >>> euclidD((1,2),(2,4))
    2.23606797749979
    >>> euclidD((3,2),(2,4))
    2.23606797749979
    '''
    
    total = 0
    for index in range (len(point1)):
        diff = (point1[index]-point2[index]) ** 2  # part of the distance formula
        total = total +diff # adds the difference between the points up to put in distance equation

    euclidDistance = sqrt(total)

    return euclidDistance


def createCentroids(k, datadict):
    '''(int, dict) -> list

    input the amount of clusters you want to have and
    your earthquake data and this finds where all the centroids
    are for a particular cluster. Docstring examples will not be exact
    since we are using the random function.

    >createCentroids(1, readFile('equakes50f.txt')
    [[-122.1958333, 46.2098333, 5.1]]
    
    '''
    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rkey = random.randint(1,len(datadict))
        if rkey not in centroidKeys: #adds data points that are not in centroid keys already
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1

    return centroids



def createClusters(k, centroids, datadict, r):
    '''(int, list, dict, int) -> list

    given the amount of clusters you want, your centroids, equake data, and the number
    of repeats, this creates all the clusters for you data based on the amount of clusters
    and your centroids

    >>> createClusters(1, createCentroids(1, readFile('equakes50f.txt')) , readFile('equakes50f.txt'), 1)
    gives a list of the clusters. will be different every time because of random function
    '''
    for apass in range(r):
        print('****PASS', apass, '****')
        clusters = []
        for i in range(k):
            clusters.append([])

        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey], centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances) # finds smallest  distance from the cluster
            index = distances.index(mindist)

            clusters[index].append(akey)

        dimensions = len(datadict[1]) # finds the dimension of the cluster 
        for clusterIndex in range(k):
            sums = [0]*dimensions
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] = sums[ind] + datapoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind]/ clusterLen

            centroids[clusterIndex] = sums

       # for c in clusters:
            
            #print('CLUSTER')
            #for key in c:
                #print(datadict[key], end = ' ')
            #print()

        return clusters

def eqDraw(k, eqDic, eqClusters):
    '''(int, dict, list)-> None

    plots the individual points of the earthquakes on a world map and the
    bigger dots correspond to a larger magnitude

    >>> eqDraw(1, eqDict, eqClusters)
    draws points on the world map for each earthquake based of its magnitude
    '''
    
    
    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic('worldmap.gif')
    quakeWin.screensize(1200,715)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/ 90

    quakeT.hideturtle()
    quakeT.speed('fastest')
    quakeT.up()

    colorlist = ['red', 'green', 'blue', 'orange', 'cyan', 'yellow']
    
 
    
    for clusterIndex in range(k):
        quakeT.color(colorlist[clusterIndex])
        for akey in eqClusters[clusterIndex]:
            
            lon = eqDic[akey][0]
            lat = eqDic[akey][1]
            mag_size = eqDic[akey][2]  # the magnitude of each earthquake
            quakeT.goto(lon*wFactor, lat*hFactor)
            quakeT.dot(mag_size*2) #multiply by two so you cant tell the difference a little easier
    quakeWin.exitonclick()

    return None
    

    
def visualizeQuakes(k,r,dataFile):
    '''(int, int, str) -> None
    calls eqdraw to plot the earthquake data on a worldmap
    and takes in the parameters k, r, dataFile to help this plot.
    Returns None

    >>> visualizeQuakes(1, 3, 'equakes50f.txt')
    plots all the points on the world map for the given data

    '''
    
    datadict = readFile(dataFile)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)

    eqDraw(k, datadict, clusters)
    
    return None

def main():
    '''() -> None

    runs the visualizeQuakes function
    '''
    k= 6
    r = 2
    dataFile = 'earthquakes.csv'

    visualizeQuakes(k,r, dataFile)

main()



        
