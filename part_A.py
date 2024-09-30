"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
x = [1, 2, 3, 4, 5]
def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    total = 0                           
    count = 0
    for num in x:                    # loop calculates the mean value
        count += 1
        total += num
    average = total / count
    
    squared_values = []              
    total = 0
    count = 0
    for i in x:                     # loop calculates the mean of the variables squared
        num = i**2
        squared_values.append(num)
        count += 1
        total += num
    average2 = total / count
    dev = (average2 - (average**2)) ** 0.5    #calculate the standard deviation
    return dev
std_loops(x)

x = [1, 2, 3, 4, 5]
def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    meanx = (1/len(x)) * (sum(x))                      # Calculate the mean of the variables
    dev = (sum([(num - meanx) ** 2 for num in x]) / len(x)) ** 0.5     # Calculate the standard deviation
    return dev
std_builtin(x)
    


# The final solution uses a premade Numpy function for standard deviation
    
import numpy as np
x = [1, 2, 3, 4, 5]
std_dev = np.std(x)
print(std_dev)