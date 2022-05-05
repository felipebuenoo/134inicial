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


def testar_somar():
    # 1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido

    # Escrevi isso no não vi comparação
