from scipy.integrate import quad

#Esta função calcula uma integral de uma função dado um limite inferior e superior 
def integral(lim_inf,lim_sup,function,**kwargs):
    """
    Integrates a generic function using scipy (quad method)

    Parameters:

    lim_inf (float): Integral inferior limit
    lim_sup (float): Integral superior limit
    function (callable): Generic function that will integrated

    Return: 

    resultado (float): Result of the integral
    """
   #checando se as variáveis possuem o tipo correto
    if not isinstance(lim_inf, (float, int)):
        raise TypeError(f"lim_inf deve ser float ou int, mas recebeu {type(lim_inf).__name__}")
    
    if not isinstance(lim_sup, (float, int)):
        raise TypeError(f"lim_sup deve ser float ou int, mas recebeu {type(lim_sup).__name__}")
    
    if not callable(function):
        raise TypeError("function deve ser uma função ou objeto chamável (callable).")
    #checando o valor de lim_inf e lim_sup
    invertido = False
    if lim_inf > lim_sup:
        lim_inf, lim_sup = lim_sup, lim_inf
        invertido = True
    resultado, erro = quad(function, lim_inf, lim_sup,**kwargs)

    if invertido:
        resultado *= -1

    return resultado, erro
