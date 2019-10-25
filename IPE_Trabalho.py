import matplotlib.pyplot as plt
import pandas as pd
from random import gammavariate as G
# ### Dados Basicos
while 1:

   print("------ Digite os coeficientes da fila------")
   print("Coeficientes da Chegada")
   c_alpha = float(input("\tAlpha: "))
   c_beta  = float(input("\tBeta: "))
   print("Coeficientes do Atendimento")
   a_alpha = float(input("\tAlpha: "))
   a_beta  = float(input("\tBeta: "))
   
   tamanho = abs(int(input("Numero de Xi: "))) #tamanho da tabela numero de linhas
   
   
   EntreChegadas = [G(c_alpha, c_beta) for i in range(tamanho)]
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
       
   TempoNoSistema = [Atendimentos[i]+Espera[i] for i in range(tamanho)]
    
    # # Graficos
   # In[7]:
   while(1):
       print("-----------Dados--------")
       switch = int(input("\t1 - Tamanho da fila\n\t2 - Dados Basicos\n\t3 - Ocio/Espera e Tempo no Sistema \n\t4 - Gerar xls\n\t0 - Sair dos Dados\n"))
       if(switch==1):
       # ## Fila
           plt.plot(TamanhoFila[0], TamanhoFila[1], "-bD")
           plt.title("Tamanho da Fila")
           plt.ylabel("Quantidade")
           plt.xlabel("Tempo (min.)")
           plt.legend( ["Tamanho da Fila"], shadow=True)
           plt.grid(True)
           plt.show()
       if(switch==2):
           plt.title("Informações Basicas")
           plt.ylabel("Tempo (min.)")
           plt.xlabel("Xi")
           plt.plot(EntreChegadas)
           plt.plot(Atendimentos)
           plt.legend( ["Chegadas a="+str(c_alpha)+" b="+str(c_beta),"Atendimentos a="+str(a_alpha)+" b="+str(a_beta)], shadow=True)    
           plt.grid(True)
           plt.show()
           
       if(switch==3):
           plt.title("Ocio/Espera e Tempo no Sistema")
           plt.ylabel("Tempo (min.)")
           plt.xlabel("Xi")
           plt.plot(Ocio, "--b")
           plt.plot(Espera, "-r")
           plt.plot(TempoNoSistema, "-k")
           plt.legend( ["Ocio ","Espera", "Tempo no Sistema"], shadow=True) 
           plt.grid(True)
           plt.show()
           
       if(switch==4):
           DataFrame = pd.DataFrame(columns=["Entre Chegadas", "Atendimento", "Chegada", "Inicio Atendimento", "Fim Atendimento", "Espera", "Ocio"])
           DataFrame["Entre Chegadas"]=EntreChegadas
           DataFrame["Atendimento"]=Atendimentos
           DataFrame["Chegada"]=Chegadas
           DataFrame["Inicio Atendimento"]=IAtendimento
           DataFrame["Fim Atendimento"]=FAtendimento
           DataFrame["Espera"]=Espera
           DataFrame["Ocio"]=Ocio
           DataFrame["Tempo no Sistema"]=TempoNoSistema
           DataFrame.to_excel("Fila_CH_a_"+str(c_alpha)+"_b_"+str(c_beta)+"_AT_a"+str(a_alpha)+"_b_"+str(a_beta)+".xlsx",sheet_name="Fila",index_label="Xi")
           
       if(switch==0):
           break
   

   # In[16]:
   op = bool(int(input("Deseja repetir? \n\t1 - Sim\n\t0 - Não\n")))
   if(op==False):
       exit()