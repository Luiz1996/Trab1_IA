import random

class EstadoTabuleiro:
    nRainhas = 0
    energia = 0
    tabuleiro = []

    def getTabuleiro(self):
        return self.tabuleiro

    def getEnergia(self):
        return self.energia 
        
    def setTabuleiro(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def setEnergia(self, energia):
        self.energia = energia

    def __init__(self, qtdeRainhas):
        self.nRainhas = qtdeRainhas

        self.tabuleiro = []
    
        for linha in range(self.nRainhas):
            linhas = []
            for coluna in range(self.nRainhas):
                if linha == coluna:
                    linhas.append(True)
                else:
                    linhas.append(False)
            self.tabuleiro.append(linhas)
        
        for linha in range(self.nRainhas):
            self.trocaPosicaoLinhas(linha, random.randint(0,  (self.nRainhas-1)))
        
        self.atualizarEnergia()

    def trocaPosicaoLinhas(self, n1, n2):
            linha = self.tabuleiro[n1]
            self.tabuleiro[n1] = self.tabuleiro[n2]
            self.tabuleiro[n2] = linha
            
    def atualizarEnergia(self):
        energiaParcial = 0 
        for linha in range(self.nRainhas):
            for coluna in range(self.nRainhas):
                if self.tabuleiro[linha][coluna]:
                    energiaParcial += self.validarColisao(linha, coluna)
        self.energia = (energiaParcial/2)


    def validarColisao(self, linhaRainhaOrigem, colunaRainhaOrigem):
        qtdeConflitos = 0 

        for linhaRainhaAtual in range(self.nRainhas):
            for colunaRainhaAtual in range(self.nRainhas):
                
                temRainha = self.tabuleiro[linhaRainhaAtual][colunaRainhaAtual]
                
                naoEhRainhaOrigem = (linhaRainhaAtual  != linhaRainhaOrigem and colunaRainhaAtual != colunaRainhaOrigem)
						                     
                estaNaDiagonalLinhaColunaRainhaOrigem = (linhaRainhaAtual + colunaRainhaAtual == linhaRainhaOrigem + colunaRainhaOrigem or linhaRainhaAtual - colunaRainhaAtual == linhaRainhaOrigem - colunaRainhaOrigem)

                if temRainha and estaNaDiagonalLinhaColunaRainhaOrigem and naoEhRainhaOrigem:
                    qtdeConflitos += 1
        
        return qtdeConflitos

    def gerarNovoEstado(self):
        novoEstado = EstadoTabuleiro(self.nRainhas)
        novoEstado.setTabuleiro(self.tabuleiro)
        novoEstado.trocaPosicaoLinhas(random.randint(0,  self.nRainhas-1), random.randint(0,  self.nRainhas-1))
        novoEstado.atualizarEnergia()

        return novoEstado

    def imprimirTabuleiro(self):
        print("\n\n--------------------------------------------------------------------------------------------------------------------\n\n")
        print("Impressao do resultado:")
        for linha in range(self.nRainhas):
            for coluna in range(self.nRainhas):
                print(" R " if self.tabuleiro[linha][coluna] == True else " - ", end="")
            print("")

        print("\n\n--------------------------------------------------------------------------------------------------------------------\n\n")

        print("Solucao otima encontrada!" if self.energia == 0 else "Solucao otima nao encontrada!")