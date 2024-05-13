# Exemplo calculadora em python com funções

import math
import matplotlib.pyplot as plt
import numpy as np

def somar(a, b):
    # Função que realiza a soma de dois numeros(somente numeros)
    try:
        res = float(a) + float(b)
    except:
        return "Operação não pode ser realizada!"
    else:
        return "Soma = " f"{res:5.2f}"

def subtrair(a, b):
    # Função que realiza a subtração de dois numeros(somente numeros)
    try:
        res = float(a) - float(b)
    except:
        return "Operação não pode ser realizada!"
    else:
        return "Subtração = " f"{res:5.2f}"

def multiplicar(a, b):
    try:
        res = float(a) * float(b)
    except:
        return "Operação não pode ser realizada!"
    else:
        return f"Multiplicação = {res:5.2f}"

def dividir(a, b):
    try:
        res = float(a) / float(b)
    except:
        return "Operação não pode ser realizada!"
    else:
        return f"Divisão = {res:5.2f}"

def potencia(a, b):
    try:
        res = float(a) ** float(b)
    except:
        return "Operação não pode ser realizada!"
    else:
        return f"Potenciação = {res:5.2f}"

def raiz(a):
    try:
        res = math.sqrt(float(a))
    except:
        return "Operação não pode ser realizada!"
    else:
        return f"Raiz Quadrada = {res:5.2f}"

def f(x, a, b, c):
    return a * x**2 + b * x + c

def polinomio(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        delta = (b**2) - (4 * a * c)
        resultado = f"Polinômio = Delta: O valor de Δ é {delta}\n"

        if delta >= 0:
            if a != 0:
                raiz_quadrada = math.sqrt(delta)
                resultado += "As raízes são:\n"
                x1 = (-b + raiz_quadrada) / (2 * a)
                x2 = (-b - raiz_quadrada) / (2 * a)
                resultado += f"Raiz 1: {x1:.2f}\n"
                resultado += f"Raiz 2: {x2:.2f}\n"

                # Gerar valores para o eixo x
                x = np.linspace(min(x1, x2) - 1, max(x1, x2) + 1, 400)
                y = f(x, a, b, c)

                # Plotar o gráfico da função
                plt.plot(x, y, label=f"f(x) = {a}x^2 + {b}x + {c}")
                plt.title("Gráfico da Função Quadrática")
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.grid(True)
                plt.axhline(0, color="black", linewidth=0.5)
                plt.axvline(0, color="black", linewidth=0.5)

                # Marcar as raízes no gráfico
                plt.scatter([x1, x2], [0, 0], color="red", label="Raízes")

                print(resultado)
                plt.show()

            else:
                print("Não é possível realizar a divisão por 0! Portanto o polinômio não pussui raízes reais. Não é possível gerar o gráfico.\n")
        else:
            print("O polinômio possui Δ negativo. Portanto o polinômio possui raízes complexas. Não é possível gerar o gráfico.\n")
    except ValueError:
        return "Os valores de A, B e C precisam ser números!\n"