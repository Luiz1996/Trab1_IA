class EstadoTabuleiro:
    tabuleiro = []
    nRainhas = 0

    def __init__(self, qtdeRainhas):
        self.nRainhas = qtdeRainhas

        self.tabuleiro = []
    
        for linha in range(self.nRainhas):
            linhas = []
            for coluna in range(self.nRainhas):
                linhas.append(False)
            self.tabuleiro.append(linhas)
        self.tabuleiro = self.algoritmoDeRetrocesso(self.tabuleiro, qtdeRainhas)

    def algoritmoDeRetrocesso(self, tabuleiro, qtdeRainhas):
        if self.verificaRetrocesso(0, qtdeRainhas, tabuleiro):
            return tabuleiro

    def verificaRetrocesso(self, coluna, qtdeRainhas, tabuleiro):
        if coluna >= qtdeRainhas:
            return True
        
        for i in range(qtdeRainhas):
            if (self.verificaColisao(qtdeRainhas, coluna, i, tabuleiro)):
                tabuleiro[i][coluna] = True

                if (self.verificaRetrocesso(coluna+1, qtdeRainhas, tabuleiro)):
                    return True
                
                tabuleiro[i][coluna] = False
                
        return False

    def verificaColisao(self, qtdeRainhas, coluna, linha, tabuleiro):
        for i in range(coluna):
            if tabuleiro[linha][i] == True:
                return False
        
        for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
            if tabuleiro[i][j] == True:
                return False
        
        for i, j in zip(range(linha, qtdeRainhas, 1), range(coluna, -1, -1)):
            if tabuleiro[i][j] == True:
                return False
        
        return True

    def imprimirTabuleiro(self):
        print("\n\n--------------------------------------------------------------------------------------------------------------------\n\n")
        print("Impressao do resultado:")
        for linha in range(self.nRainhas):
            for coluna in range(self.nRainhas):
                print("[R]" if self.tabuleiro[linha][coluna] == True else "[ ]", end="")
            print("")

        print("\n\n--------------------------------------------------------------------------------------------------------------------\n\n")

       