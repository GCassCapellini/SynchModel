from integrate import integral
import numpy as np
from matplotlib import pyplot as plt
import astropy.units as u

def SynchEm(part_dist,E,Egam,B):
    #definindo constantes em cgs
    e = 4.8032e-10 * u.Unit('statcoul') #carga do elétron
    me = 9.1094e-28 * u.Unit('g') #massa do elétron
    h = 6.6261e-27  * u.Unit('erg')*u.Unit('s') #constante de planck
    c = 2.9979e10 * u.Unit('cm')/u.Unit('s') #velocidade de luz
    #cálculo do termo fora da integral
    factor1 = 3.7/3**(1/6)
    factor2 = e**(8/3)*B**(2/3)/(h**(4/3)*c**(1/6))
    #cálculando energia crítica:
    factor_c1 = 3/(4*np.pi)
    factor_c2 = e*h/(me**3*c**5)
    factor_c3 = np.sqrt(2/3)*B*E**2
    Ec = factor_c1*factor_c2*factor_c3
    #calculando a integral
    #definindo limites da integral
    Emin, Emax = E[0], E[len(E)-1]
    #definindo função que será integrada
    term_exp = np.exp(-Egam/Ec)
    term_div = (Egam/E**2)**(1/3)
    fnctn = part_dist*term_div*term_exp
    #fazendo a integração
    Integral_sync,erro_sync = integral(Emin,Emax,fnctn)
    return Integral_sync
