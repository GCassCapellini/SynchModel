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

Em ambos os casos é retornado um array 

## Informações sobre rotinas importadas e funções:

O código utiliza as rotinas matplotlib, numpy, astropy, math e scipy.

O código apresenta as funções: grid, PartDist_PL, sync, integrate. Para mais detalhes sobre cada função veja as suas respectivas seções:

### grid

### PartDist_PL

### sync

### integrate
