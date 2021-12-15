from EstadoTabuleiro import EstadoTabuleiro
import time
def tempoAtualMili():
    return round(time.time() * 1000)

def main():
    qtdeRainhas = 0
    while True:
        qtdeRainhas = int(input("Informe a quantidade de Rainhas(>=4): "))

        if qtdeRainhas < 4:
            print("A quantidade de rainhas informada é inválida!")
            print("\n\n--------------------------------------------------------------------------------------------------------------------\n\n")
            continue

        tempoInicial = tempoAtualMili()

        tabuleiroFinal = EstadoTabuleiro(qtdeRainhas)

        tabuleiroFinal.imprimirTabuleiro()

        print("A execucao levou ", int((tempoAtualMili() - tempoInicial) / 1000), " segundos(s).")
        print("\n\n--------------------------------------------------------------------------------------------------------------------\n\n")
main()