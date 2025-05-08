import numpy as np
def DistPL(norm,alpha,array):
    #This function calculates the particle distribution according to a PowerLaw
    #checking if parameters have the right types
    if not isinstance(norm,(float,int)):
        raise TypeError(f"'norm' must be float or int, received {type(norm).__name__}.")
    if not isinstance(alpha,(float,int)):
        raise TypeError(f"'alpha' must be float ou int, received {type(norm).__name__}.")
    if not isinstance(array,np.ndarray):
        raise TypeError(f"'array' must be np.ndarray, received {type(norm).__name__}.")
    #checking if energy values are correct
    if np.any(array <= 0):
        raise ValueError("All energy values must be positive")
    #calculating PowerLaw distribution
    dist = norm*array**(-alpha)
    return dist