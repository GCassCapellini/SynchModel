from integrate import integral
import numpy as np

def SynchEm(part_dist,E,Egam,B):
    #definindo constantes em cgs
    e = 4.8032e-10  #carga do elétron
    me = 9.1094e-28 #massa do elétron
    h = 6.6261e-27  #constante de planck
    c = 2.9979e10  #velocidade de luz
    #cálculo do termo fora da integral
    factor1 = 3.7/3**(1/6)
    factor2 = e**(8/3)*B**(2/3)/(h**(4/3)*c**(1/6))
    #calculando a integral
    #definindo limites da integral
    Emin, Emax = E[0], E[-1]
    #definindo função que será integrada
    Lgam = np.zeros_like(Egam)
    for i in range(len(Egam)):
        factor_c1 = 3/(4*np.pi)
        factor_c2 = e*h/(me**3*c**5)
        def integ(E):
            #cálculando energia crítica:
            factor_c3 = np.sqrt(2/3)*B*E**2
            Ec = factor_c1*factor_c2*factor_c3
            return part_dist(E)*(Egam[i]/E**2)**(1/3)*np.exp(-Egam[i]/Ec)
        Integral_val,error = integral(Emin,Emax,integ)
        Lgam[i] = factor1*factor2*Integral_val
    return Lgam
