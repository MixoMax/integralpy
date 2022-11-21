import math
import string
import matplotlib.pyplot as plt

#To Do
#Funktionen nur in intervallen hinzufügen: Syntax: "x**2,i0-20;x**3,i20-25"
#

function = str(input("Funktion: "))
stepsize = int(input("Schritgröße (Schritte pro Einheit): "))
minx = float(eval(input("von: ")))
maxx = float(eval(input("bis: ")))

def splitFunction(function):

    functionArray = []
    if(function.count("i") == 0):
        return function
    else:
        for l in range(function.count(";")):
            index = function.find("i")
            
            funcxy = [function[int(0):int(index-1)], function[int(index+1):int(function.find("-")), int(function.find("-")+1):int(function.find(";")-1)]]
            if len(function) > index:
                function = function[int(0) : int(index) : ] + function[int(index + 1) : :]
                function = function[int(function.find("-")) : ] + function[int(function.find("-")+1) : :]
                function = function[int(0) : int(function.find(";")) : ] + function[int(function.find(";")+1) : :]
            functionArray.append(funcxy)
        
        return functionArray

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
    
def calcXY(stepsize, functionArray):
    yArray = []
    xArray = []
    if(type(functionArray is int)):
        print(functionArray)
        for xcoord in range(len(functionArray)*stepsize+1):
            xcoord = (xcoord/stepsize)
            yArray.append(getY(xcoord, function = functionArray))
            xArray.append(xcoord)
        return xArray, yArray
    
    else:        
        for i in len(functionArray):
            j = abs(functionArray[i][1]-functionArray[i][2])
            for xcoord in range(j*stepsize):
                xcoord = (xcoord/stepsize) + functionArray[i][1]
                yArray.append(getY(xcoord, function=functionArray[i][0]))
                xArray.append(xcoord)
        return xArray, yArray
            

def calcArea(xArray, yArray):
    QuadTotal = []
    TriangleTotal = []
    for i in range(len(xArray)-1):
        QuadTotal.append(calcSize(xArray[i], 0, xArray[i+1], yArray[i+1]))
        TriangleTotal.append((calcSize(xArray[i], yArray[i], xArray[i+1], yArray[i+1]))/2)
    return sum(TriangleTotal) + sum(QuadTotal)

functionArray = splitFunction(function)
xArray, yArray = calcXY(stepsize, functionArray)
print(calcArea(xArray, yArray))
plot(xArray, yArray)
#