num = int(input("Digite um número:"))

if num < 0:
    print("Não é possível calcular a raiz quadrada d eum número negativo")
elif num > 100:
    print("Número muito grande, reduza para um valor abaixo de 100")
else:
    resultado = num**0.5
    print(f"Raiz quadrada: {resultado}")


