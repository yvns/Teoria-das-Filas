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
import pandas as pd
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


   # In[23]:
   tamanho = 1000 #tamanho da tabela numero de linhas

   
   # In[2]:
   EntreChegadas = [G(c_alpha, c_beta) for i in range(tamanho)]
   # In[3]:
   Atendimentos  = [G(a_alpha, a_beta) for i in range(tamanho)]
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
    
   for i in range( 1, tamanho):
       IAtendimento.append(max(Chegadas[i], FAtendimento[i-1]))
       FAtendimento.append(IAtendimento[i]+Atendimentos[i])
       
    # ## Tamanho da Fila
    # In[6]:
   Ocorrencias = [[0 , 0]]
    
   for i in range(tamanho):
       Ocorrencias.append([Chegadas[i],  1])
       Ocorrencias.append([FAtendimento[i], -1])
   Ocorrencias = sorted(Ocorrencias)

   TamanhoFila = [[0], [0]] #TamanhoFila[0] = Instante de mudança | TamanhoFila[1] = Tamanho
   j=1
   for i in range(1, len(Ocorrencias)):
       TamanhoFila[0].append(Ocorrencias[i][0])
       TamanhoFila[1].append(TamanhoFila[1][j-1])
       j=j+1
       TamanhoFila[0].append(Ocorrencias[i][0])
       TamanhoFila[1].append(TamanhoFila[1][j-1]+Ocorrencias[i][1])
       j=j+1
    
   # In[20]
   Ocio = [Chegadas[0]]
   for i in range( 1, tamanho):
       Ocio.append(max(Chegadas[i]-FAtendimento[i-1], 0))

   Espera = []
   for i in range(tamanho):
       Espera.append(IAtendimento[i]-Chegadas[i])
    
    # # Graficos
   # In[7]:
   ''' 
   fig = plt.figure()
   grafico1 = fig.add_subplot(311)
   grafico2 = fig.add_subplot(312)
   grafico3 = fig.add_subplot(313)'''
   
   

   while(1):
       print("-----------Dados--------")
       switch = int(input("\t1 - Tamanho da fila\n\t2 - Dados Basicos\n\t3 - Ocio e Espera\n\t0 - Sair\n"))
       if(switch==1):
       # ## Fila
           plt.plot(TamanhoFila[0], TamanhoFila[1], "-bD")
           plt.title("Tamanho da Fila")
           plt.ylabel("Quantidade de pessoas")
           plt.xlabel("Tempo (min.)")
           plt.legend( ["Tamanho da Fila"], shadow=True)
           plt.grid(True)
           plt.show()
       if(switch==2):
           plt.title("Informações Basicas")
           plt.ylabel("Tempo (min.)")
           plt.xlabel("Cliente")
           plt.plot(EntreChegadas)
           plt.plot(Atendimentos)
           plt.legend( ["Chegadas a="+str(c_alpha)+" b="+str(c_beta),"Atendimentos a="+str(a_alpha)+" b="+str(a_beta)], shadow=True)    
           plt.grid(True)
           plt.show()
       if(switch==3):
           plt.title("Informações Complementares")
           plt.ylabel("Tempo (min.)")
           plt.xlabel("Ocio ou espera do cliente")
           plt.plot(Ocio, "--b")
           plt.plot(Espera, "-r")
           plt.legend( ["Ocio ","Espera"], shadow=True)   
           plt.grid(True)
           plt.show()
       if(switch==0):
           break
   

   # In[16]:
   op = bool(int(input("Deseja repetir? \n\t1 - Sim\n\t0 - Não\n")))
   if(op==False):
       exit()