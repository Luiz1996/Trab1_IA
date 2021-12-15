from EstadoTabuleiro import EstadoTabuleiro
import random
import time
import math

def tempoAtualMili():
    return round(time.time() * 1000)

def obterValorRandomico(intervaloMinimo, intervaloMaximo):
    return random.uniform(intervaloMinimo,intervaloMaximo)

def copiaTabuleiros(tabuleiro1, tabuleiro2):
    tabuleiro1.setEnergia(tabuleiro2.getEnergia())
    tabuleiro1.setTabuleiro(tabuleiro2.getTabuleiro())

def main():
    qtdeRainhas = 0 #int 
    tempoInicial = 0 #long 
    decrementoTemp = 0 #double
    temperaturaFinal = 0 #double
    qtdeEstadosPorRodada = 0 #int 
    temperaturaInicial = 0 #double

    while True:
        decrementoTemp = obterValorRandomico(0.5, 0.9)

        qtdeRainhas = int(input("Informe a quantidade de Rainhas(>=4): "))

        if qtdeRainhas < 4:
            print("A quantidade de rainhas informada é inválida!")
            print("\n\n--------------------------------------------------------------------------------------------------------------------\n\n")
            continue
        
        temperaturaInicial = float(input("Informe a temperatura inicial.......: "))
        
        temperaturaFinal = float(input("Informe a temperatura final.........: "))

        qtdeEstadosPorRodada = int(input("Qtde de estados gerados por rodada..: "))
        
        print("Decremento de tempe. em ", "{:.2f}".format(decrementoTemp), " graus...\n" )
        
        estadoAtual = EstadoTabuleiro(qtdeRainhas)
        
        melhorEstado = EstadoTabuleiro(qtdeRainhas)
		
        novoEstado =  EstadoTabuleiro(qtdeRainhas)

        tempoInicial = tempoAtualMili()

        while temperaturaInicial > temperaturaFinal:
            for estadoRodadaAtual in range(qtdeEstadosPorRodada):
                novoEstado = estadoAtual.gerarNovoEstado()

                delta = (novoEstado.getEnergia() - estadoAtual.getEnergia())
                if delta < 0.0:
                    copiaTabuleiros(estadoAtual, novoEstado)
                     
                    if novoEstado.getEnergia() < melhorEstado.getEnergia():
                        copiaTabuleiros(melhorEstado, novoEstado)

                        if melhorEstado.getEnergia() == 0.0:
                            break
                else:
                    numeroRandomico = obterValorRandomico(0, 1)
                    valorProbabilidadeTroca = math.exp((- delta) / temperaturaInicial)

                    if numeroRandomico < valorProbabilidadeTroca:
                        copiaTabuleiros(estadoAtual, novoEstado)

            if melhorEstado.getEnergia() == 0.0:
                temperaturaInicial = 0
            temperaturaInicial -= decrementoTemp

        melhorEstado.imprimirTabuleiro()
      
        print("A execucao levou ", int((tempoAtualMili() - tempoInicial) / 1000), " segundos(s).")
        print("\n\n--------------------------------------------------------------------------------------------------------------------\n\n")

main()