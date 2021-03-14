import matplotlib.pyplot as plt
import numpy as np

def plotFunc():
    #Initialize the X-Axis and the range
    xpoints = np.array(range(0, 4))

    #Initialize the 3 Y-Axes
    fpoints = xpoints #Sets to X
    gpoints = xpoints**2 #Sets to X²
    hpoints = xpoints*xpoints*xpoints #Sets to x³

    #Intitalize the color and labels for each of the Y-Axes for the legend
    plt.plot(fpoints, 'b', label="f(x)=x")
    plt.plot(gpoints, 'c', label="g(x)=x²")
    plt.plot(hpoints, 'r', label="h(x)=x³")

    #Labels to show the X and Y-Axes
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')

    plt.legend() #Displays a representation of the Axes to make it tidy and neat
    plt.show()   #Display the graph

plotFunc()