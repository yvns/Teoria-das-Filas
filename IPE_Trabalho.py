import sys
import matplotlib.pyplot as plt
import pandas as pd

sys.path.append('./Classes') #Deixando acessivel para import toda a pasta Classes

from ClassFilaGamma import Fila_G

while 1:
   
   print("------ Digite os coeficientes da fila------")
   print("Coeficientes da Chegada")
   c_alpha = float(input("\tAlpha: "))
   c_beta  = float(input("\tBeta (\"Tempo/Cliente\"): "))
   print("Coeficientes do Atendimento")
   a_alpha = float(input("\tAlpha: "))
   a_beta  = float(input("\tBeta (\"Tempo/Cliente\"): "))
   tamanho = abs(int(input("Numero de Xi: "))) #tamanho da tabela numero de linhas
   
   Fila = Fila_G(c_alpha, c_beta, a_alpha, a_beta, tamanho)
   Fila.gerarFila()
    # # Graficos
   # In [7]:
   while(1):
       print("-----------Dados--------")
       switch = int(input("\t1 - Tamanho da fila\n\t2 - Dados Basicos\n\t3 - Ocio/Espera e Tempo no Sistema \n\t4 - Gerar xls\n\t0 - Sair dos Dados\n"))
       if(switch==1):
       # ## Fila
           plt.plot(Fila.tamanhoFila[0], Fila.tamanhoFila[1], "-bD")
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
           plt.plot(Fila.entreChegadas)
           plt.plot(Fila.atendimentos)
           plt.legend( ["Chegadas a="+str(c_alpha)+" b="+str(c_beta),"Atendimentos a="+str(a_alpha)+" b="+str(a_beta)], shadow=True)    
           plt.grid(True)
           plt.show()
           
       if(switch==3):
           plt.title("Ocio/Espera e Tempo no Sistema")
           plt.ylabel("Tempo (min.)")
           plt.xlabel("Xi")
           plt.plot(Fila.ocio, "--b")
           plt.plot(Fila.espera, "-r")
           plt.plot(Fila.tempoNoSistema, "-k")
           plt.legend( ["Ocio ","Espera", "Tempo no Sistema"], shadow=True) 
           plt.grid(True)
           plt.show()
           
       if(switch==4):
           DataFrame = pd.DataFrame(columns=["Entre Chegadas", "Atendimento", "Chegada", "Inicio Atendimento", "Fim Atendimento", "Espera", "Ocio"])
           DataFrame["Entre Chegadas"]=Fila.entreChegadas
           DataFrame["Atendimento"]=Fila.atendimentos
           DataFrame["Chegada"]=Fila.chegadas
           DataFrame["Inicio Atendimento"]=Fila.inicioAtendimento
           DataFrame["Fim Atendimento"]=Fila.fimAtendimento
           DataFrame["Espera"]=Fila.espera
           DataFrame["Ocio"]=Fila.ocio
           DataFrame["Tempo no Sistema"]=Fila.tempoNoSistema
           DataFrame.to_excel("Fila_CH_a_"+str(c_alpha)+"_b_"+str(c_beta)+"_AT_a"+str(a_alpha)+"_b_"+str(a_beta)+".xlsx",sheet_name="Fila",index_label="Xi")
           
       if(switch==0):
           break
   
   # In [16]:
   op = bool(int(input("Deseja repetir? \n\t1 - Sim\n\t0 - Não\n")))
   if(op==False):
       exit()