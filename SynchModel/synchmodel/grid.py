import math
import numpy as np

#Este código define uma função que estabelece uma rede de variáveis.
#Os parâmetros são: min (float), max (float), itrcn (int)

def grid(Min,Max,itrcn):
    """
    Creates a grid o parameters as a numpy.ndarray

    Parameters:

    Min (float): Minimum of the grid
    Max (float): Maximum of the grid
    itrcn (float): Number of spaces in the grid

    Returns:

    array (numpy.ndarray): Grid of values from Min to Max
    """
    Min = Min #defined minimum if the grid
    Max = Max #defined maximum of the grid
    itrcn = itrcn #defined number of interaction  
    if Max>Min and Min>0: #debug line
        if type(Min) is float and type(Max) is float and type(itrcn) is int: #debug line
            #Grid creation routine
            array = np.zeros(itrcn+1) #defined array that will be returned
            itv = (math.log10(Max)-math.log10(Min))/itrcn #interval dx of the grid
            for i in range(itrcn+1): #loop to calculate array
                array[i] = 10**(math.log10(Min)+i*itv) #calculating array
            return array

        #error messages    
        else: 
            return 'Error message: one of the parameters in grid does not have the necessary type: Check grid([float],[float],[int])'
    
    else:
       return "Error message: the defined max is smaller than min or one of them are negative"        