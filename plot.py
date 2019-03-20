# Zoe Cahill - Contains a method which will plot a function
# References https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

def plotfunction():
    # Imports matplotlib which will be needed to plot the function
    import matplotlib.pyplot as plt
    # Creating 3 lists to store the variables of x, x**2 and 2**x
    x = []
    xsquared = []
    twopowerofx = []

    # This loop will go through numbers 0 - 4 and generate the lists of numbers we will
    # require to graph the functions
    for i in range (0, 5):
        
        # Adding results to the lists
        x.append (i)
        xsquared.append (i**2)
        twopowerofx.append (2**i)


        # Originally had this code within the for loop but it would not graph
        # correctly hence why I generated the lists separately from plotting them
        #plt.plot([x], [x], 'ro')
        #plt.plot([x], [x**2], 'bo')
        #plt.plot([x], [2**x], 'yo')
        
        # Increments the counter
        i=+1

    # Here we call the plot function to plot the various lists of functions generated above
    plt.plot(x, x, 'ro-', label = 'x')
    plt.plot(x, xsquared, 'bo-', label = 'x**2')
    plt.plot(x, twopowerofx, 'yo-', label = '2**x')

    # This generates the legend key for each labeled line as above
    plt.legend(loc='upper left')

    # Names the x axis
    plt.xlabel('x - axis') 
    # Names the y-axis 
    plt.ylabel('y - axis') 

    # Gives a title to the graph
    plt.title('Functions of x, x**2 and 2**x in range [0,4]') 

    # Calls the method to generate graphic
    plt.show()

plotfunction()