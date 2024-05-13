# Importando o módulo da calculadora
import calculos

def menu():
    print("\n=== Calculadora ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Resolver Polinômio")
    print("8. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção (1-8): ")

        if opcao == '1':
            print(calculos.somar(input("Entre com o primeiro valor: "), input("Entre com o segundo valor: ")))
        elif opcao == '2':
            print(calculos.subtrair(input("Entre com o primeiro valor: "), input("Entre com o segundo valor: ")))
        elif opcao == '3':
            print(calculos.multiplicar(input("Entre com o primeiro valor: "), input("Entre com o segundo valor: ")))
        elif opcao == '4':
            print(calculos.dividir(input("Entre com o primeiro valor: "), input("Entre com o segundo valor: ")))
        elif opcao == '5':
            print(calculos.potencia(input("Entre com a base: "), input("Entre com o expoente: ")))
        elif opcao == '6':
            print(calculos.raiz(input("Digite o número para calcular a raiz quadrada: ")))
        elif opcao == '7':
            print(calculos.polinomio(input("Entre com o valor de A: "), input("Entre com o valor de B: "), input("Entre com o valor de C: ")))
        elif opcao == '8':
            print("Até mais!!!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
main()