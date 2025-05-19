def SynchEm(part_dist,E,Egam,B):
    """
    Essa função calcula a emissão síncrotron dada uma distribuição de partículas, um array de energia dos elétrons e dos fótons e um campo magnético

    Parâmetros:

    part_dist[function]: função da distribuição de partículas

    E [np.ndarray]: array com os valores da energia dos elétrons

    Egam [np.ndarray]: array com os valores da energia dos fótons

    B [float]: valor do campo magnético

    Return:

    L [np.ndarray]: array da luminosidade síncrotron produzida

    """

    #checando se entradas estão corretas:

    if not callable (part_dist,function):
        raise TypeError (f"part_dist deve ser uma função, mas recebeu {type(part_dist).__name__}")
    if not isinstance (E,np.ndarray):
        raise TypeError (f"E deve ser um numpy.ndarray, mas recebeu {type(part_dist).__name__}")
    if not isinstance (Egam,np.ndarray):
        raise TypeError (f"Egam deve ser um numpy.ndarray, mas recebeu {type(part_dist).__name__}")
    if not isinstance (B,(int,float)):
        raise TypeError (f"E deve ser um int ou float, mas recebeu {type(part_dist).__name__}")

    #definindo constantes em cgs
    e = 4.8032e-10  #carga do elétron
    me = 9.1094e-28 #massa do elétron
    h = 6.6261e-27  #constante de planck
    c = 2.9979e10  #velocidade de luz

    #cálculo do termo fora da integral
    factor1 = 1.85*np.sqrt(2)*e**3*B
    factor2 = h*me*c**2
    
    #calculando a integral
    #definindo limites da integral
    Emin, Emax = E[0], E[-1]
    #definindo função que será integrada
    Lgam = np.zeros_like(Egam)
    for i in range(len(Egam)):
        def integ(epsilon):
            #cálculando energia crítica
            Ec = (3 * e * h * np.sqrt(2/3) * B * epsilon**2) / (4 * np.pi * me**3 * c**5)
            return part_dist(epsilon)*(Egam[i]/Ec)**(1/3)*np.exp(-Egam[i]/Ec)    
        Integral_val,error = integral(Emin,Emax,integ)
        Lgam[i] = factor1/factor2*Integral_val
    return Lgam
