#!/usr/bin/env python
# coding: utf-8

# Espaço para as:
# - Configurações de pagina
# - Imports
# - Funções
# - Classes

# In[1]:
## Coisa do Jupyter não apagar!:
'''from IPython.core.display import display, HTML
display(HTML("<style>.container { width:95% !important;}</style>"))
%config InlineBackend.figure_format='retina' '''

import matplotlib.pyplot as plt
from random import gammavariate as G


# ### Dados Basicos
while 1:
   print("--- Digite os coeficientes da fila")
   
   print("Coeficientes da Chegada")
   c_alpha = float(input("\tAlpha:"))
   c_beta  = float(input("\tBeta:"))
   
   print("Coeficientes do Atendimento")
   a_alpha = float(input("\tAlpha:"))
   a_beta  = float(input("\tBeta:"))

    # In[2]:
   EntreChegadas = [G(c_alpha, c_beta) for i in range(1000)]
   # In[3]:
   Atendimentos  = [G(a_alpha, a_beta) for i in range(1000)]
   # #### Dados secundarios
    
   # In[4]:    
   Chegadas = []
   soma=0
   for xi in EntreChegadas: 
       soma +=xi
       Chegadas.append(soma)        
    # In[5]:    
   IAtendimento = [] #Inicio do Atendimento
   FAtendimento = [] #Fim do Atendimento
    
   IAtendimento.append(Chegadas[0])
   FAtendimento.append(IAtendimento[0]+Atendimentos[0])
    
   for i in range( 1, 1000):
       IAtendimento.append(max(Chegadas[i], FAtendimento[i-1]))
       FAtendimento.append(IAtendimento[i]+Atendimentos[i])    
       
    # ## Tamanho da Fila    
    # In[6]:
   Ocorrencias = [[0 , 0]]
    
   for i in range(1000):
       Ocorrencias.append([Chegadas[i],  1])
       Ocorrencias.append([FAtendimento[i], -1])
   Ocorrencias = sorted(Ocorrencias)
    
   TamanhoFila = [[0], [0]]
   j=1
   for i in range(1, len(Ocorrencias)):
       TamanhoFila[0].append(Ocorrencias[i][0])
       TamanhoFila[1].append(TamanhoFila[1][j-1])
       j=j+1
       TamanhoFila[0].append(Ocorrencias[i][0])
       TamanhoFila[1].append(TamanhoFila[1][j-1]+Ocorrencias[i][1])
       j=j+1
    
   # In[7]:
   fig = plt.figure()
   grafico1 = fig.add_subplot(211)
   grafico2 = fig.add_subplot(212)
   
   grafico1.set_title("Informações Basicas")
   grafico1.set_ylabel("Tempo (min.)")
   grafico1.set_xlabel("Cliente")
   grafico1.plot(EntreChegadas)
   grafico1.plot(Atendimentos)
   
   grafico1.legend( ["Chegadas","Atendimentos"], shadow=True)    
   grafico1.grid(True)

    # ## Fila
    
   inic=0
   fim =4001 # Quantidade de ocorrencias = fim-inic
   
   grafico2.plot(TamanhoFila[0][inic:fim], TamanhoFila[1][inic:fim], "-bD")
   grafico2.set_title("Tamanho da Fila")
   grafico2.set_ylabel("Quantidade de pessoas")
   grafico2.set_xlabel("Tempo (min.)")
   grafico2.legend( ["Tamanho da Fila"], shadow=True)
   grafico2.grid(True)
   plt.show()
   # In[16]:
   op = bool(int(input("Deseja repetir? \n\t1 - Sim\n\t0 - Não\n")))
   if(op==False):
       exit()