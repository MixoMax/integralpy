import math
import string
import matplotlib.pyplot as plt

function = str(input("Funktion: "))
stepsize = int(input("Schritgröße (Schritte pro Einheit): "))
minx = float(eval(input("von: ")))
maxx = float(eval(input("bis: ")))

def getY(xcoord, function):
    x = str(xcoord)
    function = function.replace("x", str(float(x)))
    y = eval(function)
    return y

def calcSize(x1,y1,x2,y2):
    size = (x1-x2)*(y1-y2)
    return size

def plot(xArray, yArray):
    fig = plt.figure()
    ax = plt.axes()
    ax.plot(xArray, yArray, color="b")
    mult = int(stepsize*abs(minx-maxx)/100)
    for i in range(int(len(xArray)/mult)):
        i = i * mult
        ax.plot([xArray[i],xArray[i]], [0, yArray[i]], color="r")
        if(i+1 < len(xArray)):
            ax.plot([xArray[i+1],xArray[i]], [yArray[i], yArray[i]], color="r")
    plt.show()

yArray = []
xArray = []
for xcoord in range(int(stepsize*(abs(minx-maxx))+1)):
    xcoord = xcoord + (minx*stepsize)
    xcoord = float(xcoord / stepsize)
    yArray.append(getY(xcoord, function))
    xArray.append(xcoord)

QuadTotal = []
TriangleTotal = []
for i in range(len(xArray)-1):
    QuadTotal.append(calcSize(xArray[i], 0, xArray[i+1], yArray[i+1]))
    TriangleTotal.append((calcSize(xArray[i], yArray[i], xArray[i+1], yArray[i+1]))/2)

print(sum(TriangleTotal)+ sum(QuadTotal))
plot(xArray, yArray)