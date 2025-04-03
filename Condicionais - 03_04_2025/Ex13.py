temp = float(input("Digite a temperatura em Celsius:"))

if temp < 10:
    print("Frio")
elif temp > 10 and temp < 25:
    print("Aconchegante")
elif temp > 25 and temp < 40:
    print("Quente")
else:
    print("Muito")