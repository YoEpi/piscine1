import matplotlib.pyplot as plt
import numpy as np  # Import numpy for numerical calculations
import math

def plot_fct(func, x_min, x_max):
    x = np.linspace(0, 100, 1000)  # Generate 1000 points in the specified range
    y = [func(xi) for xi in x]  # Calculate the corresponding y-values

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of Function')
    plt.grid(True)
    plt.show()

def f ( x ) :
    return x **2 + x *3 + 2

plot_fct (lambda x : x , -10, 10)    #ctrl +/
plot_fct ( math . sin , 0 , 50)
plot_fct (f , -100 , 200)
plot_fct ( lambda x : x **2 , -10 , 10)
plot_fct ( lambda x : 1/ x , -100 , 100)