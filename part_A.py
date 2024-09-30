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
    for num in x:
        count += 1
        total += num
    average = total / count
    
    squared_values = []
    total = 0
    count = 0
    for i in x:
        num = i**2
        squared_values.append(num)
        count += 1
        total += num
    average2 = total / count
    dev = (average2 - (average**2)) ** 0.5
    return dev
std_loops(x)


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
    
    meanx = (1/len(x)) * (sum(x))
    means = sum([(num - meanx) ** 2 for num in x])
    dev = (means / len(x)) ** 0.5
    return dev
std_builtin(x)
    




    
import numpy as np
x = [1, 2, 3, 4, 5]
std_dev = np.std(x)
print(std_dev)