# SynchModel
Este código calcula a emissão sincrotron produzida tendo como base o artigo  	High Energy Astrophysical Phenomena (https://arxiv.org/abs/1202.5949v1).
A expressão final para o espectro é obtida através das aproximações realizadas no artigo, em especial:

1 - A função de Bessel é aproximada

2 - É assumido que o campo magnético perpendicular é o mesmo em todo o espaço

Os parâmetros do código são: B, N(E), E_gamma, E_c, Emin, Emax

As constantes são: e,h,c,m 

O código é separado em duas partes:

1 - Distribuição de partículas N(E): nesta seção são definidas funções que determinam a função de distribuição das partículas 

2 - Espectro síncrotron: nesta seção calcula-se a emissão síncrotron dada a função de distribuição definida na seção 1.


## Informações sobre rotinas importadas e funções:

O código utiliza as rotinas matplotlib, numpy, astropy, math e scipy.

O código apresenta as funções: grid, PartDist_PL, sync, integral. Para mais detalhes sobre cada função veja as suas respectivas seções:

### grid(min,max,itrcn):
  Essa função estabelece uma rede 1D de parâmetros baseado nas especificações dadas.
  
  Parâmetros:
  
    min [float]: mínimo da rede desejado. Deve ser maior que zero e menor que max
    
    max [float]: máximo da rede desejado. Deve ser maior que zero e que min
    
    itrcn [int]: número de espaços da rede-1. Corresponde ao número de interações para formar a rede

  Retorna:

    array[numpy.ndarray]: array desejado com unidade igual àquelas definidas em min e max.

## Distribuição de Partículas

### PowerLaw(norm,alpha,array):
  Essa função calcula a distribuição de partículas considerando uma lei de potência

  $N(E) = N_0 \times E^{-\alpha}$

  Parâmetros:

    norm [(float,int)]: parâmetro de normalização

    alpha [(float,int)]: índice espectral da lei de potência

    array [numpy.ndarray]: array com os valores da variável da função

  Retorna:

    N(E) [numpy.ndarray]: array com o resultado da distribuição de partículas

### ExpCutOffPL(norm,alpha,beta,cut):
  Essa função calcula a distribuição de partículas considerando uma lei de potência com um cut off exponencial
 
  $N(E) = N_0 \times E^{-\alpha} \times exp(-(E/cut)^\beta)$

  Parâmetros:

    norm [(float,int)]: parâmetro de normalização

    alpha [(float,int)]: índice espectral da lei de potência

    beta [(float,int)]: índice do cut off exponencial

    cut [float]: valor de corte da exponencial

  Retorna:

    N(E) [numpy.ndarray]: array com o resultado da distribuição de partículas

### DistPL_plot(norm,alpha,array):
Função para visualização do modelo de distribuição

### ExpCutPL_plot(norm,alpha,array,beta,cut):
Função para visualização do modelo de distribuição


### sync
  Essa função calcula a emissão síncrotron dada uma distribuição de partículas, um array de energia dos elétrons e dos fótons e um campo magnético 

  Parâmetros:

    part_dist[function]: função da distribuição de partículas

    E [np.ndarray]: array com os valores da energia dos elétrons

    Egam [np.ndarray]: array com os valores da energia dos fótons

    B [float]: valor do campo magnético

  Retorna:

    L [np.ndarray]: array da luminosidade síncrotron produzida

    

### integral(lim_inf,lim_sup,function,**kwargs):
  Essa função calcula a integral de uma função utilizando a rotina quad do pacote scipy

  Parâmetros:

    lim_inf [(float,int)]: limite inferior da integral

    lim_sup [(float,int)]: limite superior da integral

    Vale notar que se lim_inf>lim_sup a rotina inverte o sinal da integral automaticamente

    function[callable]: função que deseja interal

    **kwargs: argumentos extras
  
  Retorna:

    resultado, erro [float],[float]: resultado da integral calculada e o seu respectivo erro
