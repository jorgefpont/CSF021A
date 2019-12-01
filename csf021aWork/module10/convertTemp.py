"""
Module ConvertTemp is the MODEL for a temperature conversion program.
Note that the Model never contains a reference to the View.
It contains 2 functions that convert C to F and vice-versa
"""

def toF(t):
    return ( (9.0/5.0) * t + 32.0 )

def toC(t):
    return ( (5.0/9.0) * (t - 32.0) )