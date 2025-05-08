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

def ExpCutPL(norm,alpha,array,beta,cut):
    #checking if the parameters have the right type
    if not isinstance(norm,(float,int)):
        raise TypeError(f"'norm' must be float or int, received {type(norm).__name__}.")
    if not isinstance(alpha,(float,int)):
        raise TypeError(f"'alpha' must be float or int, received {type(norm).__name__}.")
    if not isinstance(beta,(float,int)):
        raise TypeError(f"'beta' must be float or int, received {type(norm).__name__}.")
    if not isinstance(cut,(float,int)):
        raise TypeError(f"'cut' must be float or int, received {type(norm).__name__}.")
    if not isinstance(array,np.ndarray):
        raise TypeError(f"'array' must be np.ndarray, received {type(norm).__name__}.")
    #checking if energy values are correct
    if np.any(array <= 0):
        raise ValueError("All energy values must be positive")
    #calculating PowerLaw distribution
    dist = norm*array**(-alpha)*np.exp((-array/cut)**(beta))
    return dist
