import pytest

def imprimir_oi(nome):
    print(f'Oi, {nome}')

def somar(número_A, número_B):
    resultado = número_A + número_B
    return resultado


if __name__ == '__main__':
    imprimir_oi('Léo')

    resultado_final = somar(5,7)
    print(f'A soma: {resultado_final}')


def teste_somar():
    #1 - Configura
