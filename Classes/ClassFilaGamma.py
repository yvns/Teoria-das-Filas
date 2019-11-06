from random import gammavariate as G

''' Autor: Dario
    Esta classe simula apenas filas com comportamento gamma
'''
class Fila_G:
    def __init__(self, alpha_chegada, beta_chegada, alpha_atendimento, beta_atendimento, tamanho):
        self.alphaChegada = alpha_chegada
        self.betaChegada  = beta_chegada
        self.alphaAtendimento = alpha_atendimento
        self.betaAtendimento  = beta_atendimento
        self.tamanho = tamanho
        
    # Gera uma nova simulação para a mesma fila
    def gerarFila(self):
        # ### Dados Basicos
        self.entreChegadas = [G(self.alphaChegada, self.betaChegada) for i in range(self.tamanho)]
        self.atendimentos  = [G(self.alphaAtendimento, self.betaAtendimento) for i in range(self.tamanho)]
        
        # #### Dados secundarios
        # In [4]:    
        self.chegadas = []
        soma=0
        for xi in self.entreChegadas: 
            soma +=xi
            self.chegadas.append(soma) 
         # In [5]:    
        self.inicioAtendimento = [] #Inicio do Atendimento
        self.fimAtendimento = [] #Fim do Atendimento
        
        self.inicioAtendimento.append(self.chegadas[0])
        self.fimAtendimento.append(self.inicioAtendimento[0]+self.atendimentos[0])
         
        for i in range( 1, self.tamanho):
            self.inicioAtendimento.append(max(self.chegadas[i], self.fimAtendimento[i-1]))
            self.fimAtendimento.append(self.inicioAtendimento[i] + self.atendimentos[i])
           
         # ## Tamanho da Fila
         # In [6]:
        Ocorrencias = [[0 , 0]]
         
        for i in range(self.tamanho):
            Ocorrencias.append([self.chegadas[i],  1])
            Ocorrencias.append([self.fimAtendimento[i], -1])
        Ocorrencias = sorted(Ocorrencias)
    
        self.tamanhoFila = [[0], [0]] #TamanhoFila[0] = Instante de mudança | TamanhoFila[1] = Tamanho
        j=1
        for i in range(1, len(Ocorrencias)):
            self.tamanhoFila[0].append(Ocorrencias[i][0])
            self.tamanhoFila[1].append(self.tamanhoFila[1][j-1])
            j=j+1
            self.tamanhoFila[0].append(Ocorrencias[i][0])
            self.tamanhoFila[1].append(self.tamanhoFila[1][j-1]+Ocorrencias[i][1])
            j=j+1
        
        # In [20]
        self.ocio = [self.chegadas[0]]
        for i in range( 1, self.tamanho):
            self.ocio.append(max(self.chegadas[i]-self.fimAtendimento[i-1], 0))
    
        self.espera = []
        for i in range(self.tamanho):
            self.espera.append(self.inicioAtendimento[i]-self.chegadas[i])  
        self.tempoNoSistema = [self.atendimentos[i]+self.espera[i] for i in range(self.tamanho)]