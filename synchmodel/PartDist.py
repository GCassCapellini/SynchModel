import numpy as np

##-------- Funções para visualização do modelo de distribuição ------------##
def DistPL_plot(norm,alpha,array):
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


def ExpCutPL_plot(norm,alpha,array,beta,cut):
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

##-------- Funções para cálculo do modelo de distribuição e integração ------------##

def PowerLaw(norm, alpha):

    """
    Creates a particle distribution function following a power-law.

    Parameters:
        norm (float): Normalization constant of the distribution.
        alpha (float): Spectral index of the power law.

    Returns:
        function (callable): A function that computes the particle distribution for a given energy E.
    """
    #creating a function factory:
    def distribution(E):
        #calculating the distribution of particles according to a power law
        if E <= 0:
            raise ValueError("E must be positive.")
        return norm * E**(-alpha)
    return distribution

def ExpCutOffPL(norm, alpha, beta, cut):
    """
    Creates a particle distribution function following an exponential cutoff power-law.

    Parameters:
        norm (float): Normalization constant of the distribution.
        alpha (float): Spectral index of the power law.
        beta (float): Exponential cutoff index.
        cut (float): Cutoff energy scale.

    Returns:
        function (callable): A function that computes the particle distribution for a given energy E.
    """
    #creating a function factory:
    def distribution(E):
        #calculating the distribution of particle according to a exponencial cut off power law
        if E <= 0:
            raise ValueError("E must be positive.")
        return norm * E**(-alpha) * np.exp(-(E / cut)**beta)
    return distribution
